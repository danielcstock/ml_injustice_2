import pyautogui as auto
import time

class Atrocitus():
    '''
        Classe para o personagem Atrocitus.
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
        
    def log(self):
        print("Atrocitus has been chosen.")