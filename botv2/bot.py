import pyautogui, time

userinput = input("What do you want to do? \n A. Spam \n B. See License, enter the option in CAPITAL LETTERS \n")

if userinput == "A":
  print("I'm ready. click on the text field you want to spam within 5 seconds!")
  time.sleep(5)
  a = open("file.txt")
  for word in a:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
elif userinput == "B":
  print("\n BSD 3-Clause License \n Copyright (c) 2020, Damian Jude Mascarenhas \n All rights reserved. \n Redistribution and use in source and binary forms, with or without \n modification, are permitted provided that the following conditions are met: \n 1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer. \n 2. Redistributions in binary form must reproduce the above copyright notice, \n this list of conditions and the following disclaimer in the documentation \n and/or other materials provided with the distribution. \n 3. Neither the name of the copyright holder nor the names of its \n contributors may be used to endorse or promote products derived from \n this software without specific prior written permission. \n THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS \" AS IS \" \n AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE \n IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE \n DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE \n FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL \n DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR \n SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER \n CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, \n OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE \n OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.")
