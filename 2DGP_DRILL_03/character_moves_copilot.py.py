from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')

x, y = 0,90 #시작 지정

while True:
    while x < 750:
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x, y)
        update_canvas()
        x += 2
        delay(0.01)

    # 위로 이동
    while y < 550:
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x, y)
        update_canvas()
        y += 2
        delay(0.01)

    # 왼쪽으로 이동
    while x > 50:
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x, y)
        update_canvas()
        x -= 2
        delay(0.01)

    # 아래로 이동
    while y > 90:
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x, y)
        update_canvas()
        y -= 2
        delay(0.01)



    # 2. 삼각형 운동 copilot 참조
    triangle_points = [
        (x, y),  # 현재 위치에서 시작
        (750, 550),  # 오른쪽 위 꼭짓점
        (50, 550),  # 왼쪽 위 꼭짓점
    ]

    for i in range(3):
        start_x, start_y = triangle_points[i]
        end_x, end_y = triangle_points[(i + 1) % 3]
        steps = 100
        for t in range(steps):
            x = start_x + (end_x - start_x) * t / steps
            y = start_y + (end_y - start_y) * t / steps
            clear_canvas()
            grass.draw(400, 30)
            character.draw(x, y)
            update_canvas()
            delay(0.01)
    #copilot 참조 끝

    # 3. 원 운동
    cx, cy, r = 400, 300, 200
    degree = 0
    while degree < 360:
        rad = math.radians(degree)
        x = cx + r * math.cos(rad)
        y = cy + r * math.sin(rad)
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x, y)
        update_canvas()
        degree += 2
        delay(0.01)
close_canvas()