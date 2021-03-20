import pyautogui as auto
import time

class Cheetah():
    '''
        Classe para o personagem Cheetah.
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

        
    def log(self):
        print("Cheetah chosen.")

