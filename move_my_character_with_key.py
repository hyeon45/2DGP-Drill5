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

while running:
    clear_canvas()

    background.draw_to_origin(0, 0, 800, 600)
    character.clip_draw(frame * 60, 60 * 1, 60, 60, x, y, 100, 100)

    update_canvas()
    handle_events()

    frame = (frame + 1) % 8

    x += dir * 5
    y += height * 5

    delay(0.05)

close_canvas()