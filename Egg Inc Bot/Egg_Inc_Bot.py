from pyautogui import *
import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api, win32con






def clickChickens(x, y):
    print('Clicking Chickens...')
    win32api.SetCursorPos((x,y))
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(np.random.uniform(13, 17))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def fastClick(x, y):
    win32api.SetCursorPos((x,y))
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(np.random.uniform(0.12, 0.3))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def Click(x, y):
    win32api.SetCursorPos((x,y))
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(np.random.uniform(0.2, 1.5))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


# Position of Accepting reward: 1264, 860
# Position of Egg Inc App Icon: 2220, 257
# Position of Collect Silos: 1251, 896
# Position of Egg Meter: 1249, 170 
#                        R 25 G 172 B 0  GREEN METER
#                        R 240, G 13, B 13 RED METER
#                        Position for Red Meter 1245, 361
#                        R 204, G 204, B 204
# Position of Accepting Package: 1264, 872                       
# Position of Hen Housing Capacity Meter: 1502, 378             RED  RGB 240, 13, 13        GREY 230, 230, 230
# Position of Shipping Depot Capacity Meter: 1500, 366          RED  RGB 240, 13, 13        GREY 230, 230, 230
# Position of Widescreen ad (Arrow): 2432, 83 
# Position of Red X to Cancel Contracts AFK Notification 1464, 480   RGB 240, 13, 13
# Position of Blue Button Go to Farm (Contracts): 1183, 847          RGB 39, 110, 198
# Position Ad widescreen arrows and X: 2430, 78
# Position of Ad X Widescreen: 2412, 137
def clickChickenButton():
    if pyautogui.pixel(1245, 170)[0] != 240:
        if pyautogui.pixel(1300, 170)[1] == 172:
            print('METER IS FULL')
            clickChickens(1264, 1284) #Position of Chicken Press Button
        elif pyautogui.pixel(1300, 170)[1] == 204:
            print('Chicken Meter Not Full Yet...')
        else:
            print('ClickChickenButton() Broke This Time...')
        

def adCheck():
    pass

'''

SILO AND CRASHING CHECK FUNCTIONS

GAME CRASH CALLS SILO CHECK BECAUSE IT DISPLAYS WHEN YOU LOG IN.

SILO CHECK WILL ALSO BE CALLED INSIDE OF CONTRACT CHECK FUNCTION


'''
def refillSiloCheck():
    if pyautogui.locateOnScreen('Images/Login_Refill_Silos.png', grayscale=True, confidence=0.7) != None: # If Found
        print('Re-Filling Silos...')
        fastClick(1260, 840)
    elif pyautogui.locateOnScreen('Images/Login_Refill_Silos.png', grayscale=True, confidence=0.7) == None: # If not found
        print('Silo Collect Not Found...')

def gameCrashCheck():
    print('Checking for Game Crash...')
    if pyautogui.locateOnScreen('Images/Egg_Inc_App_Icon.png', grayscale=False, confidence=0.7) != None:
        print('Game Crashed, Re-Launching Game...')
        fastClick(2220, 257)
        time.sleep(np.random.uniform(9, 13))
    # Run Silo Check after launching the crashed game.
    refillSiloCheck()




def droneCheck():
    print('Checking for Drones...')
    try:
        drone_img = pyautogui.locateOnScreen('Images/Drone1.png', region=(5, 144, 125 , 70), grayscale=True, confidence=0.3)
        drone_button = pyautogui.center(drone_img)
        x, y = drone_button
        fastClick(x,y)
        print('Clicking Drone')
    except TypeError:
        print('Exception Thrown, Drone Image Not Found')


def shippingDepotCheck():
    #1490, 530 Upgrade first car 
    # 172 G value
    # 1450, 517 Select Car to Upgrade
    # RGB FOR GREY is 127, 127, 127
    # 120 pixels y direction from each button
    # Y 1205 is botton of the menu
    # Shipping Depot X Button 1490, 238
    # Upgrade Vehicle X button 1450, 406
    # Urgent Notification OK BUTTON 1345, 760       RGB 39, 110, 198
    fastClick(1329, 888) # Click Shipping Depot
    time.sleep(np.random.uniform(0.1, 1))
    y = 530
    while y < 1205:
        time.sleep(np.random.uniform(1.25, 2))

        if pyautogui.pixel(1370, 365)[0] == 240: # if the end of the capacity meter is red
            if pyautogui.pixel(1490, y)[1] == 172: #Check the first car upgrade slot
                fastClick(1490, y)                  # Click the car upgrade button
                time.sleep(np.random.uniform(1.25, 2))
                print('Found Car Upgrade Button...')
                if pyautogui.pixel(1435, 500)[1] == 172: #First Car upgrade button is Green
                    print('Upgraded Car!!!')
                    fastClick(1440, 500) # Click car button
                    time.sleep(np.random.uniform(1, 2))
                    #fastClick(1489, 238) # Click x to leave Depot
                    print('Left the Depot...')
                elif pyautogui.pixel(1440, 500)[1] == 127: # If the button is grey (Cant afford upgrade)
                    fastClick(1450, 406) # Click the x button to close upgrade car menu
                else:
                    print('Cant buy a car at this time')
            else:
                print('Couldnt upgrade car')
        elif pyautogui.pixel(1500, 366)[0] == 230: # If the capacity meter is grey
            fastClick(1490, 238) # Click x Button Shipping Depot
        else:
            print('Shipping Depot Didnt need an extra car...')
            y = 5000
        y += 120

 
