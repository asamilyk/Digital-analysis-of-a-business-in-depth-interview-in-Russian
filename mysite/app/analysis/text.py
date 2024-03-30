import re
import nltk
from nltk.corpus import stopwords
from collections import Counter

# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger_ru')
class Text:
    pos_counts = {}
    tokenized_text = []

    def tokenize(self, text):
        # replacing non-letters with nothing
        t = re.sub(r'[^\w\s]', '', text)
        # conversion to lowercase
        t = t.lower().split()
        self.tokenized_text = t


    def general_statistics(self):
        part_of_speech_stat_num = []
        part_of_speech_stat_per = []
        pos_tags = self.get_pos_tags()
        self.pos_counts = Counter(tag for word, tag in pos_tags)
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
        tot = sum(self.pos_counts.values())
        total = tot if tot > 0 else 1
        for key in main_tags:
            count = self.pos_counts[tags[key]]
            part_of_speech_stat_num.append(count if count < 10 ** 10 else ">10^10")
            part_of_speech_stat_per.append(str(round(float(count) * 100 / total, 1)) + "%")
        return part_of_speech_stat_num, part_of_speech_stat_per, tot


    def get_pos_tags(self):
        tokens = nltk.word_tokenize(" ".join(self.tokenized_text), language='russian')
        pos_tags = nltk.pos_tag(tokens, lang='rus')
        return pos_tags


    def in_ex_reference(self):
        c = Counter(self.tokenized_text)
        pronouns = sum(c[x] for x in ("я", "меня", "мне", "мной", "мой", "мне", "мое", "я сам"))
        print(self.pos_counts["V=fin=1p=sg"])


