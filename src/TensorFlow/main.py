from Roster.Aquaman import Aquaman
from Roster.Atom import Atom
from Roster.Atrocitus import Atrocitus
from Roster.Bane import Bane
from Roster.Batman import Batman
from Roster.BlackAdam import BlackAdam
from Roster.BlackManta import BlackManta
from Roster.BlackCanary import BlackCanary
from Roster.BlueBeetle import BlueBeetle
from Roster.Brainiac import Brainic
from Roster.Catwoman import Catwoman
from Roster.Cheetah import Cheetah
from Roster.Cyborg import Cyborg
from Roster.Darkseid import Darkseid
from Roster.Deadshot import DeadShot
from Roster.DoctorFate import DoctorFate
from Roster.Enchantress import Enchantress
from Roster.Firestorm import Firestorm
from Roster.GorillaGrodd import GorillaGrodd
from Roster.GreenArrow import GreenArrow
from Roster.GreenLantern import GreenLantern
from Roster.HarleyQuinn import HarleyQuinn
from Roster.Hellboy import Hellboy
from Roster.PoisonIvy import PoisonIvy
from Roster.Raiden import Raiden
from Roster.RedHood import RedHood
from Roster.Robin import Robin
from Roster.ScareCrow import ScareCrow
from Roster.Starfire import Starfire
from Roster.Subzero import Subzero
from Roster.Supergirl import Supergirl
from Roster.Superman import Superman
from Roster.SwampThing import SwampThing
from Roster.TheFlash import TheFlash
from Roster.TheJoker import TheJoker
from Roster.TMNT import TMNT
from Roster.WonderWoman import WonderWoman
from ML import ML
from test import test
import pyautogui as auto
import time

def ENTER():
    time.sleep(1)
    auto.keyDown("enter")
    time.sleep(0.3)
    auto.keyUp("enter")

def ROSTER(character):
    time.sleep(3.5)
    character.choose_me()
    select()

def PAUSE():
    auto.moveTo(700, 707)
    auto.moveTo(780, 707, 1, auto.easeInQuad)
    auto.doubleClick()
    auto.mouseDown()
    time.sleep(0.2)
    auto.mouseUp()

def select():
    auto.keyDown("esc")
    time.sleep(0.3)
    auto.keyUp("esc")
    time.sleep(1)

    auto.keyDown("left")
    time.sleep(0.3)
    auto.keyUp("left")
    time.sleep(0.5)

    auto.keyDown("left")
    time.sleep(0.3)
    auto.keyUp("left")
    time.sleep(0.5)

    auto.keyDown("enter")
    time.sleep(0.3)
    auto.keyDown("enter")

def select_tower():
    time.sleep(2)
    auto.keyDown("enter")
    time.sleep(0.3)
    auto.keyUp("enter")

def run_tower(character, size):
    select_tower()
    time.sleep(5)
    character.choose_me()
    select()
    character.log()
    for n in range(size):
        print("Battle " + str(n+1))
        auto.keyDown("enter")
        time.sleep(0.3)
        auto.keyUp("enter")
        time.sleep(5)
        auto.keyDown("enter")
        time.sleep(0.3)
        auto.keyUp("enter")

        auto.keyDown("enter")
        time.sleep(0.3)
        auto.keyUp("enter")

        time.sleep(100)

        time.sleep(1)
        auto.keyDown("enter")
        time.sleep(0.3)
        auto.keyUp("enter")
        time.sleep(1)
        auto.keyDown("enter")
        time.sleep(0.3)
        auto.keyUp("enter")
        time.sleep(1)
        auto.keyDown("enter")
        time.sleep(0.3)
        auto.keyUp("enter")

    # Rewards screen
    time.sleep(10)
    auto.keyDown("enter")
    time.sleep(0.3)
    auto.keyUp("enter")

    time.sleep(1)
    auto.keyDown("enter")
    time.sleep(0.3)
    auto.keyUp("enter")

    time.sleep(1)
    auto.keyDown("enter")
    time.sleep(0.3)
    auto.keyUp("enter")

    time.sleep(1)
    auto.keyDown("enter")
    time.sleep(0.3)
    auto.keyUp("enter")

    time.sleep(1)
    auto.keyDown("enter")
    time.sleep(0.3)
    auto.keyUp("enter")

def run_endless_tower(character):
    select_tower()
    time.sleep(5)
    character.choose_me()
    select()
    character.log()
    while(True):
        time.sleep(10)
        auto.keyDown("enter")
        time.sleep(0.3)
        auto.keyUp("enter")

def switch_roster(argument):
    switcher = {
        1: Aquaman(),
        2: Atom(),
        3: Atrocitus(),
        4: Bane(),
        5: Batman(),
        6: BlackAdam(),
        7: BlackCanary(),
        8: BlackManta(),
        9: BlueBeetle(),
        10: Brainiac(),
        11: Catwoman(),
        12: Cheetah(),
        13: Cyborg(),
        14: Darkseid(),
        15: Deadshot(),
        16: DoctorFate(),
        17: Enchatress(),
        18: Firestorm(),
        19: TheFlash(),
        20: GorillaGrodd(),
        21: GreenArrow(),
        22: GreenLantern(),
        23: HarleyQuinn(),
        24: Hellboy(),
        25: TheJoker(),
        26: PoisonIvy(),
        27: Raiden(),
        28: RedHood(),
        29: Robin(),
        30: ScareCrow(),
        31: Starfire(),
        32: Subzero(),
        33: Supergirl(),
        34: Superman(),
        35: SwampThing(),
        36: TMNT(),
        37: WonderWoman()
    }
    return switcher.get(argument, Superman())

def switch_action(argument, character):
    if argument == "ENTER_MULTIVERSE":
        ENTER()
    elif argument == "ENTER_IN_BATTLE":
        ENTER()
    elif argument == "ROSTER_BATMAN":
        ROSTER(character)
    elif argument == "PAUSE":
        PAUSE()
    elif argument == "REPEAT":
        ENTER()

def action(character, ml):
    time.sleep(3.5)
    auto.screenshot("img.jpg")
    switch_action(ml.predict(), character)

if __name__ == '__main__':
    
    print("1 - Aquaman\n2 - Atom\n3 - Atrocitus\n4 - Bane\n5 - Batman\n6 - Black Adam\n7 - Black Canary\
        \n8 - Black Manta\n9 - Blue Beetle\n10 - Brainiac\n11 - Catwoman\n12 - Cheetah\n13 - Cyborg\
        \n14 - Darkseid\n15 - Deadshot\n16 - Doctor Fate\n17 - Enchantress\n18 - Firestorm\n19 - The Flash\
        \n20 - Gorilla Grodd\n21 - Green Arrow\n22 - Green Lantern\n23 - Harley Quinn\n24 - Hellboy\n25 - The Joker\
        \n26 - Poison Ivy\n27 - Raiden\n28 - Red Hood\n29 - Robin\n30 - Scarecrow\n31 - Starfire\n32 - Sub-Zero\
        \n33 - Supergirl\n34 - Superman\n35 - Swamp Thing\n36 - TMNT\n37 - Wonder Woman")
    c = int(input())
    print("1 - Multiverse tower\n2 - Endless tower")
    o = int(input())
    ml = ML()
    character = switch_roster(c)
    while(True):
        if(o == 1):
            action(character,ml)
        else:
            run_endless_tower(character)
