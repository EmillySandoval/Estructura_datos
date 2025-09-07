class Main {
    public static int buscar(int[] arreglo, int objetivo) {
        for (int i = 0; i < arreglo.length; i++) {
            if (arreglo[i] == objetivo) {
                return i;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] datos = {3, 8, 1, 5, 9};
        int elementoBuscado = 5;

        int resultado = buscar(datos, elementoBuscado);

        if (resultado != -1) {
            System.out.println("Elemento encontrado en la posición: " + resultado);
        } else {
            System.out.println("Elemento no encontrado en el arreglo.");
        }
    }
}