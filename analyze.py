from nltk.corpus import stopwords
from scraper import strip_punctuation
from os import listdir

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
    return sum([value for key, value in unigram_count.items()])/len(unigram_count)

for file in listdir("lyrics/eurodance"):
    print("{}: {}".format(file[:-4], get_average_word_rep("lyrics/eurodance/{}".format(file))))
