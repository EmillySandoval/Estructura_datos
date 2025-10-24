#include <iostream>
#include <cstdlib>
#include <ctime>
#include <conio.h>
#include <windows.h>
#include <vector>
#include <chrono>
#include <thread>
#include <iomanip>
#include <fstream>
#include <algorithm>
#include <sstream>
using namespace std;

const int TAMANO = 20;

// Estructura mejorada para el ranking según la imagen
struct Puntuacion {
    string nombre;
    int puntuacionTotal;
    double tiempoTotal;
    string tiempoFormateado;
    int movimientos;
    int tesoros;
    string fechaHora;
};

char tablero[TAMANO][TAMANO];
bool visible[TAMANO][TAMANO];
int filaJugador, columnaJugador;
int vidas = 3, energia = 4;
int pasosSinChoque = 0;
int tesorosEncontrados = 0;
int tesorosVida = 0, tesorosEnergia = 0, tesorosRevelacion = 0;
bool tieneLlave = false;
vector<char> inventario;
int nivelActual = 1;
bool juegoActivo = true;
string nombreJugador;

// Variables para efectos temporales
bool revelarTrampasTemporal = false;
bool revelarLlaveTemporal = false;
bool revelarPuertaTemporal = false;
bool revelarAlrededorTemporal = false;
chrono::steady_clock::time_point tiempoRevelacionTrampas;
chrono::steady_clock::time_point tiempoRevelacionLlave;
chrono::steady_clock::time_point tiempoRevelacionPuerta;
chrono::steady_clock::time_point tiempoRevelacionAlrededor;

// Variables para cronómetro
chrono::steady_clock::time_point inicioNivel;
chrono::steady_clock::time_point finNivel;
chrono::steady_clock::time_point inicioJuego;

// Puntuaciones por nivel
int puntuacionNivel1 = 0, puntuacionNivel2 = 0, puntuacionNivel3 = 0;
double tiempoNivel1 = 0, tiempoNivel2 = 0, tiempoNivel3 = 0;

// Símbolos para mostrar lo que había en las casillas
char simbolosPasados[TAMANO][TAMANO];

// Vector para el ranking
vector<Puntuacion> ranking;

// Contador de movimientos
int movimientosTotales = 0;

void colorTexto(int color) {
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), color);
}

// Función para formatear el tiempo en minutos y segundos
string formatearTiempo(double segundos) {
    int minutos = static_cast<int>(segundos) / 60;
    int segs = static_cast<int>(segundos) % 60;
    stringstream ss;
    ss << setfill('0') << setw(2) << minutos << ":" << setfill('0') << setw(2) << segs;
    return ss.str();
}

// Función para obtener la fecha y hora actual
string obtenerFechaHora() {
    time_t ahora = time(0);
    tm* tiempoLocal = localtime(&ahora);
    stringstream ss;
    ss << put_time(tiempoLocal, "%Y-%m-%d %H:%M:%S");
    return ss.str();
}

// Función para cargar el ranking desde archivo
void cargarRanking() {
    ifstream archivo("ranking.txt");
    ranking.clear();

    if (archivo.is_open()) {
        string linea;
        while (getline(archivo, linea)) {
            stringstream ss(linea);
            Puntuacion p;
            string puntuacionStr, tiempoStr, movimientosStr, tesorosStr;

            getline(ss, p.nombre, ',');
            getline(ss, puntuacionStr, ',');
            getline(ss, tiempoStr, ',');
            getline(ss, movimientosStr, ',');
            getline(ss, tesorosStr, ',');
            getline(ss, p.fechaHora);

            p.puntuacionTotal = stoi(puntuacionStr);
            p.tiempoTotal = stod(tiempoStr);
            p.movimientos = stoi(movimientosStr);
            p.tesoros = stoi(tesorosStr);
            p.tiempoFormateado = formatearTiempo(p.tiempoTotal);

            ranking.push_back(p);
        }
        archivo.close();
    }
}

// Función para guardar el ranking en archivo
void guardarRanking() {
    ofstream archivo("ranking.txt");

    if (archivo.is_open()) {
        for (const auto& p : ranking) {
            archivo << p.nombre << ","
                    << p.puntuacionTotal << ","
                    << p.tiempoTotal << ","
                    << p.movimientos << ","
                    << p.tesoros << ","
                    << p.fechaHora << endl;
        }
        archivo.close();
    }
}

// Función para agregar una puntuación al ranking
void agregarAlRanking(const string& nombre, int puntuacion, double tiempo, int movs, int teso) {
    Puntuacion nueva;
    nueva.nombre = nombre;
    nueva.puntuacionTotal = puntuacion;
    nueva.tiempoTotal = tiempo;
    nueva.movimientos = movs;
    nueva.tesoros = teso;
    nueva.fechaHora = obtenerFechaHora();
    nueva.tiempoFormateado = formatearTiempo(tiempo);

    ranking.push_back(nueva);

    // Ordenar el ranking por puntuación (descendente)
    sort(ranking.begin(), ranking.end(), [](const Puntuacion& a, const Puntuacion& b) {
        return a.puntuacionTotal > b.puntuacionTotal;
    });

    // Mantener solo las top 10 puntuaciones
    if (ranking.size() > 10) {
        ranking.resize(10);
    }

    guardarRanking();
}

