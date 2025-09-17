from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')

x,y= 20,90
while (x < 800):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, 90)
    x = x + 2
    delay(0.01)


#잔디 위에서 위로
while (y < 720):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(750, y)
    y = y + 2
    delay(0.01)

    x=750
while (x > 30):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, 550)
    x = x - 2
    delay(0.01)

y = 570
while (y > 90):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(20, y)
    y = y - 2
    delay(0.01)


    def move_circle():
        cx, cy, r = 400, 300, 200
        for degree in range(0, 360, 2):
            rad = math.radians(degree)
            x = cx + r * math.cos(rad)
            y = cy + r * math.sin(rad)
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(int(x), int(y))
            delay(0.01)
    while True :




 close_canvas()