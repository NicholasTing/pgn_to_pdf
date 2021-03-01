from PIL import Image
import chess.pgn


def create_chess_board(pgn):
    size = 8
    img = Image.new("RGB", (size,size), "white") # create a new 15x15 image
    pixels = img.load() # create the pixel map

    black_2 = []
    for i in range(img.size[0]):
        if i % 2 == 0:
            black_2.append(i)

    black_1 = [i-1 for i in black_2 if i > 0]
    if img.size[0] % 2 == 0: # 'that' if statement
        black_1.append(img.size[0]-1)


    for i in black_1:
        for j in range(0, size, 2):
            pixels[i,j] = (0,0,0)

    for k in black_2:
        for l in range(1, size, 2):
            pixels[k,l] = (0,0,0)

    # img.show()
    return img

# TODO: Extract into a function
# Open the pgn file
pgn = open("pgn/carokann.pgn")
game = chess.pgn.read_game(pgn)


for i, move in enumerate(game.mainline()):
    print('i')
    print(i)
    print('\n')
    print('move')
    print(move)
    print('\n')
    
create_chess_board(pgn)