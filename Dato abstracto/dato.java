import java.util.ArrayList;

class Persona {
    private String nombre;
    private String apellido1;
    private String apellido2;

    public Persona(String nombre, String apellido1, String apellido2) {
        this.nombre = nombre;
        this.apellido1 = apellido1;
        this.apellido2 = apellido2;
    }

    public String getNombreCompleto() {
        return nombre + " " + apellido1 + " " + apellido2;
    }
}

public class Main {
    public static void main(String[] args) {
        ArrayList<Persona> personas = new ArrayList<>();
        personas.add(new Persona("Emily", "sandoval", "Ramírez"));
        personas.add(new Persona("Carlos", "Ramírez", "Torres"));

        for (Persona persona : personas) {
            System.out.println(persona.getNombreCompleto());
        }
    }
}
