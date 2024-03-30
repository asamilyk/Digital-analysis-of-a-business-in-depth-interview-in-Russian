from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
import itertools
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('Arial', 'ArialRegular.ttf'))
pdfmetrics.registerFont(TTFont('ArialBold', 'ArialBold.ttf'))
w, h = A4


def createPDF(c, b, d, total):
    write_line(c, w / 2 - 140, h - 40, 20, "Результаты анализа интервью", 'Arial')
    c.setFont("Arial", 12)
    c.line(0, h - 50, w, h - 50)
    write_line(c, w / 2 - 90, h - 70, 15, "Анализ частей речи", 'ArialBold')
    write_line(c, 20, h - 90, 12, "Общее количество слов: " + str(total), 'Arial')
    a = ["Часть речи", 'Наречие', 'Предлог',
         'Лич. мест.', 'Глагол', 'Союз', 'Прил.', 'Сущ.']
    createGrid(a, b, d, c)
    c.line(0, h - 200, w, h - 200)
    write_line(c, w / 2 - 80, h - 220, 15, "Метапрограммы", 'ArialBold')
    write_line(c, 20, h - 240, 12, "Внутренняя – внешняя референция", 'Arial')



    return c


def write_line(c, x, y, size, phrase, font):
    text = c.beginText(x, y)
    text.setFont(font, size)
    text.textLine(phrase)
    c.drawText(text)



def createGrid(a, b, d, c):
    # Margin.
    x_offset = 70
    y_offset = 50
    # Space between rows.
    padding = 30
    xlist = [20 + x * x_offset for x in range(9)]
    ylist = [h - 50 - y_offset - i * padding for i in range(4)]

    for rows in grouper([a, b, d], 3):
        rows = tuple(filter(bool, rows))
        c.grid(xlist, ylist[:len(rows) + 1])
        for y, row in zip(ylist[:-1], rows):
            for x, cell in zip(xlist, row):
                c.drawString(x + 2, y - padding + 3, str(cell))


def grouper(iterable, n):
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args)
