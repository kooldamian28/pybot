import pyautogui, time
time.sleep(5)

a = open("file.txt")

for word in a:
  pyautogui.typewrite(word)
  pyautogui.press("enter")
