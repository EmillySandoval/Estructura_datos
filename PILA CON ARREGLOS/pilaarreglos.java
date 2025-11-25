public class Pila {
    private static final int TAMANIO_MAXIMO = 100;
    private int[] pila;
    private int tope;
    
    public Pila() {
        pila = new int[TAMANIO_MAXIMO];
        tope = -1;
    }
    
    public void apilar(int numero) {
        if (tope == TAMANIO_MAXIMO - 1) {
            System.out.println("Desbordamiento de Pila");
            return;
        }
        pila[++tope] = numero;
    }
    
    public int desapilar() {
        if (tope == -1) {
            System.out.println("Subdesbordamiento de Pila");
            return -1;
        }
        return pila[tope--];
    }
    
    public int mirar() {
        if (tope == -1) {
            System.out.println("La pila está vacía");
            return -1;
        }
        return pila[tope];
    }
    
    public boolean estaVacia() {
        return tope == -1;
    }
    
    public boolean estaLlena() {
        return tope == TAMANIO_MAXIMO - 1;
    }
    
    public static void main(String[] args) {
        Pila p = new Pila();
        p.apilar(10);
        p.apilar(20);
        p.apilar(30);
        
        System.out.println("Elemento Superior: " + p.mirar());
        System.out.println("Extrae elemento: " + p.desapilar());
        System.out.println("Elemento Superior: " + p.mirar());
    }
}