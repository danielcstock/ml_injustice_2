import pyautogui as auto
import time

class TheFlash():
    '''
        Classe para o personagem The Flash.
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
        
    def log(self):
        print("The Flash has been chosen.")