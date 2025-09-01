#include <iostream>
#include <vector>
#include <string>

class Persona {
private:
    std::string nombre;
    std::string apellido1;
    std::string apellido2;

public:
    Persona(std::string n, std::string a1, std::string a2)
        : nombre(n), apellido1(a1), apellido2(a2) {}

    std::string getNombreCompleto() const {
        return nombre + " " + apellido1 + " " + apellido2;
    }
};

int main() {
    std::vector<Persona> personas;
    personas.push_back(Persona("Emily", "sandoval", "Ramírez"));
    personas.push_back(Persona("Carlos", "Ramírez", "Torres"));

    for (const auto& persona : personas) {
        std::cout << persona.getNombreCompleto() << std::endl;
    }

    return 0;
}
