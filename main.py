import pygame, sys

pygame.init()

WIDTH, HEIGHT = 900, 900
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe!")

# Load images
BOARD = pygame.image.load("assets/Board.png")
X_IMG = pygame.image.load("assets/X.png")
O_IMG = pygame.image.load("assets/O.png")
X_WIN_IMG = pygame.image.load("assets/Winning X.png")  # Winning image for X
O_WIN_IMG = pygame.image.load("assets/Winning O.png")  # Winning image for O

BG_COLOR = (214, 201, 227)

# Initialize the board
board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
graphical_board = [[[None, None] for _ in range(3)] for _ in range(3)]
to_move = 'X'

# Fill the screen with background color and place the board image
SCREEN.fill(BG_COLOR)
SCREEN.blit(BOARD, (64, 64))
pygame.display.update()

# Initialize game_finished to False
game_finished = False


def render_board(board, X_IMG, O_IMG):
    global graphical_board
    for i in range(3):
        for j in range(3):
            if board[i][j] == "X":
                graphical_board[i][j][0] = X_IMG
                graphical_board[i][j][1] = X_IMG.get_rect(center=(j*300 + 150, i*300 + 150))
            elif board[i][j] == "O":
                graphical_board[i][j][0] = O_IMG
                graphical_board[i][j][1] = O_IMG.get_rect(center=(j * 300 + 150, i * 300 + 150))


def add_XO(board, graphical_board, to_move):
    current_pos = pygame.mouse.get_pos()
    converted_x = (current_pos[0] - 64) // 300  # Correct conversion for X
    converted_y = (current_pos[1] - 64) // 300  # Correct conversion for Y

    if 0 <= converted_x < 3 and 0 <= converted_y < 3:
        if board[converted_y][converted_x] != "O" and board[converted_y][converted_x] != "X":
            board[converted_y][converted_x] = to_move
            if to_move == "O":
                to_move = "X"
            else:
                to_move = "O"

    render_board(board, X_IMG, O_IMG)

    for i in range(3):
        for j in range(3):
            if graphical_board[i][j][0] is not None:
                SCREEN.blit(graphical_board[i][j][0], graphical_board[i][j][1])

    return board, to_move


def check_win(board):
    winner = None
    # Check rows for a win
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] is not None:
            winner = board[row][0]
            for i in range(3):
                graphical_board[row][i][0] = X_WIN_IMG if winner == 'X' else O_WIN_IMG
                SCREEN.blit(graphical_board[row][i][0], graphical_board[row][i][1])
            pygame.display.update()
            return winner

    # Check columns for a win
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            winner = board[0][col]
            for i in range(3):
                graphical_board[i][col][0] = X_WIN_IMG if winner == 'X' else O_WIN_IMG
                SCREEN.blit(graphical_board[i][col][0], graphical_board[i][col][1])
            pygame.display.update()
            return winner

    # Check diagonal (top-left to bottom-right)
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        winner = board[0][0]
        for i in range(3):
            graphical_board[i][i][0] = X_WIN_IMG if winner == 'X' else O_WIN_IMG
            SCREEN.blit(graphical_board[i][i][0], graphical_board[i][i][1])
        pygame.display.update()
        return winner

    # Check diagonal (top-right to bottom-left)
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        winner = board[0][2]
        for i in range(3):
            graphical_board[i][2 - i][0] = X_WIN_IMG if winner == 'X' else O_WIN_IMG
            SCREEN.blit(graphical_board[i][2 - i][0], graphical_board[i][2 - i][1])
        pygame.display.update()
        return winner

    # Check for draw
    if winner is None:
        for i in range(3):
            for j in range(3):
                if board[i][j] != 'X' and board[i][j] != 'O':
                    return None
        return "DRAW"


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_finished:
            # Only allow moves when the game is not finished
            board, to_move = add_XO(board, graphical_board, to_move)

            winner = check_win(board)
            if winner is not None:
                game_finished = True

            render_board(board, X_IMG, O_IMG)
            pygame.display.update()

        # If the game is finished, wait for a click to reset
        elif event.type == pygame.MOUSEBUTTONDOWN and game_finished:
            # Reset the game when clicked after game is finished
            board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            graphical_board = [[[None, None] for _ in range(3)] for _ in range(3)]
            to_move = 'X'
            SCREEN.fill(BG_COLOR)
            SCREEN.blit(BOARD, (64, 64))
            game_finished = False
            pygame.display.update()