// Función para mostrar el ranking en el formato de la imagen
void mostrarRanking() {
    system("cls");
    colorTexto(14);
    cout << "========== RANKING TOP 10 ==========" << endl;
    colorTexto(7);

    if (ranking.empty()) {
        colorTexto(8);
        cout << "No hay puntuaciones registradas todavia." << endl;
    } else {
        cout << "TOP 10 PUNTUACIONES" << endl << endl;

        for (size_t i = 0; i < ranking.size(); i++) {
            if (i == 0) colorTexto(14);
            else if (i == 1) colorTexto(8);
            else if (i == 2) colorTexto(6);
            else colorTexto(7);

            cout << i + 1 << ". " << ranking[i].nombre << ": " << ranking[i].puntuacionTotal << " pts" << endl;
            cout << "   " << ranking[i].tiempoFormateado << " | \u2605 " << ranking[i].movimientos << " mov" << endl;
            cout << "   " << ranking[i].tesoros << " tesoros | \u270D " << ranking[i].fechaHora << endl;

            if (i < ranking.size() - 1) cout << endl;
        }
    }

    colorTexto(7);
    cout << "\n Presiona cualquier tecla para continuar...";
    getch();
}

// Función para registrar el nombre del jugador
void registrarJugador() {
    system("cls");
    colorTexto(11);
    cout << "=== REGISTRO DE JUGADOR ===" << endl;
    colorTexto(7);
    cout << "Ingresa tu nombre: ";
    getline(cin, nombreJugador);

    if (nombreJugador.empty()) {
        nombreJugador = "Jugador";
    }

    cout << "\n Bienvenido: " << nombreJugador << "!" << endl;
    cout << "Preparate para la aventura..." << endl;
    Sleep(2000);
}

// Función para preguntar si desea nueva partida o cargar partida guardada
bool preguntarTipoPartida() {
    system("cls");
    colorTexto(11);
    cout << "=== BIENVENIDO AL JUEGO ===" << endl;
    colorTexto(7);
    cout << "Selecciona el tipo de partida:" << endl;
    cout << "1. Nueva partida" << endl;
    cout << "2. Cargar partida guardada" << endl;
    cout << "Ingresa tu opcion (1-2): ";

    char opcion;
    cin >> opcion;
    cin.ignore();

    return (opcion == '2'); // true si quiere cargar partida
}

// Función para guardar el estado del juego
void guardarPartida() {
    ofstream archivo("partida_guardada.txt");

    if (archivo.is_open()) {
        // Guardar estado actual del juego
        archivo << nombreJugador << endl;
        archivo << nivelActual << endl;
        archivo << vidas << endl;
        archivo << energia << endl;
        archivo << tesorosEncontrados << endl;
        archivo << tesorosVida << endl;
        archivo << tesorosEnergia << endl;
        archivo << tesorosRevelacion << endl;
        archivo << tieneLlave << endl;
        archivo << movimientosTotales << endl;
        archivo << filaJugador << endl;
        archivo << columnaJugador << endl;

        // Guardar inventario
        archivo << inventario.size() << endl;
        for (char item : inventario) {
            archivo << item << endl;
        }

        // Guardar tablero y visibilidad
        for (int i = 0; i < TAMANO; i++) {
            for (int j = 0; j < TAMANO; j++) {
                archivo << tablero[i][j];
            }
            archivo << endl;
        }

        for (int i = 0; i < TAMANO; i++) {
            for (int j = 0; j < TAMANO; j++) {
                archivo << (visible[i][j] ? '1' : '0');
            }
            archivo << endl;
        }

        for (int i = 0; i < TAMANO; i++) {
            for (int j = 0; j < TAMANO; j++) {
                archivo << simbolosPasados[i][j];
            }
            archivo << endl;
        }

        // Guardar puntuaciones por nivel
        archivo << puntuacionNivel1 << endl;
        archivo << puntuacionNivel2 << endl;
        archivo << puntuacionNivel3 << endl;
        archivo << tiempoNivel1 << endl;
        archivo << tiempoNivel2 << endl;
        archivo << tiempoNivel3 << endl;

        archivo.close();
        cout << "Partida guardada exitosamente!" << endl;
    } else {
        cout << "Error al guardar la partida." << endl;
    }
}

