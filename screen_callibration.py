import pyautogui
import time 

def get_point(message:str)  :
    "ask user to position the mouse in specified corner of the screen"

    print()
    print(message)
    print('You have about 5 seconds to move the mouse and then I will grab its position')

    time.sleep(5)
    x,y = pyautogui.position()
    print(f"Captured Position: x = {x}, y = {y}")
    return x,y


def main():
    pyautogui.FAILSAFE = True

    print("Callibration of Google Snake Board")

    #get top-left corner of the board 

    x1,y1 = get_point("Move your mouse ot the TOP-LEFT corcer of teh Snake board(inside the boarder)")

    # bet the bottom right corner of the board

    x2,y2 = get_point("MOve your mouse to the BOTTOM-RIGHT of the Snake board inside the border")


    print()
    print("Callibration Complete!")

    print(f" TOP_LEFT = ({x1}, {y1})")

    print(f"Bottom-Right = ({x2},{y2})")


    width = x2 - x1 
    height = y2 - y1

    print(f"Board_left = {x1} \n Board_top = {y1} \n width = {width}\n  height = {height}")



if __name__ == "__main__":
    main()
