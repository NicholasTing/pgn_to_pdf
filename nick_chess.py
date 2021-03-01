from reportlab.pdfgen.canvas import Canvas
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

# Open the pgn file
pgn = open("pgn/caro_kann.pgn")
game = chess.pgn.read_game(pgn)

variables = extract_variables(game)
print(variables)

canvas = Canvas("hello.pdf")
canvas.drawString(72, 72, "Hello, World")
canvas.save()