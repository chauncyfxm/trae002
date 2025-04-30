import pyautogui
import numpy as np


def recognize_icon_by_color(target_color, tolerance=30):
    # 进行屏幕截图
    screenshot = pyautogui.screenshot()
    screenshot_np = np.array(screenshot)

    # 转换目标颜色为 numpy 数组
    target_color_np = np.array(target_color)

    # 计算每个像素与目标颜色的差异
    color_differences = np.sqrt(np.sum((screenshot_np - target_color_np) ** 2, axis=-1))

    # 找到差异在容差范围内的像素
    matching_pixels = np.where(color_differences <= tolerance)

    if len(matching_pixels[0]) > 0:
        # 找到匹配像素的边界
        min_x = np.min(matching_pixels[1])
        max_x = np.max(matching_pixels[1])
        min_y = np.min(matching_pixels[0])
        max_y = np.max(matching_pixels[0])

        return (min_x, min_y, max_x - min_x, max_y - min_y)
    else:
        return None


if __name__ == '__main__':
    # 示例：指定目标颜色为红色
    target_color = (255, 74, 54)
    result = recognize_icon_by_color(target_color)
    if result:
        print(f'找到图标，位置：{result}')
    else:
        print('未找到图标。')