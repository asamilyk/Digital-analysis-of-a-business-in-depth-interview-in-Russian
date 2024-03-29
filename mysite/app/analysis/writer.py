from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
import itertools
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('Times-Roman', 'arial.ttf'))
w, h = A4
c = Canvas("../../../canvas.pdf", pagesize=A4)


def createPDF(b, d, total):
    text = c.beginText(w / 2 - 140, h - 40)
    text.setFont("Times-Roman", 20)
    text.textLine("Результаты анализа интервью")
    c.drawText(text)

    c.setFont("Times-Roman", 12)
    c.line(0, h - 50, w, h - 50)

    text = c.beginText(20, h - 70)
    text.setFont("Times-Roman", 15)
    text.textLine("Анализ частей речи")
    c.drawText(text)

    text = c.beginText(20, h - 90)
    text.setFont("Times-Roman", 12)
    text.textLine("Общее количество слов: " + str(total))
    c.drawText(text)
    a = ["Часть речи", 'Наречие', 'Предлог',
         'Лич. мест.', 'Глагол', 'Союз', 'Прил.', 'Сущ.']
    createGrid(a, b, d)
    c.line(0, h - 200, w, h - 200)
    c.showPage()
    c.save()
    return c


def createGrid(a, b, d):
    # Margin.
    x_offset = 70
    y_offset = 50
    # Space between rows.
    padding = 30
    xlist = [20 + x*x_offset for x in range(9)]
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
