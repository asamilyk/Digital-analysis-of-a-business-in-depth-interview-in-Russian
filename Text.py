import re
from nltk.corpus import stopwords



class Text:
    text = ""
    tokenized_text = []

    def __init__(self, text):
        self.text = text

    def tokenize(self):
        # replacing non-letters with nothing
        t = re.sub(r'[^\w\s]', '', self.text)
        # conversion to lowercase
        t = t.lower().split()
        self.tokenized_text = t

    def deleteStopWords(self):
        stop_words = set(stopwords.words('russian'))
        print(stop_words)




