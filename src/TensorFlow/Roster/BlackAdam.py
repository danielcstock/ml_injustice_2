import pyautogui as auto
import time

class BlackAdam():
    '''
        Classe para o personagem BlackAdam.
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
        
        auto.keyDown("down")
        time.sleep(0.3)
        auto.keyUp("down")
        time.sleep(0.5)
        

    def log(self):
        print("BlackAdam chosen.")

