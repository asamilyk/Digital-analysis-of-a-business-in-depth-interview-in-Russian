import app.analysis.text as t
from app.analysis import writer
from app.analysis.reader import read


def analyse(file):
    text = read(file)
    t.tokenize(text)
    print(t.tokenized_text)
    t.general_statistics()
    print(t.part_of_speech_stat_num)
    print(t.part_of_speech_stat_per)
    return writer.createPDF(['Кол-во'] + t.part_of_speech_stat_num, ['% от общ.'] + t.part_of_speech_stat_per, t.total)
