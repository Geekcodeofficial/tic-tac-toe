import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300
LINE_COLOR = (255, 255, 255)
LINE_WIDTH = 15
CIRCLE_RADIUS = 30  # Adjusted size
CIRCLE_COLOR = (0, 255, 0)
CROSS_LENGTH = 30  # Adjusted size
CROSS_COLOR = (255, 0, 0)
FONT_COLOR = (255, 255, 255)
FONT_SIZE = 36

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Game variables
board = [['', '', ''], ['', '', ''], ['', '', '']]
current_player = 'X'
game_over = False
winner = None

# Function to draw the Tic Tac Toe grid
def draw_grid():
    cell_size = SCREEN_WIDTH // 3

    # Draw horizontal lines
    for i in range(1, 3):
        pygame.draw.line(screen, LINE_COLOR, (0, i * cell_size), (SCREEN_WIDTH, i * cell_size), LINE_WIDTH)

    # Draw vertical lines
    for i in range(1, 3):
        pygame.draw.line(screen, LINE_COLOR, (i * cell_size, 0), (i * cell_size, SCREEN_HEIGHT), LINE_WIDTH)

    # Draw borders around each cell
    for row in range(3):
        for col in range(3):
            pygame.draw.rect(screen, LINE_COLOR, (col * cell_size, row * cell_size, cell_size, cell_size), LINE_WIDTH)

# Function to draw X at a specific position
def draw_x(row, col):
    pygame.draw.line(screen, CROSS_COLOR, (col * SCREEN_WIDTH // 3 + CROSS_LENGTH, row * SCREEN_HEIGHT // 3 + CROSS_LENGTH),
                     ((col + 1) * SCREEN_WIDTH // 3 - CROSS_LENGTH, (row + 1) * SCREEN_HEIGHT // 3 - CROSS_LENGTH), LINE_WIDTH)
    pygame.draw.line(screen, CROSS_COLOR, ((col + 1) * SCREEN_WIDTH // 3 - CROSS_LENGTH, row * SCREEN_HEIGHT // 3 + CROSS_LENGTH),
                     (col * SCREEN_WIDTH // 3 + CROSS_LENGTH, (row + 1) * SCREEN_HEIGHT // 3 - CROSS_LENGTH), LINE_WIDTH)

# Function to draw O at a specific position
def draw_o(row, col):
    pygame.draw.circle(screen, CIRCLE_COLOR, (col * SCREEN_WIDTH // 3 + SCREEN_WIDTH // 6,
                                               row * SCREEN_HEIGHT // 3 + SCREEN_HEIGHT // 6), CIRCLE_RADIUS, LINE_WIDTH)

# Function to check for a winner
def check_winner():
    global winner
    # Check rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != '':
            winner = board[row][0]
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '':
            winner = board[0][col]
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '':
        winner = board[0][0]
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '':
        winner = board[0][2]
        return True

    return False

# Function to check if the board is full
def is_board_full():
    for row in range(3):
        for col in range(3):
            if board[row][col] == '':
                return False
    return True

# Function to display the winner or a tie
def display_result():
    font = pygame.font.Font(None, FONT_SIZE)
    if winner:
        result_text = f"{winner} wins!"
    else:
        result_text = "It's a tie!"
    text = font.render(result_text, True, FONT_COLOR)
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()
    pygame.time.delay(3000)  # Display the result for 3 seconds
    reset_game()

# Function to reset the game
def reset_game():
    global board, current_player, game_over, winner
    board = [['', '', ''], ['', '', ''], ['', '', '']]
    current_player = 'X'
    game_over = False
    winner = None
    screen.fill((0, 0, 0))
    draw_grid()
    pygame.display.flip()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX, mouseY = pygame.mouse.get_pos()
            clicked_row = mouseY // (SCREEN_HEIGHT // 3)
            clicked_col = mouseX // (SCREEN_WIDTH // 3)

            if board[clicked_row][clicked_col] == '':
                if current_player == 'X':
                    draw_x(clicked_row, clicked_col)
                    board[clicked_row][clicked_col] = 'X'
                else:
                    draw_o(clicked_row, clicked_col)
                    board[clicked_row][clicked_col] = 'O'

                if check_winner():
                    game_over = True
                    display_result()
                elif is_board_full():
                    game_over = True
                    display_result()
                else:
                    current_player = 'O' if current_player == 'X' else 'X'

    pygame.display.flip()