def habCheck():
    '''
    We are going to check the RGB value for each of the 4 meters that the hab has.

    ONCE I RESET AND PRESIIEGE ************** CHECK FOR THE FUCKING GREEN BUTTON FIRST!!!!!!!!!!!!!!!!!! ***********************

    Anyways... erm..

    If the RGB Value at the end of the meter is RED. Then we will press the upgrade button and grab the first available hab.
    
    
    '''

    #               ************* 127 RGB for GREY!!!!  ***************

    # Position of Build New Hen House:
    # TR 1390, 600
    # BR 1390, 980
    # BL 1120, 980

    fastClick(1300, 300) #Hab Location on Origin (0,0)
    time.sleep(np.random.uniform(1, 1.5))
    if pyautogui.pixel(1420, 375)[0] == 240:
        print('Hen Housing is at Critical!!!!!')


    if pyautogui.pixel(1200, 525)[0] == 240: # Top Left Meter
        fastClick(1180, 760) # Top Left Upgrade Button
        time.sleep(np.random.uniform(1.2, 2.2))
        if pyautogui.pixel(1420, 495)[1] == 172: # if the upgrade button next to the next house is available, click.
            fastClick(1420, 495)
            print('Fixed Hen Housing...')
            time.sleep(np.random.uniform(1, 2.2))
        else:
            fastClick(1440, 405)
            time.sleep(np.random.uniform(1, 2.2))
            fastClick(1490, 235)

    time.sleep(np.random.uniform(1, 2))

    if pyautogui.pixel(1200, 900)[0] == 240: # Bottom Left Meter
        fastClick(1180, 1140) # Bottom Left Upgrade Button
        time.sleep(np.random.uniform(1.25, 2.5))
        if pyautogui.pixel(1420, 495)[1] == 172:
            fastClick(1420, 495) # Upgraded house button
            print('Fixed Hen Housing...')
            time.sleep(np.random.uniform(1.5, 3.2))
        else:
            fastClick(1440, 405)
            time.sleep(np.random.uniform(1, 2.2))
            fastClick(1490, 235)
    elif pyautogui.pixel(1120, 980)[1] == 172: # IF ITS A NEW HAB
        fastClick(1120, 980)
        time.sleep(np.random.uniform(1, 2.2))


    time.sleep(np.random.uniform(1, 2))

    if pyautogui.pixel(1450, 525)[0] == 240: # Top Right Meter
        fastClick(1450, 760) # Upgrade Button
        time.sleep(np.random.uniform(1.25, 2.5))
        if pyautogui.pixel(1420, 495)[1] == 172:
            fastClick(1420, 495)
            print('Fixed Hen Housing...')
            time.sleep(np.random.uniform(1, 2.2))
        else:
            fastClick(1440, 405)
            time.sleep(np.random.uniform(1, 2.2))
            fastClick(1490, 235)

    time.sleep(np.random.uniform(1, 2))

    if pyautogui.pixel(1450, 900)[0] == 240: # Bottom Right Meter
        fastClick(1450, 1140) # Upgrade Button
        time.sleep(np.random.uniform(1.25, 2.5))
        if pyautogui.pixel(1420, 495)[1] == 172:
            fastClick(1420, 495)
            print('Fixed Hen Housing...')
            time.sleep(np.random.uniform(1, 2.2))
        else:
            fastClick(1440, 405)
            time.sleep(np.random.uniform(1, 2.2))
            fastClick(1490, 235)

    time.sleep(np.random.uniform(1, 2.2))
    if pyautogui.pixel(1422, 239)[2] == 198 and pyautogui.pixel(1098, 239)[2] == 198: 
                fastClick(1490, 235) # Leave Hen Housing
                print('Hen Housing Checked...')
    

