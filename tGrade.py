import pyautogui as pag


def tabpress3():
    for i in range(0, 3):
        pag.press("tab")


pag.sleep(5)

pag.press("tab")
pag.press("tab")
pag.write("93")
tabpress3()
pag.write("85")
tabpress3()
pag.write("75")
tabpress3()
pag.write("70")
tabpress3()
tabpress3()
pag.press("tab")
pag.press("tab")
pag.press("enter")


