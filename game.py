import random

# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo",
"inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)
# Número máximo de intentos permitidos
max_fallos = 10
# Lista para almacenar las letras adivinadas
guessed_letters = []
# contador de fallos
fallos = 0
# para armar la palabra segun la dificultad
palabra = []

print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")

# Solicitar al usuario que elija la dificultad
print("banca primero elegi la dificultad")
while True:
    dificultad = input("Ingrese qué dificultad desea: facil, medio o dificil: ").lower()
    if dificultad in ["facil", "medio", "dificil"]:
        print(f"Has elegido la dificultad {dificultad}.")
        if dificultad == "facil":
            for letter in secret_word:
                if letter in "aeioóu":
                    palabra.append(letter)
                else:
                    palabra.append("_")
            guessed_letters = ["a", "e", "i", "o", "ó", "u"]
            word_displayed = "".join(palabra)
        elif dificultad == "medio":
            word_displayed = secret_word[0] + "_" * (len(secret_word) - 2) + secret_word[-1]
        else:
            word_displayed = "_" * len(secret_word)
        break
    else:
        print("no coincide con ninguna de las opciones que le dimos por favor vuelva a intentar")

# Mostrarla palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")

while fallos < max_fallos:
    # Pedir al jugador que ingrese una letrap
    letter = input("Ingresa una letra: ").lower()

    # punto 7 solucion de bug de string vacio
    if letter == "":
        print("Valor invalido, ingrese una letra ;)")
        fallos +=1
        continue

    # Verificar si la letra ya ha sido adivinada

    if letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
        fallos +=1
        continue

    # Agregar la letra a la lista de letras adivinadas
    guessed_letters.append(letter)

    # Verificar si la letra está en la palabra secreta
    if letter in secret_word:
        print("¡Bien hecho! La letra está en la palabra.")
    else:
        print("Lo siento, la letra no está en la palabra.")
        fallos += 1

    # Mostrar la palabra parcialmente adivinada
    letters = []
    for letter in secret_word:
        if letter in guessed_letters:
            letters.append(letter)
        else:
            letters.append("_")
    if dificultad == "medio":
        letters.pop(0)
        letters.pop(-1)
        letters.insert(0, secret_word[0])
        letters.append(secret_word[-1])
    word_displayed = "".join(letters)
    print(f"Palabra: {word_displayed}")
    # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
        if fallos == 1:
            print("con un fallo")
        else:
            print(f"con {fallos} fallos")
        break
else:
        print(f"¡Oh no! Has fallado {max_fallos} veces.")
        print(f"La palabra secreta era: {secret_word}")
