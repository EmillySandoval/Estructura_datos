#include <iostream>
#include <windows.h>
#include <conio.h>
#include <string>
#include <vector>
#include <fstream>
#include <ctime>
#include <algorithm>

using namespace std;

#define VERDE       10
#define ROJO        12
#define AMARILLO    14
#define BLANCO      15
#define GRIS        8

const int ANCHO = 20;
const int ALTO = 20;

HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);

struct Punto {
    int x, y;
};

struct Nodo {
    Punto pos;
    Nodo* sig;
    Nodo* ant;
};

struct Jugador {
    string nombre;
    int puntaje;
    int nivel;

    bool operator<(const Jugador& otro) const {
        return puntaje > otro.puntaje;
    }
};

class ListaEnlazada {
public:
    Nodo* cabeza;
    Nodo* cola;
    int tamano;

    ListaEnlazada() {
        cabeza = nullptr;
        cola = nullptr;
        tamano = 0;
    }

    ~ListaEnlazada() {
        limpiar();
    }

    void insertarCabeza(Punto p) {
        Nodo* nuevo = new Nodo;
        nuevo->pos = p;
        nuevo->ant = nullptr;
        nuevo->sig = cabeza;

        if (cabeza != nullptr) {
            cabeza->ant = nuevo;
        }

        cabeza = nuevo;

        if (cola == nullptr) {
            cola = nuevo;
        }

        tamano++;
    }

    void eliminarCola() {
        if (cola == nullptr) {
            return;
        }

        Nodo* temp = cola;
        cola = cola->ant;

        if (cola != nullptr) {
            cola->sig = nullptr;
        } else {
            cabeza = nullptr;
        }

        delete temp;
        tamano--;
    }

    bool chocaConsigo(Punto p) {
        if (cabeza == nullptr) return false;

        Nodo* actual = cabeza->sig;

        while (actual != nullptr) {
            if (actual->pos.x == p.x && actual->pos.y == p.y) {
                return true;
            }
            actual = actual->sig;
        }
        return false;
    }

    bool estaDentro(int x, int y) {
        Nodo* actual = cabeza;
        while (actual != nullptr) {
            if (actual->pos.x == x && actual->pos.y == y) {
                return true;
            }
            actual = actual->sig;
        }
        return false;
    }

    Punto obtenerCabeza() {
        if (cabeza != nullptr) {
            return cabeza->pos;
        }
        return {0, 0};
    }

    int obtenerTamano() {
        return tamano;
    }

    void limpiar() {
        while (cabeza != nullptr) {
            Nodo* temp = cabeza;
            cabeza = cabeza->sig;
            delete temp;
        }
        cola = nullptr;
        tamano = 0;
    }
};

string nombreJugador;
int velocidad;
int puntaje;
int nivel;
int comidaParaTrampa;
Punto comida;
Punto trampa;
bool hayComida;
bool hayTrampa;
ListaEnlazada serpiente;
int dir;
bool juegoTerminado;
bool juegoPausado;
vector<Jugador> ranking;

void gotoxy(int x, int y) {
    COORD coord;
    coord.X = x;
    coord.Y = y;
    SetConsoleCursorPosition(hConsole, coord);
}

void setColor(int color) {
    SetConsoleTextAttribute(hConsole, color);
}

void ocultarCursor() {
    CONSOLE_CURSOR_INFO info;
    info.dwSize = 100;
    info.bVisible = FALSE;
    SetConsoleCursorInfo(hConsole, &info);
}

void leerRanking() {
    ranking.clear();
    ifstream archivo("ranking.txt");

    if (archivo.is_open()) {
        Jugador j;
        while (archivo >> j.nombre >> j.puntaje >> j.nivel) {
            ranking.push_back(j);
        }
        archivo.close();
        sort(ranking.begin(), ranking.end());
    }
}

