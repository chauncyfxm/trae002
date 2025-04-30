import pyautogui


def move_mouse(x, y):
    try:
        pyautogui.moveTo(x, y)
        print(f'鼠标已移动到坐标 ({x}, {y})')
    except Exception as e:
        print(f'移动鼠标时出错: {e}')


if __name__ == '__main__':
    # 示例: 移动鼠标到坐标 (100, 200)
    x = 100
    y = 200
    move_mouse(x, y)