// Función para cargar partida guardada
bool cargarPartida() {
    ifstream archivo("partida_guardada.txt");

    if (!archivo.is_open()) {
        cout << "No se encontro partida guardada." << endl;
        return false;
    }

    string linea;

    // Cargar datos básicos
    getline(archivo, nombreJugador);
    archivo >> nivelActual;
    archivo >> vidas;
    archivo >> energia;
    archivo >> tesorosEncontrados;
    archivo >> tesorosVida;
    archivo >> tesorosEnergia;
    archivo >> tesorosRevelacion;
    archivo >> tieneLlave;
    archivo >> movimientosTotales;
    archivo >> filaJugador;
    archivo >> columnaJugador;
    archivo.ignore();

    // Cargar inventario
    int tamInventario;
    archivo >> tamInventario;
    archivo.ignore();
    inventario.clear();
    for (int i = 0; i < tamInventario; i++) {
        char item;
        archivo >> item;
        archivo.ignore();
        inventario.push_back(item);
    }

    // Cargar tablero
    for (int i = 0; i < TAMANO; i++) {
        getline(archivo, linea);
        for (int j = 0; j < TAMANO; j++) {
            tablero[i][j] = linea[j];
        }
    }

    // Cargar visibilidad
    for (int i = 0; i < TAMANO; i++) {
        getline(archivo, linea);
        for (int j = 0; j < TAMANO; j++) {
            visible[i][j] = (linea[j] == '1');
        }
    }

    // Cargar símbolos pasados
    for (int i = 0; i < TAMANO; i++) {
        getline(archivo, linea);
        for (int j = 0; j < TAMANO; j++) {
            simbolosPasados[i][j] = linea[j];
        }
    }

    // Cargar puntuaciones por nivel
    archivo >> puntuacionNivel1;
    archivo >> puntuacionNivel2;
    archivo >> puntuacionNivel3;
    archivo >> tiempoNivel1;
    archivo >> tiempoNivel2;
    archivo >> tiempoNivel3;

    archivo.close();

    // Reiniciar el cronómetro para el nivel actual
    inicioNivel = chrono::steady_clock::now();

    // CORRECCIÓN: Calcular el tiempo total correctamente
    double tiempoTotalCargado = tiempoNivel1 + tiempoNivel2 + tiempoNivel3;
    chrono::duration<double> duracionTotal(tiempoTotalCargado);


    cout << "Partida cargada exitosamente!" << endl;
    Sleep(2000);
    return true;
}

// Función para mostrar ranking después de cada nivel
void mostrarRankingNivel(int nivel, int puntuacion, double tiempo) {
    system("cls");
    colorTexto(14);
    cout << "========== RANKING - NIVEL " << nivel << " ==========" << endl;
    colorTexto(7);

    // Mostrar estadísticas del nivel actual
    cout << "Tu desempeno en el nivel " << nivel << ":" << endl;
    cout << "Puntuacion: " << puntuacion << " pts" << endl;
    cout << "Tiempo: " << formatearTiempo(tiempo) << endl;
    cout << "Tesoros encontrados: " << tesorosEncontrados << endl;
    cout << endl;

    // Mostrar ranking general
    cargarRanking(); // Recargar ranking actualizado

    if (ranking.empty()) {
        colorTexto(8);
        cout << "No hay puntuaciones registradas todavia." << endl;
    } else {
        cout << "TOP 10 PUNTUACIONES GLOBALES" << endl << endl;

        for (size_t i = 0; i < ranking.size(); i++) {
            if (i == 0) colorTexto(14);
            else if (i == 1) colorTexto(8);
            else if (i == 2) colorTexto(6);
            else colorTexto(7);

            cout << i + 1 << ". " << ranking[i].nombre << ": " << ranking[i].puntuacionTotal << " pts" << endl;
            cout << "   " << ranking[i].tiempoFormateado << " | \u2605 " << ranking[i].movimientos << " mov" << endl;
            cout << "   " << ranking[i].tesoros << " tesoros | \u270D " << ranking[i].fechaHora << endl;

            if (i < ranking.size() - 1) cout << endl;
        }
    }

    colorTexto(7);
    cout << "\n Presiona cualquier tecla para continuar...";
    getch();
}

void inicializarTablero(int nivel) {
    srand(time(0));

    for (int i = 0; i < TAMANO; i++) {
        for (int j = 0; j < TAMANO; j++) {
            tablero[i][j] = ' ';
            visible[i][j] = false;
            simbolosPasados[i][j] = ' ';
        }
    }

    // Ajustar dificultad según nivel
    int numParedes = 50 + (nivel - 1) * 10;
    // SOLO 6 TRAMPAS EN TOTAL
    int numTrampas = 6;
    int numTesoros = 12 + (nivel - 1) * 3;

    // Paredes
    for (int i = 0; i < numParedes; i++) {
        int f, c;
        do { f = rand() % TAMANO; c = rand() % TAMANO; } while (tablero[f][c] != ' ');
        tablero[f][c] = 'P';
    }

    // Tesoros (Vida, Energía, Revelación)
    for (int i = 0; i < numTesoros; i++) {
        int f, c;
        do { f = rand() % TAMANO; c = rand() % TAMANO; } while (tablero[f][c] != ' ');
        char tipoTesoro;
        int r = rand() % 3;
        tipoTesoro = (r == 0) ? 'V' : (r == 1) ? 'E' : 'R';
        tablero[f][c] = tipoTesoro;
    }

    // SOLO 6 TRAMPAS EN TOTAL
    for (int i = 0; i < numTrampas; i++) {
        int f, c;
        do { f = rand() % TAMANO; c = rand() % TAMANO; } while (tablero[f][c] != ' ');
        char tipoTrampa;
        if (i < 2) tipoTrampa = 'M';
        else if (i < 4) tipoTrampa = 'X';
        else tipoTrampa = 'Z';
        tablero[f][c] = tipoTrampa;
    }

    // Llave
    int f, c;
    do { f = rand() % TAMANO; c = rand() % TAMANO; } while (tablero[f][c] != ' ');
    tablero[f][c] = 'L';

    // Puerta de salida
    do { f = rand() % TAMANO; c = rand() % TAMANO; } while (tablero[f][c] != ' ');
    tablero[f][c] = 'S';

    // Posición inicial del jugador
    do { filaJugador = rand() % TAMANO; columnaJugador = rand() % TAMANO; } while (tablero[filaJugador][columnaJugador] != ' ');
    visible[filaJugador][columnaJugador] = true;
    tablero[filaJugador][columnaJugador] = '-';
    simbolosPasados[filaJugador][columnaJugador] = 'I';

    // Iniciar cronómetro
    inicioNivel = chrono::steady_clock::now();
}

