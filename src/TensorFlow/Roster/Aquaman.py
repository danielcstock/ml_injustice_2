import pyautogui as auto
import time

class Aquaman():
    '''
        Classe para o personagem Aquaman.
    '''

    def choose_me(self):
        auto.keyDown("left")
        time.sleep(0.3)
        auto.keyUp("left")
        time.sleep(0.5)

        auto.keyDown("down")
        time.sleep(0.3)
        auto.keyUp("down")
        time.sleep(0.5)


    def log(self):
        print("Aquaman chosen.")

