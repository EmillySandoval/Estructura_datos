#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

void insertionSort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;

    
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;  
        }
        arr[j + 1] = key;
    }
}

int main() {
    srand(time(0));
    const int n = 10;
    int arr[n];

    cout << "Antes de ordenar: ";
    for (int i = 0; i < n; i++) {
        arr[i] = rand() % 100 + 1;
        cout << arr[i] << " ";
    }
    cout << endl;

    insertionSort(arr, n);

    cout << "Después de ordenar: ";
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;

    return 0;
}