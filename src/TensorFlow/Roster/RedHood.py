import pyautogui as auto
import time

class RedHood():
    '''
        Classe para o personagem RedHood.
    '''

    def choose_me(self):
        auto.keyDown("right")
        time.sleep(0.3)
        auto.keyUp("right")
        time.sleep(0.5)

        

    def log(self):
        print("RedHood chosen.")

