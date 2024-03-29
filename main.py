import poem
import Text as t
import writer



text = poem.TEXT
t.tokenize(text)
print(t.tokenized_text)
t.general_statistics()
print(t.part_of_speech_stat_num)
print(t.part_of_speech_stat_per)
writer.createPDF(['Кол-во']+t.part_of_speech_stat_num, ['% от общ.']+t.part_of_speech_stat_per, t.total)







