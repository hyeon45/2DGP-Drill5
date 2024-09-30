from pico2d import *

open_canvas()
background = load_image('TUK_GROUND.png')
character = load_image('download_character_image.png')

running = True
frame = 0
x = 800 // 2
y = 90
dir = 0
height = 0

def handle_events():
    global running, dir, height

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
            elif event.key == SDLK_LEFT:
                dir -= 1
            elif event.key == SDLK_UP:
                height += 1
            elif event.key == SDLK_DOWN:
                height -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.key == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1
            elif event.key == SDLK_UP:
                height -= 1
            elif event.key == SDLK_DOWN:
                height += 1

def screen_boundary():
    global x, y

    if x < 0:
        x = 0
    elif x > 800 - 60:
        x = 800 - 60
    if y < 0:
        y = 0
    elif y > 600 - 60:
        y = 600 - 60

def draw_character():
    global flame, x, y

    if dir > 0:
        character.clip_draw(frame * 60, 60, 60, 60, x, y, 100, 100)
    elif dir < 0:
        character.clip_draw(frame * 60, 120, 60, 60, x, y, 100, 100)
    elif height > 0:
        character.clip_draw(frame * 60, 0, 60, 60, x, y, 100, 100)
    elif height < 0:
        character.clip_draw(frame * 60, 180, 60, 60, x, y, 100, 100)
    else:
        character.clip_draw(frame * 60, 0, 60, 60, x, y, 100, 100)

while running:
    clear_canvas()

    background.draw_to_origin(0, 0, 800, 600)
    draw_character()

    update_canvas()
    handle_events()

    frame = (frame + 1) % 8

    x += dir * 5
    y += height * 5

    screen_boundary()

    delay(0.05)

close_canvas()