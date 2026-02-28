# AIR CHESS – WHITE OBJECT + TWO-FINGER GESTURE CONTROL
# Detect white object for cursor
# Detect TWO fingers to select/drop piece (no keyboard)

# Install:
# pip install opencv-python pygame python-chess numpy

import cv2
import pygame
import chess
import numpy as np
import math

# ---------------- PYGAME SETUP ----------------
pygame.init()
WIDTH, HEIGHT = 640, 640
SQ_SIZE = WIDTH // 8
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Air Chess - 2 Finger Gesture")

font = pygame.font.SysFont("Arial", 32)
board = chess.Board()
selected_square = None
gesture_cooldown = 0

# ---------------- CAMERA ----------------
cap = cv2.VideoCapture(0)

# WHITE HSV RANGE
lower_white = np.array([0, 0, 200])
upper_white = np.array([179, 40, 255])

# ---------------- DRAW FUNCTIONS ----------------
def draw_board():
    colors = [(240,217,181), (181,136,99)]
    for r in range(8):
        for c in range(8):
            color = colors[(r+c)%2]
            pygame.draw.rect(screen, color, (c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

def draw_pieces():
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            row = 7 - (square // 8)
            col = square % 8
            text = font.render(piece.symbol(), True, (0,0,0) if piece.color else (255,255,255))
            screen.blit(text, (col*SQ_SIZE+20, row*SQ_SIZE+20))

# ---------------- FINGER COUNT FUNCTION ----------------
def count_fingers(contour, frame):
    hull = cv2.convexHull(contour, returnPoints=False)
    if hull is None or len(hull) < 3:
        return 0

    defects = cv2.convexityDefects(contour, hull)
    if defects is None:
        return 0

    finger_count = 0
    for i in range(defects.shape[0]):
        s, e, f, d = defects[i, 0]
        start = tuple(contour[s][0])
        end = tuple(contour[e][0])
        far = tuple(contour[f][0])

        a = math.dist(start, end)
        b = math.dist(start, far)
        c = math.dist(end, far)

        angle = math.acos((b**2 + c**2 - a**2) / (2*b*c + 1e-5))

        if angle <= math.pi/2 and d > 10000:
            finger_count += 1

    return finger_count + 1

# ---------------- MAIN LOOP ----------------
running = True
while running:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, lower_white, upper_white)
    mask = cv2.GaussianBlur(mask, (15,15), 0)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cursor_pos = None
    finger_count = 0

    if contours:
        largest = max(contours, key=cv2.contourArea)
        if cv2.contourArea(largest) > 2000:
            x,y,w,h = cv2.boundingRect(largest)
            cx = x + w//2
            cy = y + h//2
            cursor_pos = (cx, cy)
            cv2.circle(frame, (cx,cy), 10, (0,255,0), -1)

            finger_count = count_fingers(largest, frame)
            cv2.putText(frame, f"Fingers: {finger_count}", (10,50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if cursor_pos and finger_count == 2 and gesture_cooldown == 0:
        x = int(cursor_pos[0] * WIDTH / frame.shape[1])
        y = int(cursor_pos[1] * HEIGHT / frame.shape[0])
        col = x // SQ_SIZE
        row = y // SQ_SIZE

        if 0 <= col < 8 and 0 <= row < 8:
            square = chess.square(col, 7-row)

            if selected_square is None:
                if board.piece_at(square) and board.piece_at(square).color == board.turn:
                    selected_square = square
            else:
                move = chess.Move(selected_square, square)
                if move in board.legal_moves:
                    board.push(move)
                selected_square = None

        gesture_cooldown = 20  # prevent repeated moves

    if gesture_cooldown > 0:
        gesture_cooldown -= 1

    draw_board()
    draw_pieces()

    turn_text = "White Turn" if board.turn else "Black Turn"
    screen.blit(font.render(turn_text, True, (255,0,0)), (10,10))

    pygame.display.flip()

    cv2.imshow("White + Two Finger Control", frame)
    cv2.imshow("Mask", mask)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
pygame.quit()
