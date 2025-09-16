from pico2d import *

# 더블 버퍼링 방식으로 캔버스 열기
open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')

# 캐릭터 시작 위치
x, y = 20, 90

# 모든 움직임을 감싸는 무한 루프
while True:
    # 1. 오른쪽으로 이동 (y는 90으로 고정)
    while x < 780:
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x, y)
        update_canvas()
        x += 2
        delay(0.01)

    # 2. 위로 이동 (x는 마지막 값(780)을 그대로 사용)
    while y < 580:
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x, y)
        update_canvas()
        y += 2
        delay(0.01)

    # 3. 왼쪽으로 이동 (y는 마지막 값(580)을 그대로 사용)
    while x > 20:
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x, y)
        update_canvas()
        x -= 2
        delay(0.01)

    # 4. 아래로 이동 (x는 마지막 값(20)을 그대로 사용)
    while y > 90:
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x, y)
        update_canvas()
        y -= 2
        delay(0.01)

close_canvas()