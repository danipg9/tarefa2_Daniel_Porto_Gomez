from faker import Faker
import random


def main():
    usuarios = crear_usuarios()
    mostrar_usuarios(usuarios)


# Función para crear usuarios
def crear_usuarios(n=15, locale='es_ES'):
    faker = Faker(locale)
    usuarios = {}
    for codigo in range(1, n + 1):
        usuarios[codigo] = {
            'nome': faker.name(),
            'direccion': faker.address().replace('\n', ', '),
            'correo': faker.email(),
            'telefono': faker.phone_number()
        }
    return usuarios


# Función para crear usuarios
def mostrar_usuarios(usuarios):
    for codigo, datos in usuarios.items():
        print(f"ID {codigo}:")
        print(f"  Nome: {datos['nome']}")
        print(f"  Dirección: {datos['direccion']}")
        print(f"  Correo electrónico: {datos['correo']}")
        print(f"  Teléfono: {datos['telefono']}")
        print()


if __name__ == '__main__':
    main()