void guardarRanking() {
    ranking.push_back({nombreJugador, puntaje, nivel});
    sort(ranking.begin(), ranking.end());

    ofstream archivo("ranking.txt");
    if (archivo.is_open()) {
        int maxItems = min((int)ranking.size(), 3);
        for (int i = 0; i < maxItems; i++) {
            archivo << ranking[i].nombre << " "
                    << ranking[i].puntaje << " "
                    << ranking[i].nivel << endl;
        }
        archivo.close();
    }
}

void guardar() {
    ofstream archivo("partida.sav");
    if (!archivo.is_open()) {
        gotoxy(ANCHO + 3, 15);
        cout << "Error al guardar!";
        Sleep(1000);
        return;
    }

    archivo << puntaje << " " << nivel << " " << velocidad << " " << dir << " " << comidaParaTrampa << endl;
    archivo << hayComida << " " << comida.x << " " << comida.y << endl;
    archivo << hayTrampa << " " << trampa.x << " " << trampa.y << endl;

    archivo << serpiente.tamano << endl;
    Nodo* actual = serpiente.cola;
    while (actual != nullptr) {
        archivo << actual->pos.x << " " << actual->pos.y << endl;
        actual = actual->ant;
    }

    archivo.close();

    gotoxy(ANCHO + 3, 15);
    setColor(AMARILLO);
    cout << "Partida Guardada!";
    Sleep(1000);
    gotoxy(ANCHO + 3, 15);
    cout << "                 ";
}

bool cargar() {
    ifstream archivo("partida.sav");
    if (!archivo.is_open()) {
        return false;
    }

    serpiente.limpiar();

    archivo >> puntaje >> nivel >> velocidad >> dir >> comidaParaTrampa;
    archivo >> hayComida >> comida.x >> comida.y;
    archivo >> hayTrampa >> trampa.x >> trampa.y;

    int tamanoGuardado;
    archivo >> tamanoGuardado;
    for (int i = 0; i < tamanoGuardado; i++) {
        Punto p;
        archivo >> p.x >> p.y;
        serpiente.insertarCabeza(p);
    }

    archivo.close();
    return true;
}

void dibujarMarco() {
    setColor(GRIS);

    gotoxy(0, 0); cout << "+";
    gotoxy(ANCHO + 1, 0); cout << "+";
    gotoxy(0, ALTO + 1); cout << "+";
    gotoxy(ANCHO + 1, ALTO + 1); cout << "+";

    for (int x = 1; x <= ANCHO; x++) {
        gotoxy(x, 0); cout << "-";
        gotoxy(x, ALTO + 1); cout << "-";
    }

    for (int y = 1; y <= ALTO; y++) {
        gotoxy(0, y); cout << "|";
        gotoxy(ANCHO + 1, y); cout << "|";
    }
}

void generarItem(bool esTrampa) {
    int x, y;
    do {
        x = (rand() % ANCHO) + 1;
        y = (rand() % ALTO) + 1;
    } while (serpiente.estaDentro(x, y));

    if (esTrampa) {
        trampa = {x, y};
        hayTrampa = true;
        gotoxy(x, y);
        setColor(AMARILLO);
        cout << "T";
    } else {
        comida = {x, y};
        hayComida = true;
        gotoxy(x, y);
        setColor(ROJO);
        cout << "M";
    }
}

void iniciar(bool esPartidaCargada) {
    system("cls");
    dibujarMarco();
    ocultarCursor();

    if (!esPartidaCargada) {
        serpiente.limpiar();
        puntaje = 0;
        nivel = 1;
        velocidad = 150;
        dir = 4;
        comidaParaTrampa = 0;
        hayComida = false;
        hayTrampa = false;

        Punto p = {6, 10};
        serpiente.insertarCabeza(p);
        p.x = 7; serpiente.insertarCabeza(p);
        p.x = 8; serpiente.insertarCabeza(p);
        p.x = 9; serpiente.insertarCabeza(p);
        p.x = 10; serpiente.insertarCabeza(p);

        generarItem(false);
    }

    juegoTerminado = false;
    juegoPausado = false;
}

