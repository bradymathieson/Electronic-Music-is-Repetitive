from nltk.corpus import stopwords
from scraper import strip_punctuation
from os import listdir
import matplotlib.pyplot as plt

stop_words = set(stopwords.words('english'))

def get_average_word_rep(path):
    o = open(path, "r")
    unigram_count = dict()

    for line in o.readlines():
        if line[0] != '[':
            for word in line.lower().strip().split():
                word = strip_punctuation(word)
                if word not in stop_words:
                    if word not in unigram_count:
                        unigram_count[word] = 0
                    unigram_count[word] += 1
    o.close()
    return sum([value for key, value in unigram_count.items()])/len(unigram_count), len(unigram_count)

def plot_genre(genre):
    length_axis = list()
    avg_rep_axis = list()
    for file in listdir("lyrics/{}".format(genre)):
        rep, length = get_average_word_rep("lyrics/{}/{}".format(genre,file))
        length_axis.append(length)
        avg_rep_axis.append(rep)
    plt.scatter(length_axis, avg_rep_axis, label='hello', color='k', s=25, marker="o")
    plt.show()

plot_genre("eurodance")
