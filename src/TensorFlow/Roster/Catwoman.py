import pyautogui as auto
import time

class Catwoman():
    '''
        Classe para o personagem Catwoman.
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

    def log(self):
        print("Catwoman chosen.")

