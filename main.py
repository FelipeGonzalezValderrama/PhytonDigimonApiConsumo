import requests

respuesta = requests.get("https://digimon-api.vercel.app/api/digimon")

lista = respuesta.json()

print("Primer Digimon: ")
print("----------------")
print("Nombre: " + lista[0]["name"])
print("Level: " + lista[0]["level"])

print("+")
print("Digimons Champions:")
print("------------------")
contador = 0
for digi in lista:
    if digi["level"] == "Champion":
        contador = contador + 1
        print("Nombre: " + digi["name"])
        if contador == 4:
            break

print("+")
print("Digimons Rookie:")
print("------------------")
contador = 0  # Contar max 4 digimons
indice = 0  # Para el recorrido
while indice < len(lista):
    if lista[indice]["level"] == "Rookie":
        print("Nombre: " + lista[indice]["name"])
        contador = contador + 1
        if contador == 4:
            break
    indice = indice + 1


def mostrar_imagen(ruta):
    import urllib.request
    urllib.request.urlretrieve(ruta, "icemon.jpg")
    import climage
    screen = climage.convert("icemon.jpg", is_unicode=True)
    print(screen)


print("+")
print("Filtrar al Digimon : Icemon")
print("------------------")
for digi in lista:
    if digi["name"] == "Icemon":
        print("Nombre: " + digi["name"])
        print("Level: " + digi["level"])
        mostrar_imagen(digi["img"])
        break
