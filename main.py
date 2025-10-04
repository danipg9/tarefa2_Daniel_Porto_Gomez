from faker import Faker
import random


if __name__ == '__main__':
    main()


def main():
    usuarios = crear_usuarios()

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

