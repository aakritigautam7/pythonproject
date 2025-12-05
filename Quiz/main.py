import pygame
import sys
import time
from questions import categories, get_shuffled_questions
import random

pygame.init()

# ---------------------- SCREEN ----------------------
WIDTH, HEIGHT = 900, 550
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Advanced Quiz App")

# ---------------------- FONTS ----------------------
font_big = pygame.font.SysFont("comicsansms", 40)
font_med = pygame.font.SysFont("comicsansms", 28)
font_question = pygame.font.SysFont("comicsansms", 24)  
font_small = pygame.font.SysFont("comicsansms", 20) 

# ---------------------- BACKGROUND ----------------------
bg = pygame.image.load("assets/bg.jpg")
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

# ---------------------- SOUNDS ----------------------
click_s = pygame.mixer.Sound("assets/click.wav")
correct_s = pygame.mixer.Sound("assets/correct.wav")
wrong_s = pygame.mixer.Sound("assets/wrong.wav")
beep_s = pygame.mixer.Sound("assets/click.wav") 

# ---------------------- GLOBALS ----------------------
state = "input_name"
player_name = ""
current_category = None
questions = []
current_q = 0
score = 0
timer = 15
last_tick = time.time()
selected_option = None
next_enabled = False
num_questions = 5
difficulty = "Pro"
difficulty_times = {"Beginner": 30, "Pro": 20, "Fastest": 10}

# ---------------------- HIGH SCORE ----------------------
def load_highscores():
    try:
        with open("highscore.txt", "r") as f:
            scores = [line.strip().split(",") for line in f.readlines()]
            scores = [(n, int(s)) for n, s in scores]
            scores.sort(key=lambda x: x[1], reverse=True)
            return scores[:3]  # show only top 3
    except:
        return []

def save_highscore(name, new_score):
    scores = load_highscores()
    scores.append((name, new_score))
    scores.sort(key=lambda x: x[1], reverse=True)
    scores = scores[:3]  # keep only top 3
    with open("highscore.txt", "w") as f:
        for n, s in scores:
            f.write(f"{n},{s}\n")

