using System;
using System.Collections.Generic;

public class Persona {
    public string Nombre { get; set; }
    public string Apellido1 { get; set; }
    public string Apellido2 { get; set; }

    public Persona(string nombre, string apellido1, string apellido2) {
        Nombre = nombre;
        Apellido1 = apellido1;
        Apellido2 = apellido2;
    }

    public string NombreCompleto() {
        return $"{Nombre} {Apellido1} {Apellido2}";
    }
}

class Program {
    static void Main() {
        List<Persona> personas = new List<Persona> {
            new Persona("Emily", "sandoval", "Ramírez"),
            new Persona("Carlos", "Ramírez", "Torres")
        };

        foreach (var persona in personas) {
            Console.WriteLine(persona.NombreCompleto());
        }
    }
}