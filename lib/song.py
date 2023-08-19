class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(self.genre)
        Song.add_to_artists(self.artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if not cls.genre_count.__contains__(genre):
            cls.genres.append(genre)
            cls.genre_count.update({genre : 1})
        else:
            cls.add_to_genre_count(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if not cls.artist_count.__contains__(artist):
            cls.artists.append(artist)
            cls.artist_count.update({artist : 1})
        else:
            cls.add_to_artist_count(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        cls.genre_count.update({genre : cls.genre_count.get(genre) + 1})

    @classmethod
    def add_to_artist_count(cls, artist):
        cls.artist_count.update({artist : cls.artist_count.get(artist) + 1})
    
