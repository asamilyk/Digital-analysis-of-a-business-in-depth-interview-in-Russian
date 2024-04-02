import os
import app.analysis.text as t
import scipy.io
from reportlab.pdfgen.canvas import Canvas

from reportlab.lib.pagesizes import A4
from app.analysis import writer
#import text as t
#import writer


def analyse(file):
    if os.path.exists("canvas.pdf"):
        os.remove("canvas.pdf")
    c = Canvas("canvas.pdf", pagesize=A4)
    w = writer.Writer(c)
    text = t.Text(w)
    file_content = str(file).replace("\r", " ").replace('\n', ' ')
    text.tokenize(file_content)
    text.general_statistics()
    text.in_ex_reference()
    c.save()


file = "Сейчас я проживаю в Грузии, поэтому я постоянно взаимодействую с грузинами. пошел, играю, нравится, люблю, делаю, сделал, иду, могу, Также здесь много славян из разных стран. Ещё здесь очень много представителей других Кавказских народностей. Например, армяне, азербайджанцы. С ними тоже постоянно работаю. Сейчас я очень плотно работаю с немцами, чехами, арабами, евреями, американцами, англичанами, французами датчанами и китайцами."
analyse(file)
l = 0