import pyautogui as auto
import time

class ScareCrow():
    '''
        Classe para o personagem Scare Crow.
    '''

    def choose_me(self):
        auto.keyDown("right")
        time.sleep(0.3)
        auto.keyUp("right")
        time.sleep(0.5)

        auto.keyDown("right")
        time.sleep(0.3)
        auto.keyUp("right")
        time.sleep(0.5)

        auto.keyDown("right")
        time.sleep(0.3)
        auto.keyUp("right")
        time.sleep(0.5)

        auto.keyDown("right")
        time.sleep(0.3)
        auto.keyUp("right")
        time.sleep(0.5)

        auto.keyDown("right")
        time.sleep(0.3)
        auto.keyUp("right")
        time.sleep(0.5)

        auto.keyDown("right")
        time.sleep(0.3)
        auto.keyUp("right")
        time.sleep(0.5)

        auto.keyDown("down")
        time.sleep(0.3)
        auto.keyUp("down")
        time.sleep(0.5)

    def log(self):
        print("Scare Crow chosen.")