// Modificar la función mostrarTablero para incluir opción de guardar
void mostrarTableroConOpciones() {
    system("cls");

    // Calcular tiempo transcurrido
    auto ahora = chrono::steady_clock::now();
    chrono::duration<double> tiempoTranscurridoNivel = ahora - inicioNivel;
    chrono::duration<double> tiempoTotalJuego = ahora - inicioJuego;

    cout << "=== NIVEL " << nivelActual << " ===";
    colorTexto(12); cout << " Vidas: " << vidas;
    colorTexto(11); cout << " Energia: " << energia;
    colorTexto(10); cout << " Llave: " << (tieneLlave ? "SI" : "NO");
    colorTexto(14); cout << " Jugador: " << nombreJugador;
    colorTexto(13); cout << " Movimientos: " << movimientosTotales;
    colorTexto(11); cout << " Tiempo: " << formatearTiempo(tiempoTotalJuego.count()) << endl;
    colorTexto(7);

    // Leyenda reducida para ahorrar espacio
    cout << "Leyenda: J(Tu) P(Pared) X/Z/M(Trampas) V/E/R(Tesoros) L(Llave) S(Puerta)" << endl;

    for (int i = 0; i < TAMANO; i++) {
        for (int j = 0; j < TAMANO; j++) {
            if (i == filaJugador && j == columnaJugador) {
                colorTexto(14); cout << "J ";
            } else if (visible[i][j]) {
                if (simbolosPasados[i][j] != ' ' && simbolosPasados[i][j] != '-' && tablero[i][j] == '-') {
                    switch (simbolosPasados[i][j]) {
                        case 'X': case 'Z': case 'M':
                            colorTexto(15); cout << "T "; break;
                        case 'V': case 'E': case 'R':
                            colorTexto(2); cout << "O "; break;
                        case 'L': colorTexto(3); cout << "L "; break;
                        case 'S': colorTexto(1); cout << "S "; break;
                        case 'I': colorTexto(14); cout << "I "; break;
                        default: colorTexto(8); cout << "- "; break;
                    }
                } else {
                    switch (tablero[i][j]) {
                        case 'P': colorTexto(12); cout << "P "; break;
                        case 'X': colorTexto(4); cout << "X "; break;
                        case 'Z': colorTexto(5); cout << "Z "; break;
                        case 'M': colorTexto(13); cout << "M "; break;
                        case 'V': colorTexto(10); cout << "V "; break;
                        case 'E': colorTexto(11); cout << "E "; break;
                        case 'R': colorTexto(6); cout << "R "; break;
                        case 'L': colorTexto(3); cout << "L "; break;
                        case 'S': colorTexto(1); cout << "S "; break;
                        case '-': colorTexto(8); cout << "- "; break;
                        default: colorTexto(7); cout << ". "; break;
                    }
                }
            } else {
                bool mostrar = false;
                char contenido = ' ';

                if (revelarTrampasTemporal && (tablero[i][j] == 'X' || tablero[i][j] == 'Z' || tablero[i][j] == 'M')) {
                    mostrar = true;
                    contenido = tablero[i][j];
                } else if (revelarLlaveTemporal && tablero[i][j] == 'L') {
                    mostrar = true;
                    contenido = 'L';
                } else if (revelarPuertaTemporal && tablero[i][j] == 'S') {
                    mostrar = true;
                    contenido = 'S';
                } else if (revelarAlrededorTemporal &&
                          abs(i - filaJugador) <= 1 && abs(j - columnaJugador) <= 1) {
                    mostrar = true;
                    contenido = tablero[i][j];
                }

                if (mostrar) {
                    switch (contenido) {
                        case 'P': colorTexto(12); cout << "P "; break;
                        case 'X': colorTexto(4); cout << "X "; break;
                        case 'Z': colorTexto(5); cout << "Z "; break;
                        case 'M': colorTexto(13); cout << "M "; break;
                        case 'V': colorTexto(10); cout << "V "; break;
                        case 'E': colorTexto(11); cout << "E "; break;
                        case 'R': colorTexto(6); cout << "R "; break;
                        case 'L': colorTexto(3); cout << "L "; break;
                        case 'S': colorTexto(1); cout << "S "; break;
                        case '-': colorTexto(8); cout << "- "; break;
                        default: colorTexto(8); cout << ". "; break;
                    }
                } else {
                    colorTexto(8); cout << ". ";
                }
            }
        }
        cout << endl;
    }

    colorTexto(15);
    cout << "Controles: Flechas (Moverse) | I (Inventario) | U (Usar Tesoro) | R (Ranking) | G (Guardar) | ESC (Salir)" << endl;
    colorTexto(7);
}

