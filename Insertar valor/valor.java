import java.util.*;

public class Main {
    public static void main(String[] args) {
        List<Integer> lista = new ArrayList<>(Arrays.asList(1, 2, 3, 5));
        lista.add(3, 4);
        System.out.println(lista); 
    }
}