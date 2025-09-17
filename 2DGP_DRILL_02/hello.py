from pico2d import *
import math # 원 운동을 위해 수학 모듈을 가져옵니다.

open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')

# 캐릭터 시작 위치
x, y = 400, 90

# 메인 루프
while True:
    # --- 사각형 운동 ---
    # 1. 오른쪽으로 이동 (아래쪽 변)
    while x < 780:
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x, 90)
        update_canvas()
        x += 2
        delay(0.01)

    # 2. 위로 이동 (오른쪽 변)
    while y < 580:
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x, y)
        update_canvas()
        y += 2
        delay(0.01)

    # 3. 왼쪽으로 이동 (위쪽 변)
    while x > 20:
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x, y)
        update_canvas()
        x -= 2
        delay(0.01)

    # 4. 아래로 이동 (왼쪽 변)
    while y > 90:
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x, y)
        update_canvas()
        y -= 2
        delay(0.01)

    # --- 원 운동 ---
    # 원 운동을 위해 각도를 사용합니다.
    cx, cy, r = 400, 340, 250 # 원의 중심 좌표와 반지름
    degree = 0

    while degree < 360:
        x = cx + r * math.cos(math.radians(degree)) # x 좌표 계산
        y = cy + r * math.sin(math.radians(degree)) # y 좌표 계산

        clear_canvas()
        grass.draw(400, 30)
        character.draw(x, y)
        update_canvas()

        degree += 1 # 각도 증가
        delay(0.01)

close_canvas()