import pyautogui, time
time.sleep(5)

file = open("file.txt")

for word in file:
  pyautogui.typewrite(word)
  pyautogui.press("enter")