# ---------------------- DRAW FUNCTIONS ----------------------
def draw_text_center(txt, y, font=font_med, color=(255, 255, 255)):
    t = font.render(txt, True, color)
    rect = t.get_rect(center=(WIDTH//2, y))
    screen.blit(t, rect)

def draw_button(text, x, y, w, h, mouse):
    rect = pygame.Rect(x, y, w, h)
    color = (220, 220, 255) if rect.collidepoint(mouse) else (200, 200, 255)
    pygame.draw.rect(screen, color, rect, border_radius=10)
    txt = font_small.render(text, True, (0, 0, 0))
    screen.blit(txt, (x + 10, y + 10))
    return rect

def reset_quiz():
    global questions, current_q, score, timer, selected_option, next_enabled
    if current_category == "Mixed Bag":
        all_q = []
        for cat in categories.keys():
            all_q.extend(categories[cat])
        random.shuffle(all_q)
        questions = all_q[:num_questions]
    else:
        questions = get_shuffled_questions(current_category)[:num_questions]
    current_q = 0
    score = 0
    timer = difficulty_times[difficulty]
    selected_option = None
    next_enabled = False

# ---------------------- MAIN LOOP ----------------------
while True:
    mouse = pygame.mouse.get_pos()
    screen.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # ---------------- INPUT NAME ----------------
        if state == "input_name":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and player_name.strip() != "":
                    state = "menu"
                elif event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]
                else:
                    player_name += event.unicode

        # ---------------- MENU SCREEN ----------------
        elif state == "menu":
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_s.play()
                for i, cat in enumerate(list(categories.keys()) + ["Mixed Bag"]):
                    if cat_rects[i].collidepoint(mouse):
                        current_category = cat
                        state = "difficulty"

        # ---------------- DIFFICULTY SCREEN ----------------
        elif state == "difficulty":
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_s.play()
                for i, d in enumerate(difficulty_times.keys()):
                    if diff_rects[i].collidepoint(mouse):
                        difficulty = d
                        state = "num_questions"

        # ---------------- NUM QUESTIONS SCREEN ----------------
        elif state == "num_questions":
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_s.play()
                for i, n in enumerate([5, 10, 15]):
                    if num_rects[i].collidepoint(mouse):
                        num_questions = n
                        reset_quiz()
                        state = "quiz"

        # ---------------- QUIZ SCREEN ----------------
        elif state == "quiz":
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_s.play()
                for i, r in enumerate(opt_rects):
                    if r.collidepoint(mouse) and not next_enabled:
                        selected_option = i
                        if i == questions[current_q]["answer"]:
                            score += 1
                            correct_s.play()
                        else:
                            wrong_s.play()
                        next_enabled = True
                if next_btn.collidepoint(mouse) and next_enabled:
                    current_q += 1
                    if current_q == len(questions):
                        save_highscore(player_name, score)
                        state = "result"
                    else:
                        timer = difficulty_times[difficulty]
                        selected_option = None
                        next_enabled = False

        # ---------------- RESULT SCREEN ----------------
        elif state == "result":
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_s.play()
                if back_btn.collidepoint(mouse):
                    state = "menu"

    # ---------------- DRAW SCREENS ----------------
    if state == "input_name":
        draw_text_center("Enter Your Name and Press Enter", 200, font_med)
        draw_text_center(player_name, 300, font_small)

    elif state == "menu":
        draw_text_center(f"Hello {player_name}! Select Category", 60, font_big)
        cat_rects = []
        for i, cat in enumerate(list(categories.keys()) + ["Mixed Bag"]):
            r = draw_button(cat, 300, 150 + i * 80, 300, 60, mouse)
            cat_rects.append(r)

    elif state == "difficulty":
        draw_text_center("Select Difficulty", 60, font_big)
        diff_rects = []
        for i, d in enumerate(difficulty_times.keys()):
            r = draw_button(d, 350, 150 + i * 80, 200, 60, mouse)
            diff_rects.append(r)

    elif state == "num_questions":
        draw_text_center("Select Number of Questions", 60, font_big)
        num_rects = []
        for i, n in enumerate([5, 10, 15]):
            r = draw_button(str(n), 350, 150 + i * 80, 200, 60, mouse)
            num_rects.append(r)

    elif state == "quiz":
        now = time.time()
        if now - last_tick >= 1:
            last_tick = now
            if not next_enabled:
                timer -= 1
                if 0 < timer <= 5:
                    beep_s.play()
                if timer <= 0:
                    next_enabled = True
                    if selected_option is None:
                        wrong_s.play()
                        selected_option = -1

        q = questions[current_q]["question"]
        draw_text_center(f"Category: {current_category}", 30, font_small)
        draw_text_center(f"Question {current_q + 1}/{len(questions)}", 60, font_small)
        draw_text_center(q, 140, font_question)  # smaller font

        # Timer top-right
        timer_text = font_small.render(f"Time left: {timer}s", True, (255, 255, 255))
        screen.blit(timer_text, (WIDTH - timer_text.get_width() - 20, 10))

        opt_rects = []
        for i, op in enumerate(questions[current_q]["options"]):
            if next_enabled:
                if i == questions[current_q]["answer"]:
                    col = (0, 255, 0)
                elif selected_option == -1 or i == selected_option:
                    col = (255, 0, 0)
                else:
                    col = (200, 200, 255)
            else:
                col = (200, 200, 255)

            rect = pygame.Rect(200, 200 + i * 70, 500, 50)
            pygame.draw.rect(screen, col, rect, border_radius=10)
            draw_text_center(op, 225 + i*70, font_small)
            opt_rects.append(rect)

        next_btn = draw_button("Next", 380, 480, 140, 50, mouse if next_enabled else (-1, -1))

    elif state == "result":
        high_scores = load_highscores()
        draw_text_center("Quiz Completed!", 140, font_big)
        draw_text_center(f"Your Score: {score}", 200, font_big)
        # Feedback 
        feedback = "Outstanding!" if score == len(questions) else "Good Job!" if score >= len(questions)*0.6 else "Try Again!"
        draw_text_center(f"{feedback}", 250, font_big)  
        # Top 3 scores header 
        draw_text_center("Top 3 Scores:", 290, font_med)
        for i, (n, s) in enumerate(high_scores):
            draw_text_center(f"{i+1}. {n} - {s}", 322 + i*40, font_small)

        back_btn = draw_button("Back to Menu", 350, 480, 200, 60, mouse)

    pygame.display.update()
