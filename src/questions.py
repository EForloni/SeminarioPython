import random
# Preguntas para el juego
questions = [ "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
        "// Esto es un comentario",
        "/* Esto es un comentario */",
        "-- Esto es un comentario",
        "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

questions_to_ask = random.sample(list(zip(questions, answers, correct_answers_index)), k=3)

# El usuario deberá contestar 3 preguntas

score = 0

for question, answers, correct_index in questions_to_ask:
    # Se muestra la pregunta y las respuestas posibles
    print(question)
    for i, answer in enumerate(answers):
        print(f"{i + 1}. {answer}")

    # El usuario tiene 2 intentos para responder correctamente

    for intento in range(2):
        user_answer = (input("Respuesta: ")) 

        # Validamos que sea un número
        if not user_answer.isdigit():
            print("Respuesta no válida")
            exit(1) 

        user_answer = int(user_answer)-1

        # Verificamos si el número está dentro del rango válido
        if user_answer < 0 or user_answer >= len(answers):
            print("Respuesta no válida")
            exit(1)

        # Se verifica si la respuesta es correcta
        if user_answer == correct_index:
            print("¡Correcto!")
            score += 1
            break
    else:
            # Si el usuario no responde correctamente después de 2 intentos,
            # se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es:")
        score -= 0.5
        print(answers[correct_index])
    # Se imprime un blanco al final de la pregunta
print(f"Su resultado es: {score}")