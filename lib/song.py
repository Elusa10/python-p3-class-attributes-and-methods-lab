class Song:
    count = 0
    genres = []
    genre_count = {}
    artists = set()
    artist_count = {}


    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        Song.artists.add(artist)
        self.genre = genre
        Song.count += 1

        if genre not in Song.genres:
            Song.genres.append(genre)

        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1 

        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1      

print(Song.count)