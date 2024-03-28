import re
import nltk
from nltk.corpus import stopwords
from collections import Counter


# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger_ru')


class Text:
    text = ""
    tokenized_text = []
    part_of_speech_stat_num = {}
    part_of_speech_stat_per = {}

    def __init__(self, text):
        self.text = text

    def tokenize(self):
        # replacing non-letters with nothing
        t = re.sub(r'[^\w\s]', '', self.text)
        # conversion to lowercase
        t = t.lower().split()
        self.tokenized_text = t

    def generalStatistics(self):
        pos_tags = self.get_pos_tags()
        pos_counts = Counter(tag for word, tag in pos_tags)
        print("Количество частей речи в тексте:")
        tags = {'Наречие': "ADV",
                'Предлог': "PR",
                'Прилагательное в женском роде': "A=f",
                'Прилагательное в мужском роде': "A=m",
                'Прилагательное в среднем роде': "A=n",
                'Прилагательное во множественном числе роде': "A=pl",
                'Личные местоимения': "S-PRO",
                'Глаголы': "V",
                'Союзы': "CONJ",
                'Притяжательное прилательное м.р.': "A-PRO=m",
                'Притяжательное прилательное ж.р.': "A-PRO=f",
                'Притяжательное прилательное ср.р.': "A-PRO=n",
                'Притяжательное прилательное мн.ч.': "A-PRO=pl",
                'Наречие-местоимение': "ADV-PRO",
                'Числительное м.р.': "NUM=m",
                'Числительное и.п.': "NUM=nom",
                'Прилагательное': "A",
                'Вводное': "PARENTH"}
        total = sum(pos_counts.values())
        for key in tags.keys():
            count = pos_counts[tags[key]]
            self.part_of_speech_stat_num[key] = count
            self.part_of_speech_stat_per[key] = float(count) * 100 / total
        self.part_of_speech_stat_num = dict(
            sorted(self.part_of_speech_stat_num.items(), key=lambda item: item[1], reverse=True))
        self.part_of_speech_stat_per = dict(
            sorted(self.part_of_speech_stat_per.items(), key=lambda item: item[1], reverse=True))

    def get_pos_tags(self):
        tokens = nltk.word_tokenize(" ".join(self.tokenized_text), language='russian')
        pos_tags = nltk.pos_tag(tokens, lang='rus')
        return pos_tags

    def deleteStopWords(self):
        stop_words = set(stopwords.words('russian'))
        print(stop_words)
