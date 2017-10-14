import requests, os
from bs4 import BeautifulSoup
from string import punctuation

BASE_URL = 'https://genius.com/'
test = True
console_output = False
file_output = True

def strip_punctuation(word):
    for ch in punctuation:
        word = word.replace(ch, '')
    return word

def get_song_lyrics(title, artist, genre):
    title = strip_punctuation(title)
    artist = strip_punctuation(artist)
    extension = "-".join(artist.split() + title.split())
    URL = (BASE_URL + extension + "-lyrics").lower()
    req = requests.get(URL)

    # If lyrics were found
    if req.status_code == 200:
        soup = BeautifulSoup(req.text, "lxml")
        lyrics = soup.find_all("div", class_="lyrics")[0].get_text().strip()
        if console_output:
            print(lyrics)
        if file_output:
            if not os.path.exists("lyrics/{}".format(genre)):
                os.makedirs("lyrics/{}".format(genre))
            text_file = open("lyrics/" + genre + "/" + extension + ".txt", "w")
            text_file.write(lyrics)
            text_file.close()

        # Output to file
        # text_file = open("")

def test():
    get_song_lyrics("Everytime We Touch", "Cascada", "dance")
    get_song_lyrics("D.N.A.", "Kendrick Lamar", "rap")

if __name__ == '__main__':
    if test:
        test()
    pass
