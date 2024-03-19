import re
import nltk
from collections import Counter
import pymorphy2
#import writer as _writer
from app.analysis import writer as _writer

try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('taggers/averaged_perceptron_tagger_ru')
except LookupError:
    print("hh")
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger_ru')

morph = pymorphy2.MorphAnalyzer()


class Text:
    pos_counts = {}
    tokenized_text = []
    pos_tags = {}
    writer = _writer.Writer
    tokens = []

    def __init__(self, writer):
        self.writer = writer

    def tokenize(self, text):
        # replacing non-letters with nothing
        t = re.sub(r'[^\w\s]', '', text)
        # conversion to lowercase
        t = t.lower().split()
        self.tokenized_text = t

    def general_statistics(self):
        part_of_speech_stat_num = []
        part_of_speech_stat_per = []
        self.get_pos_tags()
        self.pos_counts = Counter(tag for word, tag in self.pos_tags)
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
            part_of_speech_stat_num.append(count if count <= 10 ** 10 else ">10^10")
            part_of_speech_stat_per.append(str(round(float(count) * 100 / total, 1)) + "%")
        self.writer.create_pdf(['Кол-во'] + part_of_speech_stat_num, ['% от общ.'] + part_of_speech_stat_per, tot)

    def get_pos_tags(self):
        self.tokens = nltk.word_tokenize(" ".join(self.tokenized_text), language='russian')
        self.pos_tags = nltk.pos_tag(self.tokens, lang='rus')

    def in_ex_reference(self):
        c = Counter(self.tokenized_text)
        pronouns = sum(c[x] for x in ("я", "меня", "мне", "мной", "мой", "мне", "мое", "я сам"))
        singular_first_person_verbs = [word for word in self.tokens if self.is_singular_1st_person_verb(word)]
        self.writer.in_ex_reference(pronouns, singular_first_person_verbs)

    def is_singular_1st_person_verb(self, word):
        parsed_word = morph.parse(word)[0]
        return parsed_word.tag.POS == 'VERB' and 'sing' in parsed_word.tag and '1per' in parsed_word.tag

    def as_av_reference(self):
        neg_words = self.count_negation_words()
        self.writer.as_av_reference(neg_words)

    def count_negation_words(self):
        negation_words = ['не', 'никогда', 'никак', 'нет', 'ничего', 'никакой', 'никакая', 'никакие', 'никаких',
                          'никуда', 'негде', 'ниоткуда', 'никаков', 'некогда', 'некуда']
        pattern = r'\b(?:{})\b'.format('|'.join(negation_words))
        matches = re.findall(pattern, " ".join(self.tokenized_text))
        return len(matches)

    def ac_re_reference(self):
        if len(self.tokenized_text) == 0:
            min_len = 0
            max_len = 0
            avr_len = 0
        else:
            sorted_words = sorted(self.tokenized_text, key=lambda x: len(x))
            min_len = len(sorted_words[0])
            max_len = len(sorted_words[len(sorted_words)-1])
            avr_len = sum([len(word) for word in self.tokenized_text]) / len(self.tokenized_text)
        self.writer.ac_re_reference(min_len, max_len, avr_len)

    def re_pr_reference(self):
        perf_verbs = 0
        imp_verbs = 0
        for token in self.tokenized_text:
            parsed_word = morph.parse(token)[0]
            if 'VERB' in parsed_word.tag:
                if 'perf' in parsed_word.tag:
                    perf_verbs += 1
                elif 'impf' in parsed_word.tag:
                    imp_verbs += 1

        self.writer.re_pr_reference(perf_verbs, imp_verbs)
