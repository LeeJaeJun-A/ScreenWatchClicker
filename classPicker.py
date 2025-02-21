import time
import random
import pyautogui
from PIL import ImageGrab, ImageChops

# 모니터링할 화면상의 영역 (x1, y1, x2, y2) -> TopLeft, BottomRight
MONITORING_AREAS = [(634, 420, 660, 460), (666, 420, 692, 460)]
CLICK_POSITIONS = []

def get_screen_image(area, filename=None):
    """지정된 화면 영역에서 이미지를 캡처하고 저장 (선택적)"""
    img = ImageGrab.grab(bbox=area)
    if filename:
        img.save(filename)
    return img

def images_different(img1, img2):
    """두 이미지가 다르면 True 반환"""
    img1 = img1.convert("L")  # 흑백 변환
    img2 = img2.convert("L")
    diff = ImageChops.difference(img1, img2)
    extrema = diff.getextrema()
    print(f"diff extrema: {extrema}")  # 디버깅용
    return max(extrema) > 10  # 10 이상의 차이가 있으면 True

def record_mouse_positions():
    print("마우스 위치를 기록할 두 개의 지점을 선택하세요.")
    for i in range(len(MONITORING_AREAS)):
        print(f"{i + 1}번째 지점 위에 마우스 포인터를 위치시켜주세요...")
        time.sleep(5)
        x, y = pyautogui.position()
        CLICK_POSITIONS.append((x, y))
        print(f"기록된 위치 {i + 1}: {x}, {y}")

def refresh_screen():
    """스크린을 새로고침하는 동작"""
    pyautogui.hotkey('command', 'r') # For Mac
    # pyautogui.press('f5')  # 웹 브라우저 새로고침
    time.sleep(1)  # 새로고침 후 안정화 대기

def monitor_and_click():
    prev_images = [get_screen_image(area, f"prev_image_{i}.png") for i, area in enumerate(MONITORING_AREAS)]
    while MONITORING_AREAS:
        time.sleep(random.uniform(0.5, 1.5))
        refresh_screen()
        new_images = [get_screen_image(area, f"new_image_{i}.png") for i, area in enumerate(MONITORING_AREAS)]
        
        for i in reversed(range(len(MONITORING_AREAS))):
            if images_different(prev_images[i], new_images[i]):
                print(f"변화 감지: 영역 {i + 1} -> 클릭 위치 이동")
                x, y = CLICK_POSITIONS[i]
                pyautogui.moveTo(x, y, duration=0.1)
                pyautogui.click()
                print("축하축하")
                
                # 클릭한 항목 제거
                del MONITORING_AREAS[i]
                del CLICK_POSITIONS[i]
                del prev_images[i]
                del new_images[i]

record_mouse_positions()
monitor_and_click()
