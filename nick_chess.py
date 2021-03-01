from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.pagesizes import A4, landscape, portrait


import chess.pgn

# TODO: find out which variables are present in most games
def extract_variables(game):
    return {
        'event': game.headers['Event'],
        'site': game.headers['Site'],
        'date': game.headers['Date'],
        'round': game.headers['Round'],
        'white': game.headers['White'],
        'black': game.headers['Black'],
    }

# TODO: Extract into a function
# Open the pgn file
pgn = open("pgn/kasparov.pgn")
game = chess.pgn.read_game(pgn)

variables = extract_variables(game)
print(variables)

canvas = Canvas("chess.pdf")
canvas.drawString(72, 72, "Hello, World")
canvas.save()

doc = SimpleDocTemplate("form_letter.pdf",pagesize=portrait(A4),
                        rightMargin=72,leftMargin=72,
                        topMargin=72,bottomMargin=18)
