from scraper import get_song_lyrics

eurodance = [
    ("All I Ever Wanted", "Basshunter"),
    ("Blue (Da Ba Dee)", "Eiffel 65"),
    ("What is Love", "Haddaway"),
    ("Everytime We Touch", "Cascada"),
    ("Around the World (La la la la la)", "ATC"),
    ("Better Off Alone", "Alice Deejay"),
    ("Odysee", "Scarf!")
]

for song in eurodance:
    get_song_lyrics(song[0], song[1], "eurodance")
