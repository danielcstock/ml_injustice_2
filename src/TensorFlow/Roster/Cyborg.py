import pyautogui as auto
import time

class Cyborg():
    '''
        Classe para o personagem Cyborg.
    '''

    def choose_me(self):
        auto.keyDown("left")
        time.sleep(0.3)
        auto.keyUp("left")
        time.sleep(0.5)

        auto.keyDown("left")
        time.sleep(0.3)
        auto.keyUp("left")
        time.sleep(0.5)

        auto.keyDown("left")
        time.sleep(0.3)
        auto.keyUp("left")
        time.sleep(0.5)

        auto.keyDown("left")
        time.sleep(0.3)
        auto.keyUp("left")
        time.sleep(0.5)

        auto.keyDown("left")
        time.sleep(0.3)
        auto.keyUp("left")
        time.sleep(0.5)

        auto.keyDown("left")
        time.sleep(0.3)
        auto.keyUp("left")
        time.sleep(0.5)

        

    def log(self):
        print("Cyborg chosen.")

