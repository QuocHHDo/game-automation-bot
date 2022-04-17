from PIL.ImageOps import grayscale
from pyautogui import * 
import pyautogui
import time 
import keyboard
import numpy as np 
import random 
#import win32api, win32con 
import win32api, win32con
#import pywin32
import sys, os
import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('250x500')
        self.title('Automation Bot')

        first_label = tk.Label(self, text = "Educational Bot Project V2.0", font=10)  
        first_label.pack(pady=2, padx=2)

        full_auto_button = tk.Button(self, text = "FULL AUTO", command = full_auto)
        full_auto_button.pack(pady=5, padx=5)

        all_auto_1_button = tk.Button(self, text = "All Auto 1", command = all_auto_1)
        all_auto_1_button.pack(pady=5, padx=5)

        reset_button = tk.Button(self, text = "Reset", command = reset)
        reset_button.pack(pady=5, padx=5)

        help_button = tk.Button(self, text = "Auto Help", command = auto_help)
        help_button.pack(pady=5, padx=5)

        recruit_button = tk.Button(self, text = "Auto Recruit", command = auto_recruit)
        recruit_button.pack(pady=5, padx=5)

        prod_button = tk.Button(self, text = "Auto Production", command = auto_prod)
        prod_button.pack(pady=5, padx=5)

        terr_button = tk.Button(self, text = "Auto Territory", command = auto_territory)
        terr_button.pack(pady=5, padx=5)

        expedition = tk.Button(self, text = "Auto Expedition", command = auto_expedition)
        expedition.pack(pady=5, padx=5)
        
        vip = tk.Button(self, text = "Auto VIP", command = auto_vip)
        vip.pack(pady=5, padx=5)

        pvp = tk.Button(self, text = "Auto 'PVP'", command = auto_PVP)
        pvp.pack(pady=5, padx=5)

        train = tk.Button(self, text = "Auto Train", command = auto_train)
        train.pack(pady=5, padx=5)

        clickTest = tk.Button(self, text = "Click Test", command = click_test)
        clickTest.pack(pady=5, padx=5)

        # Auto Barb 
        # Auto Farm 

