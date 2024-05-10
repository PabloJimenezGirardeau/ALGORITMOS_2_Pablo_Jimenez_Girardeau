from datetime import date
from typing import List
from genre import GENRE

class Song:
    """Constructor de la clase Song."""

    def __init__(self, song_id: int, name: str, artist: str, duration: int, release_date: date, genres: List[GENRE]):
        if not isinstance(song_id, int) or song_id <= 0:
            raise ValueError("El ID de la canción debe ser un entero positivo.")
        
        if not name or not isinstance(name, str):
            raise ValueError("El nombre debe ser un string no vacío.")
        
        if not artist or not isinstance(artist, str):
            raise ValueError("El artista debe ser un string no vacío.")
        
        if not isinstance(duration, int) or duration <= 10:
            raise ValueError("La duración debe ser un entero mayor a 10 segundos.")
        
        if not isinstance(release_date, date) or release_date > date.today():
            raise ValueError("La fecha de lanzamiento no puede ser una fecha futura.")
        
        if not isinstance(genres, list) or any(not isinstance(genre, GENRE) for genre in genres):
            raise ValueError("Los géneros deben ser una lista de valores del enumerado GENRE.")
        
        self._id = song_id
        self._name = name
        self._artist = artist
        self._duration = duration
        self._release_date = release_date
        self._genres = list(dict.fromkeys(genres))  # Eliminar duplicados manteniendo el orden

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_artist(self):
        return self._artist

    def get_duration(self):
        return self._duration

    def get_release_date(self):
        return self._release_date

    def get_genres(self):
        return self._genres

    def add_genre(self, genre: GENRE):
        if genre not in self._genres:
            self._genres.append(genre)

    def __eq__(self, other):
        if not isinstance(other, Song):
            return False
        return self._id == other._id

    def __str__(self):
        return f"{self._artist} tocando {self._name} durante {self._duration} segundos."

