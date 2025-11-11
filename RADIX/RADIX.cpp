#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// Función para obtener el máximo valor del array
int getMax(vector<int>& arr) {
    return *max_element(arr.begin(), arr.end());
}

// Counting Sort para un dígito específico (exp)
void countingSort(vector<int>& arr, int exp) {
    int n = arr.size();
    vector<int> output(n);
    vector<int> count(10, 0);
    
    // Contar la frecuencia de cada dígito
    for (int i = 0; i < n; i++) {
        int index = (arr[i] / exp) % 10;
        count[index]++;
    }
    
    // Cambiar count[i] para que contenga la posición actual
    for (int i = 1; i < 10; i++) {
        count[i] += count[i - 1];
    }
    
    // Construir el array de salida
    for (int i = n - 1; i >= 0; i--) {
        int index = (arr[i] / exp) % 10;
        output[count[index] - 1] = arr[i];
        count[index]--;
    }
    
    // Copiar el array de salida al array original
    for (int i = 0; i < n; i++) {
        arr[i] = output[i];
    }
}

// Función principal de Radix Sort
void radixSort(vector<int>& arr) {
    int max_num = getMax(arr);
    
    // Aplicar counting sort para cada dígito
    for (int exp = 1; max_num / exp > 0; exp *= 10) {
        countingSort(arr, exp);
    }
}

// Ejemplo de uso
int main() {
    vector<int> arr = {170, 45, 75, 90, 2, 802, 24, 66};
    
    cout << "Array original: ";
    for (int num : arr) {
        cout << num << " ";
    }
    cout << endl;
    
    radixSort(arr);
    
    cout << "Array ordenado: ";
    for (int num : arr) {
        cout << num << " ";
    }
    cout << endl;
    
    return 0;
}