meme_dict = {
    "CRINGE": "Algo raro o embarazoso",
    "LOL": "Una respuesta a algo gracioso",
    "ROFL": "Una respuesta a una broma",
    "SHEESH": "Ligera desaprobación",
    "CREEPY": "Algo aterrador o siniestro",
    "AGGRO": "Ponerse agresivo o enojado",
    "GOAT": "Persona considerada la mejor en algo",
    "NPC": "Persona que parece actuar de forma automática",
    "SUS": "Algo o alguien sospechoso"
}

print("¡BIENVENIDO AL DICCIONARIO MODERNO!")
print("Escribe una palabra en MAYÚSCULAS.")

for i in range(5):
    word = input("Escribe una palabra: ")

    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("¡Todavía no conozco esa palabra!")