void dibujar() {
    setColor(VERDE);
    Nodo* actual = serpiente.cabeza;

    if(actual != nullptr) {
        gotoxy(actual->pos.x, actual->pos.y);
        cout << "O";
        actual = actual->sig;
    }

    while (actual != nullptr) {
        gotoxy(actual->pos.x, actual->pos.y);
        cout << "o";
        actual = actual->sig;
    }

    setColor(BLANCO);
    gotoxy(ANCHO + 3, 2); cout << "Jugador: " << nombreJugador;
    gotoxy(ANCHO + 3, 4); cout << "Puntaje: " << puntaje << "  ";
    gotoxy(ANCHO + 3, 5); cout << "Nivel:   " << nivel << "  ";
    gotoxy(ANCHO + 3, 6); cout << "Tamano:  " << serpiente.obtenerTamano() << "  ";
    gotoxy(ANCHO + 3, 8); cout << "CONTROLES:";
    gotoxy(ANCHO + 3, 9); cout << "W/A/S/D = Mover";
    gotoxy(ANCHO + 3, 10); cout << "P = Pausa";
    gotoxy(ANCHO + 3, 11); cout << "G = Guardar";
}

void input() {
    if (_kbhit()) {
        char tecla = _getch();

        if (tecla == 0 || tecla == -32) {
            tecla = _getch();
        }

        switch (tolower(tecla)) {
            case 'w':
                if (dir != 2) dir = 1;
                break;
            case 's':
                if (dir != 1) dir = 2;
                break;
            case 'a':
                if (dir != 4) dir = 3;
                break;
            case 'd':
                if (dir != 3) dir = 4;
                break;
            case 'p':
                juegoPausado = !juegoPausado;
                if (juegoPausado) {
                    gotoxy(ANCHO / 2 - 3, ALTO / 2);
                    setColor(AMARILLO);
                    cout << " PAUSA ";
                } else {
                    gotoxy(ANCHO / 2 - 3, ALTO / 2);
                    cout << "       ";
                }
                break;
            case 'g':
                if (!juegoPausado) {
                     guardar();
                }
                break;
        }
    }
}

void logica() {
    Punto nuevaCabeza = serpiente.obtenerCabeza();
    Punto colaAntigua = serpiente.cola->pos;

    switch (dir) {
        case 1: nuevaCabeza.y--; break;
        case 2: nuevaCabeza.y++; break;
        case 3: nuevaCabeza.x--; break;
        case 4: nuevaCabeza.x++; break;
    }

    if (nuevaCabeza.x > ANCHO) nuevaCabeza.x = 1;
    if (nuevaCabeza.x < 1) nuevaCabeza.x = ANCHO;
    if (nuevaCabeza.y > ALTO) nuevaCabeza.y = 1;
    if (nuevaCabeza.y < 1) nuevaCabeza.y = ALTO;

    if (serpiente.chocaConsigo(nuevaCabeza)) {
        juegoTerminado = true;
        return;
    }

    serpiente.insertarCabeza(nuevaCabeza);

    bool comio = false;

    if (hayComida && nuevaCabeza.x == comida.x && nuevaCabeza.y == comida.y) {
        comio = true;
        puntaje += 10;
        hayComida = false;
        comidaParaTrampa++;
        generarItem(false);
    }

    else if (hayTrampa && nuevaCabeza.x == trampa.x && nuevaCabeza.y == trampa.y) {
        comio = true;
        hayTrampa = false;

        serpiente.eliminarCola();
        Punto colaBorrada1 = colaAntigua;
        gotoxy(colaBorrada1.x, colaBorrada1.y); cout << " ";

        if (serpiente.obtenerTamano() > 1) {
             Punto colaBorrada2 = serpiente.cola->pos;
             serpiente.eliminarCola();
             gotoxy(colaBorrada2.x, colaBorrada2.y); cout << " ";
        }

        if (serpiente.obtenerTamano() < 2) {
            juegoTerminado = true;
            return;
        }
    }

    else {
        serpiente.eliminarCola();
        gotoxy(colaAntigua.x, colaAntigua.y);
        cout << " ";
    }

    if (comidaParaTrampa >= 5 && !hayTrampa) {
        generarItem(true);
        comidaParaTrampa = 0;
    }

    if (serpiente.obtenerTamano() > 15) {
        nivel++;
        velocidad = max(40, velocidad - 20);

        gotoxy(ANCHO / 2 - 5, ALTO / 2);
        setColor(VERDE);
        cout << "NIVEL " << nivel << "!";
        Sleep(1000);
        gotoxy(ANCHO / 2 - 5, ALTO / 2);
        cout << "          ";

        while (serpiente.obtenerTamano() > 5) {
            Punto colaBorrada = serpiente.cola->pos;
            serpiente.eliminarCola();
            gotoxy(colaBorrada.x, colaBorrada.y);
            cout << " ";
        }
    }
}

