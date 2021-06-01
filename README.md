# pybot
A python bot that can automatically send specific messages when triggered.
The bot ("bot.py") reads the text message from the file: "file.txt" and automatically types it and presses enter on your keyboard to send it.
You can bookmark <a href="https://kooldamian28.github.io/pybot/">this page</a> also for easy reference: <a href="https://kooldamian28.github.io/pybot/">kooldamian28.github.io/pybot/</a>

## Instructions
1. Enter your personal message in "file.txt"
2. Run the "bot.py"
3. Click on the text field you want the bot to type in.

### More info
The bot is programmed to wait for 5 seconds before typing, if you want to adjust the delay, go to line 2 or the line which says "time.sleep(5)" and enter the time in seconds between the brackets. In the format as, time.sleep(seconds), where "seconds" is the time in seconds.

In line 4 you can adjust the bot to open any file you want, in the format, a = open("anyfile"), where "anyfile" is the file you want to open.

## Instructions for the release (pybot 2.0):
Download the bot here: [pybot 2.0](https://github.com/kooldamian28/pybot/releases/download/2.0.0/pybot.exe)

Make sure a file named "file" in the text format (.txt) is in in the same directory where this application is running. For example, if "pybot.exe" is there in a directory named "foobar", "file.txt" should also be in "foobar".

"file.txt" is where you are supposed to enter the text that you want to the application to type.

### Instructions:
1. Make sure "pybot.exe" and "file.txt" is in the same directory.
2. Enter your personal message in "file.txt".
3. Go to cmd and cd into the directory where "pybot.exe" and "file.txt" is present, then run the program from command-line by entering
"pybot.exe".
4. Click on the text field you want the bot to type in within 5 seconds.