def resource_path(relative_path):
        """ Get the absolute path to the resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

def show_window():
    windowLocation = pyautogui.locateOnScreen('Images\Window.png', grayscale=True, confidence=0.6)
    if windowLocation != None: 
        window_x, window_y = pyautogui.center(windowLocation);
        leftClick(window_x, window_y)
    time.sleep(0.3) 

def click(x,y):
    win32api.SetCursorPos((x,y)) 
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)   

    print("Clicked at: " + str(x) + "," + str(y))

def leftClick(x,y):
    pyautogui.moveTo(x,y)
    pyautogui.mouseDown()
    time.sleep(0.5) #or whatever you need, if even needed
    pyautogui.mouseUp()
    print("Clicked at: " + str(x) + "," + str(y))


def reset(): 
    time.sleep(0.3)
    castleButtonLocation = pyautogui.locateOnScreen('./Images/CastleButton.png', grayscale=True, confidence=0.6)
    if castleButtonLocation != None: 
        click(136,955)

    time.sleep(0.3) 
    # Click on bottom left button 
    click(136,955)

    time.sleep(0.3)
    # click on bottom left button again
    click(136,955)

    time.sleep(0.6)
    # Check if menu bar is not present 
    menuLocation = pyautogui.locateOnScreen('./Images/menubar.png', grayscale=True, confidence=0.6)
    if menuLocation == None: 
        # Click on button to display menu
        click(1762,974)

def auto_help():
    helpLocation = pyautogui.locateOnScreen('Images\Help.png', grayscale=True, confidence=0.6)
    if helpLocation != None: 
        help_x, help_y = pyautogui.center(helpLocation)
        leftClick(help_x, help_y)
    time.sleep(0.3) 

def auto_recruit(): 
    time.sleep(0.3)
    # Check if Recruit is available 
    #if pyautogui.pixel(443, 393)[0] == 174: 
    recruitLocation = pyautogui.locateOnScreen('./Images/Recruit.png', grayscale=True, confidence=0.2)
    if recruitLocation != None:
        # Click on Tavern 
        click(504, 523)

        time.sleep(0.3)
        # Click on Recruit Button 
        click(693, 698)

        time.sleep(2)
        # Check if Silver Chest is available
        if pyautogui.pixel(414, 849)[0] == 0: 
            print("Silver Chest Test")
            time.sleep(0.3) 
            # Click on Silver Chest Button 
            click(414, 849) 

            time.sleep(4) 
            # Click on Confirm Button  # 10+ keys
            click(356, 892)
        
        # Check if Golden Chest is available
        if pyautogui.pixel(857, 874)[0] == 0: 

            time.sleep(0.3) 
            # Click on Golden Chest Button
            click(857, 874) 

            time.sleep(4) 
            # Click on Confirm Button # < 10 keys 
            click(470, 877)

        # Check if Equipment Chest is available 
        if pyautogui.pixel(1382, 863)[0] == 0: 
            
            time.sleep(0.3)
            # Click on Equipment Chest Button
            click(1382, 863) 

            time.sleep(4) 
            # Click on Confirm Button # < 10 keys 
            click(487, 901) 
        
        time.sleep(1) 
        # Close Recruit Window 
        click(81, 87) 

def auto_prod():
    print("Test")

    # Check if Gold Production is ready to be collected
    goldProdLocation = pyautogui.locateOnScreen(resource_path('Images\Gold.png'), grayscale=True, confidence=0.8)
    #if pyautogui.pixel(1198,880)[0] == 235: 
    #if pyautogui.locateOnScreen('Gold.png', grayscale=True, confidence=0.8) != None:
    if goldProdLocation != None: 
        # Collect Gold Production
        #click(1198,880)
        gold_x, gold_y = pyautogui.center(goldProdLocation)
        leftClick(gold_x, gold_y)
    time.sleep(0.3)

    # Check if Food Production is ready to be collected
    foodProdLocation = pyautogui.locateOnScreen(resource_path('Images\Food.png'), grayscale=True, confidence=0.8)
    #if pyautogui.pixel(1330,795)[0] == 229: 
    if foodProdLocation != None:

        # Collect Farm Production
        #click(1330,795)
        food_x, food_y = pyautogui.center(foodProdLocation)
        leftClick(food_x, food_y) 

    time.sleep(0.3)

    # Check if Wood Production is ready to be collected
    woodProdLocation = pyautogui.locateOnScreen(resource_path('Images\Wood.png'), grayscale=True, confidence=0.8)
    #if pyautogui.pixel(963,360)[0] == 225: 
    if woodProdLocation != None:

        #Collect Wood Production 
        #click(963,360) 
        wood_x, wood_y = pyautogui.center(woodProdLocation)
        leftClick(wood_x, wood_y) 

    time.sleep(0.3)

    # Check if Stone Production is ready to be collected
    stoneProdLocation = pyautogui.locateOnScreen(resource_path('Images\Stone.png'), grayscale=True, confidence=0.8)
    #if pyautogui.pixel(875,905)[2] == 232:
    if stoneProdLocation != None:
        # Collect Stone Production 
        #click(875,905)
        stone_x, stone_y = pyautogui.center(stoneProdLocation)
        leftClick(stone_x, stone_y)

def auto_territory():
    time.sleep(0.3)
    
    # Click on Alliance Button 
    click(1488,961)

    time.sleep(0.3) 
    # Click on Territory Button
    click(1286,598)

    time.sleep(0.3)
    # Click on Claim Button
    click(1469,224)

    time.sleep(0.5)
    # Click on Exit Button
    click(1605,93)

    time.sleep(0.5)
    # Click on Exit #2 Button
    click(1605,93)

def auto_expedition():
    # Click on Campaign Button
    campaignLocation = pyautogui.locateOnScreen('Images\Campaign.png', grayscale=True, confidence=0.6)
    if campaignLocation != None:
        campaign_x, campaign_y = pyautogui.center(campaignLocation)
        leftClick(campaign_x, campaign_y)
    time.sleep(0.3)

    # Click on Expedition Button
    expeditionLocation = pyautogui.locateOnScreen('Images\Expedition.png', grayscale=True, confidence=0.6)
    if expeditionLocation != None:
        expedition_x, expedition_y = pyautogui.center(expeditionLocation)
        leftClick(expedition_x, expedition_y)
    time.sleep(0.3)

    # Click on Expedition Chest Button
    expeditionChestLocation = pyautogui.locateOnScreen('Images\ExpeditionChest.png', grayscale=True, confidence=0.6)
    if expeditionChestLocation != None:
        expeditionChest_x, expeditionChest_y = pyautogui.center(expeditionChestLocation)
        leftClick(expeditionChest_x, expeditionChest_y)
    time.sleep(0.3)

    # Click on Expedition Confirm Button
    expeditionConfirmLocation = pyautogui.locateOnScreen('Images\ExpeditionConfirm.png', grayscale=True, confidence=0.6)
    if expeditionConfirmLocation != None:
        expeditionConfirm_x, expeditionConfirm_y = pyautogui.center(expeditionConfirmLocation)
        leftClick(expeditionConfirm_x, expeditionConfirm_y)
    time.sleep(0.3)
    
    # Click on Expedition Exit Button
    campaignExitLocation = pyautogui.locateOnScreen('Images\CampaignExit.png', grayscale=True, confidence=0.6)
    if campaignExitLocation != None:
        campaignExit_x, campaignExit_y = pyautogui.center(campaignExitLocation)
        leftClick(campaignExit_x, campaignExit_y)
    time.sleep(0.3)

    # Under Construction

    # # Click on Sunset Button
    # sunsetLocation = pyautogui.locateOnScreen('Images\Sunset.png', grayscale=True, confidence=0.6)
    # if sunsetLocation != None:
    #     sunset_x, sunset_y = pyautogui.center(sunsetLocation)
    #     leftClick(sunset_x, sunset_y)
    # time.sleep(0.3)

    # # Click on Sunset Challenge Button
    # sunsetChallengeLocation = pyautogui.locateOnScreen('Images\SunsetChallenge.png', grayscale=True, confidence=0.6)
    # if sunsetChallengeLocation != None:
    #     sunsetChallenge_x, sunsetChallenge_y = pyautogui.center(sunsetChallengeLocation)
    #     leftClick(sunsetChallenge_x, sunsetChallenge_y)
    # time.sleep(0.3)

    # zeroAttemptLocation = pyautogui.locateOnScreen('Images\ZeroAttempt.png', grayscale=True, confidence=0.6)
    
    # # Check if Zero Attempt is NOT shown
    # while zeroAttemptLocation == None:
    #     # Click on Sunset Challenge Button
    #     if sunsetChallengeLocation != None:
    #         sunsetChallenge_x, sunsetChallenge_y = pyautogui.center(sunsetChallengeLocation)
    #         leftClick(sunsetChallenge_x, sunsetChallenge_y)
    #     time.sleep(0.3)
    #     # Click on OK Button
    #     okLocation = pyautogui.locateOnScreen('Images\OK.png', grayscale=True, confidence=0.6)
    #     if okLocation != None:
    #         ok_x, ok_y = pyautogui.center(okLocation)
    #         leftClick(ok_x, ok_y)
    #     time.sleep(0.3)

    #     # Click anywhere on the screen
    #     leftClick(500,500)
    #     time.sleep(0.3)
    # # If Zero Attempt is shown
    # if zeroAttemptLocation != None: 
    #     zeroAttempt_x, zeroAttempt_y = pyautogui.center(zeroAttemptLocation)
    # time.sleep(0.3)

def auto_vip():
    vipIconLocation = pyautogui.locateOnScreen(resource_path('Images\VIP.png'), grayscale=True, confidence=0.8)
    if vipIconLocation != None:
        vip_x, vip_y = pyautogui.center(vipIconLocation)
        leftClick(vip_x, vip_y)
    time.sleep(0.3)

    vipClaim1Location = pyautogui.locateOnScreen(resource_path('Images\VIPClaim1.png'), grayscale=True, confidence=0.8)
    if vipClaim1Location != None:
        vip_x, vip_y = pyautogui.center(vipClaim1Location)
        leftClick(vip_x, vip_y)
    time.sleep(4) 
    # Click anywhere on application
    leftClick(500,500) 

    vipClaim2Location = pyautogui.locateOnScreen(resource_path('Images\VIPClaim2.png'), grayscale=True, confidence=0.8)
    if vipClaim2Location != None:
        vip_x, vip_y = pyautogui.center(vipClaim2Location)
        leftClick(vip_x, vip_y)
    time.sleep(0.3)
    # Click anywhere on application
    leftClick(500,500)
    time.sleep(0.3)

    # Exit out of VIP Window
    vipExitLocation = pyautogui.locateOnScreen(resource_path('Images\VIPExit.png'), grayscale=True, confidence=0.8)
    if vipExitLocation != None:
        vip_x, vip_y = pyautogui.center(vipExitLocation)
        leftClick(vip_x, vip_y)
    time.sleep(0.3)

# Still needs to be worked on 
def auto_PVP():
    time.sleep(0.3)

    # Click on Expedition Button
    click(1206,964)
    
    time.sleep(0.3)
    # Click on PVP Button
    click(1148,468)

    time.sleep(1)
    # Click on Challenge Button
    click(920,948)

    time.sleep(1)
    # Keeps challenging until no more attempts
    attemptsLocation = pyautogui.locateOnScreen('./Images/attempts.png', grayscale=True, confidence=0.8)
    while attemptsLocation == None: 
        print("Available attempts")
        click(1361,881)

        time.sleep(5)
        # Click OK Button
        click(941, 945)

        time.sleep(2)
        # Click to continue 
        click(941,945)
    # If no more attempts
    time.sleep(0.5)
    print("No more attempts")
    # Exit out of window
    click(1602,88)

    time.sleep(0.3)
    # Exit out of window #2 
    click(98,103)

    time.sleep(0.5)
    # Exit out of window #3
    click(98,103) 

def auto_train():
    time.sleep(0.5)

# Siege
    # Click on siege's building
    click(1338,673)

    time.sleep(0.3) 
    #Click on siege's building again 
    click(1338, 673)

    time.sleep(0.3)
    # Click on train siege button 
    siegeTrainLocation = pyautogui.locateOnScreen('./Images/TrainSiege.png', grayscale=True, confidence=0.8)
    if siegeTrainLocation != None: 
        print("It sees siegeTrain button")
        
        time.sleep(0.3)
        # Click on Siege Train Button
        siege_x, siege_y = pyautogui.center(siegeTrainLocation)
        click(siege_x, siege_y)

        time.sleep(0.3)
        print("Checking")
        # Check if Train Button exist 
        trainButtonLocation = pyautogui.locateOnScreen('./Images/TrainButton.png', grayscale=True, confidence=0.8)
        if trainButtonLocation != None: 
            print("It sees train button")
            train_x, train_y = pyautogui.center(trainButtonLocation) 
            click(train_x, train_y)
        # Train Button does not exist
        else: 
            # Exit out of Siege Window 
            time.sleep(0.3)
            click(1585,148)

    # Calvary 
        time.sleep(0.3) 
        # Click on calvary's building
        click(1691,381) 

        time.sleep(0.3)
        # Click on calvary's building again
        click(1691,381) 

        time.sleep(0.3) 
        # Click on train calvary button
        calvaryTrainLocation = pyautogui.locateOnScreen('./Images/TrainCalv.png', grayscale=True, confidence=0.6)
        if calvaryTrainLocation != None: 
            
            time.sleep(0.3)
            # Click on Calvary Train Button
            calv_x, calv_y = pyautogui.center(calvaryTrainLocation)
            click(calv_x, calv_y) 

            time.sleep(0.3)
            # Check if Train Button exist
            trainButtonLocation = pyautogui.locateOnScreen('./Images/TrainButton.png', grayscale=True, confidence=0.8)
            if trainButtonLocation != None: 
                print("It sees train button")
                train_x, train_y = pyautogui.center(trainButtonLocation) 
                click(train_x, train_y)
            # Train Button does not exist
            else: 
                # Exit out of Calvary Window
                print("It does not see train button")
                time.sleep(0.3)
                click(1585, 148)


    # Infantry
    time.sleep(0.3)

    # Click on infantry's building
    click(1276,258) 

    time.sleep(0.3)
    # Click on infantry's building again
    click(1276,258)  

    time.sleep(0.3)
    # Click on train infantry button 
    infantryTrainLocation = pyautogui.locateOnScreen('./Images/TrainInfantry.png', grayscale=True, confidence=0.6)
    if infantryTrainLocation != None: 

        time.sleep(0.3)
        # Click onm Infantry Train Button
        infantry_x, infantry_y = pyautogui.center(infantryTrainLocation)
        click(infantry_x, infantry_y) 

        time.sleep(0.3)
        # Check if Train Button exist 
        trainButtonLocation = pyautogui.locateOnScreen('./Images/TrainButton.png', grayscale=True, confidence=0.8)
        if trainButtonLocation != None: 
            print("It sees train button")
            train_x, train_y = pyautogui.center(trainButtonLocation) 
            click(train_x, train_y)
        # Train Button does not exist
        else: 
            # Exit out of Calvary Window
            print("It does not see train button")
            time.sleep(0.3)
            click(1585, 148)
    # Archer 
    time.sleep(0.3)

    # Click on archer's building
    click(1325,687)

    time.sleep(0.3)
    # Click on archer's building again
    click(1325,687)

    time.sleep(0.3) 
    # Click on train archer button 
    archerTrainLocation = pyautogui.locateOnScreen('./Images/TrainArcher.png', grayscale=True, confidence=0.8)
    if archerTrainLocation != None: 
        
        time.sleep(0.3) 
        # Click on Archer Train Button
        archer_x, archer_y = pyautogui.center(archerTrainLocation)
        click(archer_x, archer_y) 

        time.sleep(0.3) 

        # Check if Train Button exist
        trainButtonLocation = pyautogui.locateOnScreen('./Images/TrainButton.png', grayscale=True, confidence=0.8)
        if trainButtonLocation != None: 
            print("It sees train button")
            train_x, train_y = pyautogui.center(trainButtonLocation) 
            click(train_x, train_y)
        # Train Button does not exist
        else: 
            # Exit out of Calvary Window
            print("It does not see train button")
            time.sleep(0.3)
            click(1585, 148)

def all_auto_1():
    print("Running All Auto 1")
    reset() 
    auto_help()
    auto_prod()
    auto_territory()
    auto_train()
    # Reset for auto_recruit to work
    reset()
    auto_recruit()
    print("End of All Auto 1")

def full_auto():
    all_auto_1()
    auto_vip()
    auto_expedition()
    auto_PVP()

app = Application()
app.mainloop()