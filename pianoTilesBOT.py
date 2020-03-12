import pyautogui,keyboard
from PIL import ImageGrab

#www.mouseaccuracy.com

pyautogui.FAILSAFE = True
keyboard.wait('space')

sc = ImageGrab.grab(bbox=(717,615,1160,720))
x1,y1 = sc.size
c_break = False
for i in range (0,x1,30):
    if c_break == True:
        break
    for j in range (0,y1,30):
        r,g,b = sc.getpixel((i,j))
        if r == 54:
            pyautogui.click(i+717,j+615)
            c_break = True
            break

while True:
    screen = ImageGrab.grab(bbox=(740,400,1190,530))
    x,y = screen.size
    c_break = False
    for i in range (0,x,60):
        if c_break == True:
            break
        for j in range (0,y,30):
            r,g,b = screen.getpixel((i,j))
            if (r == 0 and g == 0 and b == 0) or (r == 16 and g == 20 and b == 19):
                pyautogui.click(i+740,j+460)
                c_break = True
                break
        