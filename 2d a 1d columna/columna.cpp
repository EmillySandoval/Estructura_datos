#include <iostream>
using namespace std;

int main() {
    int matriz2D[3][3] = {{1,2,3},{4,5,6},{7,8,9}};
    int matriz1D[9], index = 0;

    cout << "Matriz 2D original:\n";
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            cout << matriz2D[i][j] << " ";
        }
        cout << endl;
    }

    for (int j = 0; j < 3; j++) {
        for (int i = 0; i < 3; i++) {
            matriz1D[index++] = matriz2D[i][j];
        }
    }

    cout << "\nMatriz 1D (por columnas):\n";
    for (int i = 0; i < 9; i++)
        cout << matriz1D[i] << " ";

 
}