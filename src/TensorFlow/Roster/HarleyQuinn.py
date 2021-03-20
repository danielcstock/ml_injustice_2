import pyautogui as auto
import time

class HarleyQuinn():
    '''
        Classe para o personagem HarleyQuinn.
    '''

    def choose_me(self):
        auto.keyDown("left")
        time.sleep(0.3)
        auto.keyUp("left")

    def log(self):
        print("HarleyQuinn chosen.")

