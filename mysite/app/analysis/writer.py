from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
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
        self.write_line(20, h - 90, 12, "Общее количество слов: " + str(total), 'Arial')
        a = ["Часть речи", 'Наречие', 'Предлог',
             'Лич. мест.', 'Глагол', 'Союз', 'Прил.', 'Сущ.']
        self.create_grid_for_gen(a, b, c)
        self.canvas.line(0, h - 200, w, h - 200)
        self.write_line(w / 2 - 80, h - 220, 15, "Метапрограммы", 'ArialBold')
        return c

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
        xlist = [20 + x * x_offset for x in range(9)]
        ylist = [h - 50 - y_offset - i * padding for i in range(4)]

        for rows in self.grouper([a, b, d], 3):
            rows = tuple(filter(bool, rows))
            self.canvas.grid(xlist, ylist[:len(rows) + 1])
            for y, row in zip(ylist[:-1], rows):
                for x, cell in zip(xlist, row):
                    self.canvas.drawString(x + 2, y - padding + 3, str(cell))

    def grouper(self, iterable, n):
        args = [iter(iterable)] * n
        return itertools.zip_longest(*args)

    def create_grid_for_in_ex(self, a, b, c):
        # Margin.
        x_offset = 140
        y_offset = 50
        # Space between rows.
        padding = 30
        xlist = [20, 230, 300]
        ylist = [h - 210 - y_offset - i * padding for i in range(4)]

        for rows in self.grouper([a, b, c], 3):
            rows = tuple(filter(bool, rows))
            self.canvas.grid(xlist, ylist[:len(rows) + 1])
            for y, row in zip(ylist[:-1], rows):
                for x, cell in zip(xlist, row):
                    self.canvas.drawString(x + 2, y - padding + 3, str(cell))

    def in_ex_reference(self, pron, first_verbs):
        self.write_line(20, h - 240, 12, "Внутренняя – внешняя референция", 'Arial')
        a = ["Количество местоимений в 1 л. ед.ч.", pron if pron < 10 ** 10 else ">10^10"]
        b = ["Количество глаголов в 1 л. ед.ч.", len(first_verbs) if len(first_verbs) < 10 ** 10 else ">10^10"]
        total = self.total if self.total > 0 else 1
        c = ["Количество таких слов в тексте (%)", str(round(float(pron+len(first_verbs)) * 100 / total, 1)) + "%"]
        self.create_grid_for_in_ex(a, b, c)