void mostrarInventario() {
    system("cls");
    colorTexto(11);
    cout << "========== INVENTARIO ==========" << endl;
    colorTexto(12); cout << "Vidas: " << vidas << endl;
    colorTexto(11); cout << "Energia: " << energia << endl;
    colorTexto(10); cout << "Tesoros encontrados: " << tesorosEncontrados << endl;
    colorTexto(10); cout << "Vida (V): " << tesorosVida << endl;
    colorTexto(11); cout << "Energia (E): " << tesorosEnergia << endl;
    colorTexto(6); cout << "Revelacion (R): " << tesorosRevelacion << endl;

    colorTexto(14);
    cout << "\n--- TESOROS EN INVENTARIO ---" << endl;
    if (inventario.empty()) {
        colorTexto(8);
        cout << "Inventario vacio" << endl;
    } else {
        for (size_t i = 0; i < inventario.size(); i++) {
            cout << i+1 << ". ";
            switch (inventario[i]) {
                case 'V': colorTexto(10); cout << "Tesoro de Vida"; break;
                case 'E': colorTexto(11); cout << "Tesoro de Energia"; break;
                case 'R': colorTexto(6); cout << "Tesoro de Revelacion"; break;
            }
            cout << endl;
        }
    }

    // MOSTRAR MENSAJE CUANDO EL INVENTARIO ESTÁ LLENO
    if (inventario.size() >= 5) {
        colorTexto(12);
        cout << "\n INVENTARIO LLENO. No puedes recoger mas tesoros." << endl;
    }

    colorTexto(7);
    cout << "\n Capacidad: " << inventario.size() << "/5" << endl;
    cout << "\n Presiona cualquier tecla para continuar...";
    getch();
}

void usarTesoro() {
    if (inventario.empty()) {
        cout << "No tienes tesoros para usar" << endl;
        getch();
        return;
    }

    bool usandoTesoro = true;
    while (usandoTesoro) {
        system("cls");
        colorTexto(11);
        cout << "======== USAR TESORO ========" << endl;
        cout << "Selecciona el tesoro a usar:" << endl;

        for (size_t i = 0; i < inventario.size(); i++) {
            cout << char('A' + i) << ". ";
            switch (inventario[i]) {
                case 'V': colorTexto(10); cout << "Tesoro de Vida (+1 vida)"; break;
                case 'E': colorTexto(11); cout << "Tesoro de Energia (+3 energia)"; break;
                case 'R': colorTexto(6); cout << "Tesoro de Revelacion"; break;
            }
            cout << endl;
        }
        cout << "X. Volver al juego" << endl;

        char opcion = getch();
        opcion = toupper(opcion);

        if (opcion == 'X') {
            return;
        }

        int indice = opcion - 'A';

        if (indice >= 0 && indice < (int)inventario.size()) {
            char tesoro = inventario[indice];

            switch (tesoro) {
                case 'V':
                    vidas++;
                    inventario.erase(inventario.begin() + indice);
                    cout << " Usaste un tesoro de vida +1 vida" << endl;
                    cout << "Presiona cualquier tecla para continuar..." << endl;
                    getch();
                    return;

                case 'E':
                    energia += 3;
                    inventario.erase(inventario.begin() + indice);
                    cout << " Usaste un tesoro de energia +3 energia" << endl;
                    cout << "Presiona cualquier tecla para continuar..." << endl;
                    getch();
                    return;

                case 'R':
                    system("cls");
                    colorTexto(6);
                    cout << "=== TESORO DE REVELACION ===" << endl;
                    colorTexto(7);
                    cout << "Elige que quieres revelar:" << endl;
                    cout << "1. Trampas (3 segundos)" << endl;
                    cout << "2. Llave (5 segundos)" << endl; // AUMENTADO A 5 SEGUNDOS
                    cout << "3. Puerta (5 segundos)" << endl;
                    cout << "4. Alrededor (2 segundos)" << endl;
                    cout << "X. Cancelar" << endl;

                    char eleccion = getch();
                    auto ahora = chrono::steady_clock::now();

                    switch (eleccion) {
                        case '1':
                            revelarTrampasTemporal = true;
                            tiempoRevelacionTrampas = ahora;
                            inventario.erase(inventario.begin() + indice);
                            cout << "Trampas reveladas por 3 segundos" << endl;
                            cout << "Presiona cualquier tecla para continuar..." << endl;
                            getch();
                            return;

                        case '2':
                            revelarLlaveTemporal = true;
                            tiempoRevelacionLlave = ahora;
                            inventario.erase(inventario.begin() + indice);
                            cout << "Llave revelada por 5 segundos" << endl; // AUMENTADO A 5 SEGUNDOS
                            cout << "Presiona cualquier tecla para continuar..." << endl;
                            getch();
                            return;

                        case '3':
                            revelarPuertaTemporal = true;
                            tiempoRevelacionPuerta = ahora;
                            inventario.erase(inventario.begin() + indice);
                            cout << "Puerta revelada por 5 segundos" << endl;
                            cout << "Presiona cualquier tecla para continuar..." << endl;
                            getch();
                            return;

                        case '4':
                            revelarAlrededorTemporal = true;
                            tiempoRevelacionAlrededor = ahora;
                            inventario.erase(inventario.begin() + indice);
                            cout << " Area alrededor revelada por 2 segundos" << endl;
                            cout << "Presiona cualquier tecla para continuar..." << endl;
                            getch();
                            return;

                        case 'x': case 'X':
                            break;

                        default:
                            cout << "Opcion invalida" << endl;
                            getch();
                            break;
                    }
                    break;
            }
        } else {
            cout << "Opcion invalida" << endl;
            getch();
        }
    }
}

