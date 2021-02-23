import pyautogui as auto
import time

class Superman():
    '''
        Classe para o personagem Superman.
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

    def log(self):
        print("Superman chosen.")