def siloUpgradeCheck():
    if pyautogui.pixel(1080, 580)[0] == 129:
        fastClick(1080, 580)
        time.sleep(np.random.uniform(2, 3.2))
        if pyautogui.pixel(1150, 825)[1] == 172:
            fastClick(1150, 825)
            time.sleep(np.random.uniform(2, 3.2))
            fastClick(1490, 360)
            print('Upgraded Silos...')
        else:
            fastClick(1490, 360)
    else:
        fastClick(1080, 580)
        time.sleep(np.random.uniform(2, 3.2))
        if pyautogui.pixel(1150, 825)[1] == 172:
            fastClick(1150, 825)
            time.sleep(np.random.uniform(2, 3.2))
            fastClick(1490, 360)
            print('Upgraded Silos...')
        else:
            fastClick(1490, 360)
    print('Checked Silo Upgrades...')

 

'''
########################################################################################                       
                        
                        Notification Check

########################################################################################
'''
def packageCheck():
    pkg_img = pyautogui.locateOnScreen('Images/Package_IMG.png', grayscale=False, confidence=0.8)
    if pkg_img != None:
        print('Package Found...')
        pkg_button = pyautogui.center(pkg_img)
        x, y = pkg_button
        print('Clicking Package...')
        fastClick(x, y)
        # Find the Collect Pkg Button
        time.sleep(np.random.uniform(2, 4))
        fastClick(1264, 872) 
    elif pkg_img == None:
        print('Package Not Available to Grab...')


def contractNotifCheck():
    # Position of Red X to Cancel Contracts AFK Notification 1464, 480   RGB 240, 13, 13
    # Position of Blue Button Go to Farm (Contracts): 1183, 847          RGB 39, 110, 198
    #position Blustacks X Button to CLOSE: 2510, 15
    con_img = pyautogui.locateOnScreen('Images/ContractAFK_IMG.png', grayscale=False, confidence=0.75)
    if con_img != None:
        print('AFK Contract Found...')
        con_button = pyautogui.center(con_img)
        x, y = con_button
        print('Clicking Contract...')
        fastClick(x, y)
        # Find the Red X Button
        time.sleep(np.random.uniform(2, 4))
        fastClick(1464, 480) # RED X               ### CHANGE ME TO ACTUALLY GO TO CONTRACTS AND GET UPGRADES / REFILL SILOS ETC ###
    elif con_img == None:
        print('Contract Notification Not Available to Grab...')

def notificationCheck():
    contractNotifCheck()
    packageCheck()

'''
##################################################################################


                                 MAIN



###################################################################################



'''

def main():
    start_time = time.time()
    time.sleep(4)
    print('Executing Chicken Bot...')
    while keyboard.is_pressed('q') == False or time.time() - start_time >= 21600: # Q key is not being pressed
        gameCrashCheck() # Game Crash Check
        if pyautogui.locateOnScreen('Images/Desktop_CIF.png', grayscale=True, confidence=0.8) != None:
            print('BLUESTACKS CRASHED! SHUT DOWN BOT!!')
            break
        
        time.sleep(np.random.uniform(1.5, 4))
        clickChickenButton()
        #droneCheck()
        time.sleep(np.random.uniform(0.2, 1.75))
        notificationCheck()
        time.sleep(np.random.uniform(2, 4.5))
        #shippingDepotCheck()   #CHANGE ME TO IF STATEMENT FOR HOUSE IMAGE TOP LEFT CLICK
        time.sleep(np.random.uniform(0.1, 2))

        # Accidental Menu Click
        if pyautogui.pixel(1422, 239)[2] == 198 and pyautogui.pixel(1098, 239)[2] == 198: 
                fastClick(1490, 238)
        elif pyautogui.pixel(1100, 370)[2] == 198 and pyautogui.pixel(1400, 239)[2] == 198:
                fastClick(1492, 362)
        elif pyautogui.pixel(1450, 240)[0] == 134: # RGB 134 0 196 Purple Button Chicken Upgrades
                fastClick(1510, 218) # Click red X on the Upgrade Tree
        else:
            print('Bot Didnt do an oopsies')
        #time.sleep(np.random.uniform(1, 1.5))
        #habCheck()     #RE ENABLE ONCE ITS FIXED
        #time.sleep(np.random.uniform(1, 2))
        #siloUpgradeCheck()
        #time.sleep(np.random.uniform(1, 1.5))
        # Print Closing Bot
        if time.time() - start_time >= 21600:
            print("Ive ran for too long...")
            fastClick(2510, 15)
            break
        if keyboard.is_pressed('q') == True:
            print('Shutting Down Chicken Bot...')
        
if __name__ == '__main__':
    main()

    