void bucle() {
    while (!juegoTerminado) {

        input();

        if (!juegoPausado) {
            logica();
        }

        if (!juegoTerminado) {
            dibujar();
        }

        if (!juegoTerminado) {
             Sleep(velocidad);
        }
    }
}

void mostrarRanking() {
    setColor(AMARILLO);
    gotoxy(10, 5); cout << "--- RANKING ---";
    if (ranking.empty()) {
        gotoxy(5, 7);
        setColor(GRIS);
        cout << "(Aun no hay puntajes guardados)";
    } else {
        setColor(BLANCO);
        for (int i = 0; i < ranking.size() && i < 3; i++) {
            gotoxy(5, 7 + i);
            cout << i + 1 << ". " << ranking[i].nombre
                 << " - Puntaje: " << ranking[i].puntaje
                 << " - Nivel: " << ranking[i].nivel;
        }
    }
}

int menu() {
    system("cls");
    leerRanking();

    setColor(VERDE);
    gotoxy(10, 2); cout << "SNAKE (Estructura de Datos)";

    mostrarRanking();

    setColor(BLANCO);
    gotoxy(5, 12); cout << "Ingresa tu nombre: ";
    setColor(VERDE);
    getline(cin, nombreJugador);

    if (nombreJugador.empty()) nombreJugador = "Jugador";
    for(char& c : nombreJugador) {
        if (c == ' ') c = '_';
    }

    setColor(BLANCO);
    gotoxy(5, 14); cout << "Elige una opcion:";
    gotoxy(5, 15); cout << "1. Partida Nueva";
    gotoxy(5, 16); cout << "2. Cargar Partida";
    gotoxy(5, 17); cout << "3. Salir";

    char opcion = '0';
    while (opcion != '1' && opcion != '2' && opcion != '3') {
        opcion = _getch();
    }

    if(opcion == '3') exit(0);

    return (opcion == '1') ? 1 : 2;
}

int main() {
    srand(time(nullptr));
    ocultarCursor();

    int opcionMenu = menu();

    bool partidaCargada = false;
    if (opcionMenu == 2) {
        if (!cargar()) {
            gotoxy(5, 19);
            cout << "No se encontro partida guardada. Iniciando nueva...";
            Sleep(1500);
            iniciar(false);
        } else {
            partidaCargada = true;
            iniciar(true);
        }
    } else {
        iniciar(false);
    }

    bucle();

    system("cls");
    setColor(ROJO);
    gotoxy(10, 5); cout << "!!! JUEGO TERMINADO !!!";

    guardarRanking();
    mostrarRanking();

    setColor(GRIS);
    gotoxy(5, 20); cout << "Presiona cualquier tecla para salir...";
    _getch();

    setColor(BLANCO);
    return 0;
}