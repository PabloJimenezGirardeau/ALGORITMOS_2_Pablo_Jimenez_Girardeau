from datetime import date
from song import Song
from genre import GENRE

def main():
    """Función principal para probar la clase Song."""

    print("=================================================================.")
    print("Caso de Prueba 1: Crear una Canción.")
    print("=================================================================.")
    song = Song(1, "calorro", "estopa", 189, date.today(), [GENRE.POP])

    if song.get_id() == 1:
        print("Prueba PASADA. El parámetro id ha sido configurado correctamente.")
    else:
        print("Prueba FALLIDA. Verifica el método __init__().")

    if song.get_name() == "calorro":
        print("Prueba PASADA. El parámetro nombre ha sido configurado correctamente.")
    else:
        print("Prueba FALLIDA. Verifica el método __init__().")

    if song.get_artist() == "estopa":
        print("Prueba PASADA. El parámetro artista ha sido configurado correctamente.")
    else:
        print("Prueba FALLIDA. Verifica el método __init__().")

    if song.get_duration() == 189:
        print("Prueba PASADA. El parámetro duración ha sido configurado correctamente.")
    else:
        print("Prueba FALLIDA. Verifica el método __init__().")

    if song.get_release_date() == date.today():
        print("Prueba PASADA. El parámetro fecha de lanzamiento ha sido configurado correctamente.")
    else:
        print("Prueba FALLIDA. Verifica el método __init__().")

    if song.get_genres() == [GENRE.POP]:
        print("Prueba PASADA. El parámetro géneros ha sido configurado correctamente.")
    else:
        print("Prueba FALLIDA. Verifica el método __init__().")


    print("=================================================================.")
    print("Caso de Prueba 2: Formato legible de la canción.")
    print("=================================================================.")
    song2 = Song(2, "calorro", "estopa", 189, date.today(), [GENRE.POP])

    if str(song2) == "estopa tocando calorro durante 189 segundos.":
        print("Prueba PASADA. El formato legible de la canción ha sido implementado correctamente.")
        print(str(song2))
    else:
        print("Prueba FALLIDA. Verifica el método __str__()." + " RESULTADO: " + str(song2))


    print("=================================================================.")
    print("Caso de Prueba 3: Añadir género a la canción.")
    print("=================================================================.")
    song2.add_genre(GENRE.ROCK)
    genres = song2.get_genres()
    if genres == [GENRE.POP, GENRE.ROCK]:
        print("Prueba PASADA. El método add_genre(genre) ha sido implementado correctamente.")
    else:
        print("Prueba FALLIDA. Verifica el método add_genre(genre), "+ " RESULTADO: " + str(genres))
    
    print("=================================================================.")
    print("Caso de Prueba 4: Método __eq__.")
    print("=================================================================.")
    song3 = Song(2, "calorro", "estopa", 189, date.today(), [GENRE.POP])
    if song2 == song3:
        print("Prueba PASADA. El método __eq__ ha sido implementado correctamente.")
    else:
        print("Prueba FALLIDA. Verifica el método __eq__().")

if __name__ == "__main__":
    main()