void moverTablero() {
    int jugadorFila = filaJugador;
    int jugadorColumna = columnaJugador;
    char celdaJugador = tablero[jugadorFila][jugadorColumna];
    char simboloJugador = simbolosPasados[jugadorFila][jugadorColumna];

    char nuevoTablero[TAMANO][TAMANO];
    char nuevosSimbolos[TAMANO][TAMANO];
    for (int i = 0; i < TAMANO; i++) {
        for (int j = 0; j < TAMANO; j++) {
            nuevoTablero[i][j] = ' ';
            nuevosSimbolos[i][j] = ' ';
        }
    }

    for (int i = 0; i < TAMANO; i++) {
        for (int j = 0; j < TAMANO; j++) {
            if (i != jugadorFila || j != jugadorColumna) {
                int nuevaFila, nuevaColumna;
                do {
                    nuevaFila = rand() % TAMANO;
                    nuevaColumna = rand() % TAMANO;
                } while (nuevoTablero[nuevaFila][nuevaColumna] != ' ' ||
                        (nuevaFila == jugadorFila && nuevaColumna == jugadorColumna));

                nuevoTablero[nuevaFila][nuevaColumna] = tablero[i][j];
                nuevosSimbolos[nuevaFila][nuevaColumna] = simbolosPasados[i][j];
            }
        }
    }

    nuevoTablero[jugadorFila][jugadorColumna] = celdaJugador;
    nuevosSimbolos[jugadorFila][jugadorColumna] = simboloJugador;

    for (int i = 0; i < TAMANO; i++) {
        for (int j = 0; j < TAMANO; j++) {
            tablero[i][j] = nuevoTablero[i][j];
            simbolosPasados[i][j] = nuevosSimbolos[i][j];
            if (i != jugadorFila || j != jugadorColumna) {
                visible[i][j] = false;
            }
        }
    }
}

void actualizarEfectosTemporales() {
    auto ahora = chrono::steady_clock::now();

    if (revelarTrampasTemporal) {
        chrono::duration<double> tiempo = ahora - tiempoRevelacionTrampas;
        if (tiempo.count() >= 3.0) {
            revelarTrampasTemporal = false;
        }
    }

    if (revelarLlaveTemporal) {
        chrono::duration<double> tiempo = ahora - tiempoRevelacionLlave;
        if (tiempo.count() >= 5.0) { // AUMENTADO A 5 SEGUNDOS
            revelarLlaveTemporal = false;
        }
    }

    if (revelarPuertaTemporal) {
        chrono::duration<double> tiempo = ahora - tiempoRevelacionPuerta;
        if (tiempo.count() >= 5.0) {
            revelarPuertaTemporal = false;
        }
    }

    if (revelarAlrededorTemporal) {
        chrono::duration<double> tiempo = ahora - tiempoRevelacionAlrededor;
        if (tiempo.count() >= 2.0) {
            revelarAlrededorTemporal = false;
        }
    }
}

// NUEVA FUNCIÓN PARA PREGUNTAR SI QUIERE JUGAR DE NUEVO
bool preguntarNuevaPartida() {
    system("cls");
    colorTexto(14);
    cout << "=== GAME OVER ===" << endl;
    colorTexto(7);
    cout << " Quieres jugar otra partida " << endl;
    cout << "1. Si, nueva partida" << endl;
    cout << "2. No, salir del juego" << endl;
    cout << "Ingresa tu opcion (1-2): ";

    char opcion;
    cin >> opcion;
    cin.ignore();

    return (opcion == '1');
}

