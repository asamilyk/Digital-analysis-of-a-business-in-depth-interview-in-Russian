import poem
import Text
import writer



t = poem.TEXT
obj = Text.Text(t)
obj.tokenize()
print(obj.tokenized_text)
obj.generalStatistics()
print(obj.part_of_speech_stat_num)
print(obj.part_of_speech_stat_per)
writer.createPDF(['Кол-во']+obj.part_of_speech_stat_num, ['% от общ.']+obj.part_of_speech_stat_per, obj.total)







