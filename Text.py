import re
import nltk
from nltk.corpus import stopwords
from collections import Counter


# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger_ru')


class Text:
    text = ""
    tokenized_text = []
    part_of_speech_stat_num = []
    part_of_speech_stat_per = []
    total = 0

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
        tags = {'Наречие': "ADV",
                'Предлог': "PR",
                'Прилагательное в женском роде': "A=f",
                'Прилагательное в мужском роде': "A=m",
                'Прилагательное в среднем роде': "A=n",
                'Прилагательное во множественном числе роде': "A=pl",
                'Личные местоимения': "S-PRO",
                'Глагол': "V",
                'Союз': "CONJ",
                'Притяжательное прилательное м.р.': "A-PRO=m",
                'Притяжательное прилательное ж.р.': "A-PRO=f",
                'Притяжательное прилательное ср.р.': "A-PRO=n",
                'Притяжательное прилательное мн.ч.': "A-PRO=pl",
                'Наречие-местоимение': "ADV-PRO",
                'Числительное м.р.': "NUM=m",
                'Числительное и.п.': "NUM=nom",
                'Прилагательное': "A",
                'Вводное': "PARENTH",
                'Существительное': "S"}
        main_tags = ['Наречие',
                     'Предлог',
                     'Личные местоимения',
                     'Глагол',
                     'Союз',
                     'Прилагательное',
                     'Существительное']
        self.total = sum(pos_counts.values())
        for key in main_tags:
            count = pos_counts[tags[key]]
            self.part_of_speech_stat_num.append(count if count < 10**10 else ">10^10")
            self.part_of_speech_stat_per.append(str(round(float(count) * 100 / self.total, 1)) +"%")

    def get_pos_tags(self):
        tokens = nltk.word_tokenize(" ".join(self.tokenized_text), language='russian')
        pos_tags = nltk.pos_tag(tokens, lang='rus')
        return pos_tags

    def deleteStopWords(self):
        stop_words = set(stopwords.words('russian'))
        print(stop_words)