// Modificar la función completarNivel para reiniciar vidas y energía
void completarNivel() {
    finNivel = chrono::steady_clock::now();
    chrono::duration<double> tiempoNivel = finNivel - inicioNivel;
    int puntuacion = (vidas * 10 + energia + tesorosEncontrados * 5);

    system("cls");
    colorTexto(10);
    cout << "¡FELICIDADES " << nombreJugador << "! Has completado el nivel " << nivelActual << endl;
    colorTexto(7);
    cout << "Tiempo en nivel: " << formatearTiempo(tiempoNivel.count()) << endl;
    cout << "Puntuacion del nivel: " << puntuacion << endl;
    cout << "Vidas restantes: " << vidas << endl;
    cout << "Energia restante: " << energia << endl;
    cout << "Tesoros encontrados: " << tesorosEncontrados << endl;
    cout << "Movimientos: " << movimientosTotales << endl;

    switch (nivelActual) {
        case 1:
            puntuacionNivel1 = puntuacion;
            tiempoNivel1 = tiempoNivel.count();
            break;
        case 2:
            puntuacionNivel2 = puntuacion;
            tiempoNivel2 = tiempoNivel.count();
            break;
        case 3:
            puntuacionNivel3 = puntuacion;
            tiempoNivel3 = tiempoNivel.count();
            break;
    }

    cout << "\nPresiona cualquier tecla para ver el ranking..." << endl;
    getch();

    // MOSTRAR RANKING DESPUÉS DE CADA NIVEL
    mostrarRankingNivel(nivelActual, puntuacion, tiempoNivel.count());

    if (nivelActual < 3) {
        nivelActual++;
        tieneLlave = false;
        inventario.clear();
        tesorosEncontrados = 0;
        tesorosVida = 0;
        tesorosEnergia = 0;
        tesorosRevelacion = 0;
        // REINICIAR VIDAS Y ENERGÍA AL PASAR DE NIVEL
        vidas = 3;
        energia = 4;
        inicializarTablero(nivelActual);
    } else {
        auto finJuego = chrono::steady_clock::now();
        chrono::duration<double> tiempoTotal = finJuego - inicioJuego;
        int puntuacionTotal = puntuacionNivel1 + puntuacionNivel2 + puntuacionNivel3;
        int tesorosTotales = tesorosVida + tesorosEnergia + tesorosRevelacion;

        system("cls");
        colorTexto(14);
        cout << "¡FELICIDADES " << nombreJugador << "! HAS COMPLETADO TODOS LOS NIVELES!" << endl;
        colorTexto(7);
        cout << "=== RESULTADOS FINALES ===" << endl;
        cout << "Nivel 1 - Puntuacion: " << puntuacionNivel1 << " - Tiempo: " << formatearTiempo(tiempoNivel1) << endl;
        cout << "Nivel 2 - Puntuacion: " << puntuacionNivel2 << " - Tiempo: " << formatearTiempo(tiempoNivel2) << endl;
        cout << "Nivel 3 - Puntuacion: " << puntuacionNivel3 << " - Tiempo: " << formatearTiempo(tiempoNivel3) << endl;
        cout << "SUMA TOTAL - Puntuacion: " << puntuacionTotal << endl;
        cout << "Tiempo total: " << formatearTiempo(tiempoTotal.count()) << endl;
        cout << "Movimientos totales: " << movimientosTotales << endl;
        cout << "Tesoros totales: " << tesorosTotales << endl;

        agregarAlRanking(nombreJugador, puntuacionTotal, tiempoTotal.count(), movimientosTotales, tesorosTotales);

        cout << "\nPresiona cualquier tecla para ver el ranking final..." << endl;
        getch();

        mostrarRanking();
        juegoActivo = false;
    }
}

void moverJugador(int dx, int dy) {
    int nuevaFila = filaJugador + dx;
    int nuevaColumna = columnaJugador + dy;

    if (nuevaFila < 0 || nuevaFila >= TAMANO || nuevaColumna < 0 || nuevaColumna >= TAMANO) {
        cout << " No puedes salir del tablero" << endl;
        getch();
        return;
    }

    char celda = tablero[nuevaFila][nuevaColumna];

    if (celda == 'P') {
        visible[nuevaFila][nuevaColumna] = true;
        energia--;
        pasosSinChoque = 0;
        movimientosTotales++; // Contar movimiento incluso al chocar
        cout << " Choque con pared -1 energia" << endl;
        if (energia <= 0) {
            vidas--;
            energia = 0;
            cout << "Energia agotada -1 vida" << endl;
        }
        getch();
        return;
    }

    char simboloOriginal = celda;
    if (celda == 'X' || celda == 'Z' || celda == 'M') {
        simboloOriginal = celda;
    } else if (celda == 'V' || celda == 'E' || celda == 'R') {
        simboloOriginal = celda;
    }

    if (celda == 'X') {
        visible[nuevaFila][nuevaColumna] = true;
        vidas--;
        pasosSinChoque = 0;
        cout << "Trampa -1 vida" << endl;
        getch();
    } else if (celda == 'Z') {
        visible[nuevaFila][nuevaColumna] = true;
        energia = 0;
        pasosSinChoque = 0;
        cout << "Trampa de energia. Energia agotada" << endl;
        if (energia <= 0) {
            vidas--;
            cout << "Energia agotada -1 vida" << endl;
        }
        getch();
    } else if (celda == 'M') {
        visible[nuevaFila][nuevaColumna] = true;
        cout << "Trampa de movimiento. El tablero se ha movido..." << endl;
        moverTablero();
        getch();
    }

    filaJugador = nuevaFila;
    columnaJugador = nuevaColumna;
    movimientosTotales++; // Contar movimiento exitoso

    if (simboloOriginal != ' ' && simboloOriginal != '-') {
        simbolosPasados[filaJugador][columnaJugador] = simboloOriginal;
    }

    if (celda != 'S' || tieneLlave) {
        tablero[filaJugador][columnaJugador] = '-';
    }

    visible[filaJugador][columnaJugador] = true;

    pasosSinChoque++;
    if (pasosSinChoque >= 3) {
        energia++;
        pasosSinChoque = 0;
    }

    if (celda == 'V' || celda == 'E' || celda == 'R') {
        if (inventario.size() < 5) {
            inventario.push_back(celda);
            tesorosEncontrados++;

            switch (celda) {
                case 'V':
                    tesorosVida++;
                    cout << "Tesoro de vida encontrado .Agregado al inventario" << endl;
                    break;
                case 'E':
                    tesorosEnergia++;
                    cout << "Tesoro de energia encontrado. Agregado al inventario" << endl;
                    break;
                case 'R':
                    tesorosRevelacion++;
                    cout << "Tesoro de revelacion encontrado. Agregado al inventario" << endl;
                    break;
            }
        } else {
            // MENSAJE MEJORADO CUANDO EL INVENTARIO ESTÁ LLENO
            cout << "Inventario lleno, No puedes llevar mas tesoros. Usa algunos primero." << endl;
        }
        getch();
    } else if (celda == 'L') {
        tieneLlave = true;
        cout << "Llave encontrada, Ahora busca la puerta" << endl;
        getch();
    } else if (celda == 'S') {
        if (tieneLlave) {
            completarNivel();
        } else {
            cout << "Puerta encontrada. Necesitas la llave." << endl;
            getch();
        }
    }
}

