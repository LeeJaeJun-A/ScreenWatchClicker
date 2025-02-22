import time
import random
import pyautogui
from PIL import ImageGrab, ImageChops

# 모니터링할 화면상의 영역
MONITORING_AREAS = []
CLICK_POSITIONS = []

def get_screen_image(area):
    """지정된 화면 영역에서 이미지를 캡처"""
    return ImageGrab.grab(bbox=area)

def images_different(img1, img2):
    """두 이미지가 다르면 True 반환"""
    img1 = img1.convert("L")
    img2 = img2.convert("L")
    diff = ImageChops.difference(img1, img2)
    extrema = diff.getextrema()
    return max(extrema) > 10  # 10 이상의 차이가 있으면 True

def record_monitoring_areas():
    """모니터링할 영역을 사용자가 지정할 수 있도록 함"""
    while True:
        while True:
            print("모니터링할 영역의 왼쪽 상단에 마우스를 위치시키고 5초 기다립니다...")
            time.sleep(5)
            x1, y1 = pyautogui.position()
            print("모니터링할 영역의 오른쪽 하단에 마우스를 위치시키고 5초 기다립니다...")
            time.sleep(5)
            x2, y2 = pyautogui.position()
            area = (x1, y1, x2, y2)
            img = get_screen_image(area)
            img.show()
            confirm = input("이 영역이 맞습니까? (y/n): ")
            if confirm.lower() == 'y':
                MONITORING_AREAS.append(area)
                break
        more = input("더 추가하시겠습니까? (y/n): ")
        if more.lower() != 'y':
            break

def record_click_positions():
    """각 모니터링 영역에 대해 클릭할 위치를 기록"""
    print("마우스 클릭 위치를 지정하세요.")
    for i in range(len(MONITORING_AREAS)):
        print(f"{i+1}번째 영역의 클릭할 위치에 마우스를 위치시키고 5초 기다립니다...")
        time.sleep(5)
        x, y = pyautogui.position()
        CLICK_POSITIONS.append((x, y))
        print(f"기록된 클릭 위치 {i+1}: {x}, {y}")

def refresh_screen():
    """스크린을 새로고침하는 동작"""
    pyautogui.hotkey('command', 'r')  # Mac용
    # pyautogui.press('f5')  # Windows용
    time.sleep(1)

def monitor_and_click():
    """설정된 영역을 모니터링하고 변화 감지 시 클릭"""
    prev_images = [get_screen_image(area) for area in MONITORING_AREAS]
    while MONITORING_AREAS:
        time.sleep(random.uniform(0.5, 1.5))
        refresh_screen()
        new_images = [get_screen_image(area) for area in MONITORING_AREAS]
        
        for i in reversed(range(len(MONITORING_AREAS))):
            if images_different(prev_images[i], new_images[i]):
                print(f"변화 감지: 영역 {i+1} -> 클릭 위치 이동")
                x, y = CLICK_POSITIONS[i]
                pyautogui.moveTo(x, y, duration=0.1)
                pyautogui.click()
                
                del MONITORING_AREAS[i]
                del CLICK_POSITIONS[i]
                del prev_images[i]
                del new_images[i]

record_monitoring_areas()
record_click_positions()
monitor_and_click()
