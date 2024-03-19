from reportlab.pdfbase import pdfmetrics
import itertools
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4

pdfmetrics.registerFont(TTFont('Arial', 'ArialRegular.ttf'))
pdfmetrics.registerFont(TTFont('ArialBold', 'ArialBold.ttf'))
w, h = A4


class Writer:
    canvas = Canvas
    total = 0


    def __init__(self, canvas):
        self.canvas = canvas

    def create_pdf(self, b, c, total):
        self.total = total
        self.write_line(w / 2 - 140, h - 40, 20, "Результаты анализа интервью", 'Arial')
        self.canvas.setFont("Arial", 12)
        self.canvas.line(0, h - 50, w, h - 50)
        self.write_line(w / 2 - 90, h - 70, 15, "Анализ частей речи", 'ArialBold')
        self.write_line(20, h - 90, 12, "Общее количество слов: " + str(total), 'ArialBold')
        a = ["Часть речи", 'Наречие', 'Предлог',
             'Лич. мест.', 'Глагол', 'Союз', 'Прил.', 'Сущ.']
        self.create_grid_for_gen(a, b, c)
        self.canvas.line(0, h - 200, w, h - 200)
        self.write_line(w / 2 - 80, h - 220, 15, "Метапрограммы", 'ArialBold')

        data = [[1, 2, 3], [1, 2, 3]]

    def write_line(self, x, y, size, phrase, font):
        text = self.canvas.beginText(x, y)
        text.setFont(font, size)
        text.textLine(phrase)
        self.canvas.drawText(text)

    def create_grid_for_gen(self, a, b, d):
        # Margin.
        x_offset = 70
        y_offset = 50
        # Space between rows.
        padding = 30
        x_list = [20 + x * x_offset for x in range(9)]
        y_list = [h - 50 - y_offset - i * padding for i in range(4)]

        for rows in self.grouper([a, b, d], 3):
            rows = tuple(filter(bool, rows))
            self.canvas.grid(x_list, y_list[:len(rows) + 1])
            for y, row in zip(y_list[:-1], rows):
                for x, cell in zip(x_list, row):
                    self.canvas.drawString(x + 2, y - padding + 3, str(cell))

    def grouper(self, iterable, n):
        args = [iter(iterable)] * n
        return itertools.zip_longest(*args)

    def create_grid_for_in_ex(self, a, b, c):
        y_offset = 50
        padding = 30
        x_list = [20, 230, 300]
        y_list = [h - 200 - y_offset - i * padding for i in range(4)]

        for rows in self.grouper([a, b, c], 3):
            rows = tuple(filter(bool, rows))
            self.canvas.grid(x_list, y_list[:len(rows) + 1])
            for y, row in zip(y_list[:-1], rows):
                for x, cell in zip(x_list, row):
                    self.canvas.drawString(x + 2, y - padding + 3, str(cell))

    def in_ex_reference(self, pron, first_verbs):
        self.write_line(20, h - 240, 12, "Внутренняя – внешняя референция", 'ArialBold')
        a = ["Количество местоимений в 1 л. ед.ч.", pron if pron < 10 ** 10 else ">10^10"]
        b = ["Количество глаголов в 1 л. ед.ч.", len(first_verbs) if len(first_verbs) < 10 ** 10 else ">10^10"]
        total = self.total if self.total > 0 else 1
        c = ["Количество таких слов в тексте (%)", str(round(float(pron + len(first_verbs)) * 100 / total, 1)) + "%"]
        self.create_grid_for_in_ex(a, b, c)

    def create_grid_for_as_av(self, a, b):
        y_offset = 50
        padding = 30
        x_list = [20, 270, 340]
        y_list = [h - 340 - y_offset - i * padding for i in range(3)]

        for rows in self.grouper([a, b], 2):
            rows = tuple(filter(bool, rows))
            self.canvas.grid(x_list, y_list[:len(rows) + 1])
            for y, row in zip(y_list[:-1], rows):
                for x, cell in zip(x_list, row):
                    self.canvas.drawString(x + 2, y - padding + 3, str(cell))

    def as_av_reference(self, neg_words):
        self.write_line(20, h - 380, 12, "Стремление – избегание", 'ArialBold')
        a = ["Количество слов, выражающих отрицание", neg_words if neg_words < 10 ** 10 else ">10^10"]
        total = self.total if self.total > 0 else 1
        b = ["Количество таких слов в тексте (%)", str(round(float(neg_words) * 100 / total, 1)) + "%"]
        self.create_grid_for_as_av(a, b)

    def create_grid_for_ac_re(self, a, b, c):
        y_offset = 50
        padding = 30
        x_list = [20, 230, 300]
        y_list = [h - 450 - y_offset - i * padding for i in range(4)]

        for rows in self.grouper([a, b, c], 3):
            rows = tuple(filter(bool, rows))
            self.canvas.grid(x_list, y_list[:len(rows) + 1])
            for y, row in zip(y_list[:-1], rows):
                for x, cell in zip(x_list, row):
                    self.canvas.drawString(x + 2, y - padding + 3, str(cell))

    def ac_re_reference(self, min_len, max_len, avr_len):
        self.write_line(20, h - 495, 12, "Активность рефлексивность", 'ArialBold')
        a = ["Минимальная длина слова", str(min_len) + " зн." if min_len < 10 ** 10 else ">10^10 зн."]
        b = ["Максимальная длина слова", str(max_len) + " зн." if max_len < 10 ** 10 else ">10^10 зн."]
        c = ["Средняя длина слова", str(round(avr_len, 1)) + " зн."]
        self.create_grid_for_ac_re(a, b, c)

    def create_grid_for_re_pr(self, a, b, c):
        y_offset = 50
        padding = 30
        x_list = [20, 230, 300, 450]
        y_list = [h - 590 - y_offset - i * padding for i in range(4)]

        for rows in self.grouper([a, b, c], 3):
            rows = tuple(filter(bool, rows))
            self.canvas.grid(x_list, y_list[:len(rows) + 1])
            for y, row in zip(y_list[:-1], rows):
                for x, cell in zip(x_list, row):
                    self.canvas.drawString(x + 2, y - padding + 3, str(cell))

    def re_pr_reference(self, perf, imp):
        self.write_line(20, h - 630, 12, "Нацеленность на результат - на процесс", 'ArialBold')
        a = ["", "Количество", "% от всех глаголов текста"]
        total = perf + imp if perf + imp > 0 else 1
        b = ["Глаголы в совершенном виде", str(perf) if perf < 10 ** 10 else ">10^10",
             str(round(float(perf) * 100 / total, 1)) + "%"]
        c = ["Глаголы в несовершенном виде", str(imp) if imp < 10 ** 10 else ">10^10",
             str(round(float(imp) * 100 / total, 1)) + "%"]
        self.create_grid_for_re_pr(a, b, c)