// Modificar el main para incluir las nuevas funcionalidades
int main() {
    bool jugarDeNuevo = true;

    while (jugarDeNuevo) {
        cargarRanking();
        juegoActivo = true;

        // Preguntar tipo de partida
        if (preguntarTipoPartida()) {
            if (!cargarPartida()) {
                // Si no se pudo cargar partida, iniciar nueva
                registrarJugador();
                vidas = 3; // 20 vidas iniciales
                energia = 4; // 4 de energía inicial
                inicioJuego = chrono::steady_clock::now();
                inicializarTablero(nivelActual);
            } else {
                // CORRECCIÓN: Calcular el tiempo total correctamente
                double tiempoTotalCargado = tiempoNivel1 + tiempoNivel2 + tiempoNivel3;
                chrono::duration<double> duracionTotal(tiempoTotalCargado);
            }
        } else {
            registrarJugador();
            vidas = 3; // 3 vidas iniciales
            energia = 4; // 4 de energía inicial
            inicioJuego = chrono::steady_clock::now();
            inicializarTablero(nivelActual);
        }

        while (juegoActivo && vidas > 0) {
            actualizarEfectosTemporales();
            mostrarTableroConOpciones(); // Usar la nueva función con opciones

            char tecla = getch();
            if (tecla == -32) {
                tecla = getch();
                switch (tecla) {
                    case 72: moverJugador(-1, 0); break;
                    case 80: moverJugador(1, 0); break;
                    case 75: moverJugador(0, -1); break;
                    case 77: moverJugador(0, 1); break;
                }
            } else if (tecla == 'i' || tecla == 'I') {
                mostrarInventario();
            } else if (tecla == 'u' || tecla == 'U') {
                usarTesoro();
            } else if (tecla == 'r' || tecla == 'R') {
                mostrarRanking();
            } else if (tecla == 'g' || tecla == 'G') {
                guardarPartida();
                cout << "Partida guardada. Presiona cualquier tecla para continuar..." << endl;
                getch();
            } else if (tecla == 27) {
                // Preguntar si quiere guardar antes de salir
                system("cls");
                cout << " Deseas guardar la partida antes de salir (s/n): ";
                char respuesta = getch();
                if (respuesta == 's' || respuesta == 'S') {
                    guardarPartida();
                }
                juegoActivo = false;
            }
        }

        if (vidas <= 0) {
            auto finJuego = chrono::steady_clock::now();
            chrono::duration<double> tiempoTotal = finJuego - inicioJuego;
            int puntuacionTotal = puntuacionNivel1 + puntuacionNivel2 + (vidas > 0 ? puntuacionNivel3 : 0);
            int tesorosTotales = tesorosVida + tesorosEnergia + tesorosRevelacion;

            system("cls");
            colorTexto(12);
            cout << "GAME OVER " << nombreJugador << endl;
            colorTexto(7);
            cout << "Te quedaste sin vidas." << endl;
            cout << "Tiempo total de juego: " << formatearTiempo(tiempoTotal.count()) << endl;
            cout << "Puntuacion total: " << puntuacionTotal << endl;
            cout << "Movimientos totales: " << movimientosTotales << endl;
            cout << "Tesoros encontrados: " << tesorosTotales << endl;

            if (puntuacionTotal > 0) {
                agregarAlRanking(nombreJugador, puntuacionTotal, tiempoTotal.count(), movimientosTotales, tesorosTotales);
            }

            cout << "\nPresiona cualquier tecla para ver el ranking..." << endl;
            getch();

            mostrarRanking();

            // PREGUNTAR SI QUIERE JUGAR DE NUEVO
            jugarDeNuevo = preguntarNuevaPartida();

            // REINICIAR VARIABLES PARA NUEVA PARTIDA
            if (jugarDeNuevo) {
                nivelActual = 1;
                vidas = 3;
                energia = 4;
                tesorosEncontrados = 0;
                tesorosVida = 0;
                tesorosEnergia = 0;
                tesorosRevelacion = 0;
                tieneLlave = false;
                movimientosTotales = 0;
                inventario.clear();
                puntuacionNivel1 = puntuacionNivel2 = puntuacionNivel3 = 0;
                tiempoNivel1 = tiempoNivel2 = tiempoNivel3 = 0;
            }
        } else {
            jugarDeNuevo = false; // Si ganó, no preguntar
        }
    }

   return 0;
}
