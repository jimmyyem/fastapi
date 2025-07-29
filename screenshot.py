import os
import uuid

import pyautogui

image_maker = pyautogui.screenshot()

dir_name = "screen"

unique_id = uuid.uuid4()
file_name = os.path.join(dir_name, f"{str(unique_id)}.png")

os.makedirs(dir_name, exist_ok=True)
image_maker.save(file_name)