#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++)
        for (int j = 0; j < n - i - 1; j++)
            if (arr[j] > arr[j + 1])
                swap(arr[j], arr[j + 1]);
}

int main() {
    const int SIZE = 20;
    int arr[SIZE];

    srand(time(0));
    for (int i = 0; i < SIZE; i++)
        arr[i] = rand() % 100 + 1;

    cout << "Arreglo original:\n";
    for (int i = 0; i < SIZE; i++)
        cout << arr[i] << " ";
    cout << endl;

    bubbleSort(arr, SIZE);

    cout << "\nArreglo ordenado:\n";
    for (int i = 0; i < SIZE; i++)
        cout << arr[i] << " ";
    cout << endl;

    return 0;
}