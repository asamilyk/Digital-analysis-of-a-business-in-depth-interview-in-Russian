import re


class Text:
    text = ""


    def __init__(self, text):
        self.test = self.tokenization(text)

    # Division into words
    def tokenization(self, text):
        # replacing non-letters with nothing
        t = re.sub(r'[^\w\s]', '', text)
        # conversion to lowercase
        t = t.lower()
        return t


