class Song:
    count = 0
    genres = []
    genre_count = dict()
    artists = []
    artist_count = dict()

    def __init__(self, name, artist, genre):
        Song.add_song_to_count()
        self.name = name
        self.artist = artist
        self.genre = genre
        
        Song.add_to_genres(genre)
        Song.add_to_genre_count()
        Song.add_to_artists(artist)
        Song.add_to_artist_count()
    
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod 
    def add_to_genres(cls, genre):
        cls.genres.append(genre)
    
    @classmethod
    def add_to_artists(cls, artist):
        cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls):
        for genre in cls.genres:
            cls.genre_count[genre] = 0 # set to zero

        for genre in cls.genres:
            cls.genre_count[genre] += 1

    @classmethod
    def add_to_artist_count(cls):
        for artist in cls.artists:
            cls.artist_count[artist] = 0 # set to zero

        for artist in cls.artists:
            cls.artist_count[artist] += 1