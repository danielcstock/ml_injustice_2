import pyautogui as auto
import time

class GreenLantern():
    '''
        Classe para o personagem GreenLantern.
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

        

    def log(self):
        print("GreenLantern chosen.")

