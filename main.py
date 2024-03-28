import poem
import Text


t = poem.TEXT
obj = Text.Text(t)
obj.tokenize()
print(obj.tokenized_text)
obj.generalStatistics()
print(obj.part_of_speech_stat_num)
print(obj.part_of_speech_stat_per)




