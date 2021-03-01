"""
Reportlab sandbox.
"""
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import A4, portrait
from chess_board import create_chess_board

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

doc = SimpleDocTemplate("form_letter.pdf",pagesize=portrait(A4),
                        rightMargin=72,leftMargin=72,
                        topMargin=72,bottomMargin=18)

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

Story=[]
logo = "merida/72/bb.png"

# We really want to scale the image to fit in a box and keep proportions.
im = Image(logo, 3*inch, 3*inch)
Story.append(im)

chess_board = create_chess_board()
Story.append(chess_board)


#ptext = '<font size=12>Some text</font>' 
#Story.append(Paragraph(ptext, styles["Normal"]))

ptext = '''
<seq>. </seq>Some Text<br/>
<seq>. </seq>Some more test Text
'''
Story.append(Paragraph(ptext, styles["Bullet"]))

ptext='<bullet>&bull;</bullet>Some Text'
Story.append(Paragraph(ptext, styles["Bullet"]))

doc.build(Story)