import time
import pyperclip
x = pyperclip.paste()
x = x.replace("    ","	")
pyperclip.copy(x)
