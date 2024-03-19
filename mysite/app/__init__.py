from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import A4

data = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

pdf = SimpleDocTemplate('can.pdf', pagesize=A4)

from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from reportlab.lib import colors

table = Table(data)
style = TableStyle([
    ('BACKGROUND', (0, 0), (3, 0), colors.chocolate),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), "Courier-Bold"),
    ('FONTSIZE', (0, 0), (-1, 0), 14),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige)
])
table.setStyle(style)

rowNmb = len(data)
for i in range(1, rowNmb):
    if i % 2 == 0:
        bc = colors.burlywood
    else:
        bc = colors.beige
    ts = TableStyle([('BACKGROUND', (0, i), (-1, i), bc)])
    table.setStyle(ts)
ts = TableStyle([
                 ('GRID', (0, 0), (-1, -1), 1, colors.black)
                 ])
table.setStyle(ts)
elems = []
elems.append(table)
pdf.build(elems)
