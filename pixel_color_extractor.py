import pyautogui


def get_pixel_color(x, y):
    try:
        screenshot = pyautogui.screenshot()
        pixel_color = screenshot.getpixel((x, y))
        return pixel_color
    except Exception as e:
        print(f'提取像素颜色时出错: {e}')
        return None


if __name__ == '__main__':
    # 示例: 获取坐标 (100, 200) 的像素颜色 (354, 35)
    x = 354
    y = 35
    color = get_pixel_color(x, y)
    if color:
        print(f'坐标 ({x}, {y}) 的像素颜色为: {color}')