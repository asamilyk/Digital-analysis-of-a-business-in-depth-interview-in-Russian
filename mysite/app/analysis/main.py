import os
import app.analysis.text as t
import scipy.io
from reportlab.pdfgen.canvas import Canvas
from app.analysis import writer
from reportlab.lib.pagesizes import A4


#import text as t
#import writer


def analyse(file):
    if os.path.exists("canvas.pdf"):
        os.remove("canvas.pdf")
    text = str(file).replace("\r", " ").replace('\n', ' ')
    tokenized_text = t.tokenize(text)
    print(tokenized_text)
    num, per, total = t.general_statistics(tokenized_text)
    c = Canvas("canvas.pdf", pagesize=A4)
    writer.createPDF(c, ['Кол-во'] + num, ['% от общ.'] + per, total)
    c.save()


