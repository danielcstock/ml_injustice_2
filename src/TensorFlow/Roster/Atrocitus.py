import pyautogui
import time

class Atrocitus():
    '''
        Classe para o personagem Atrocitus.
    '''

    def choose_me(self):
        pyautogui.hotkey("right")
        time.sleep(0.7)
        pyautogui.hotkey("right")
        time.sleep(0.7)
        pyautogui.hotkey("right")
        time.sleep(0.7)
        
    def log(self):
        print("Atrocitus has been chosen.")