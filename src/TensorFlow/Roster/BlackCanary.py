import pyautogui as auto
import time

class BlackCanary():
    '''
        Classe para o personagem BlackCanary.
    '''

    def choose_me(self):
        auto.keyDown("down")
        time.sleep(0.3)
        auto.keyUp("down")
        time.sleep(0.5)
        

    def log(self):
        print("BlackCanary chosen.")

