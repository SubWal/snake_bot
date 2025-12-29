import pyautogui
import time


#games playable area


TOP_LEFT_X = 433   
TOP_LEFT_Y = 110  
BOARD_WIDTH = 1051
BOARD_HEIGHT = 926


REGION = (TOP_LEFT_X, TOP_LEFT_Y, BOARD_WIDTH, BOARD_HEIGHT)

# How many grid cells horizontally / vertically in Google Snake
GRID_W = 17  # try 17, 19, 21, etc
GRID_H = 15

TILE_WIDTH = BOARD_WIDTH // GRID_W
TILE_HEIGHT = BOARD_HEIGHT// GRID_H

def tile_to_image_center(col: int, row:int):

    """
    
    Convert a tile postion (col, row) to the pixel center(x,y) inside teh cropped board image. 

    """

    # col, row are 0- based : leftmost/topmost tile(0,0)

    x = int((col + 0.5) * TILE_WIDTH)
    y = int((row + 0.5) * TILE_HEIGHT)
    return x,y


def image_pixel_to_tile(x :int, y:int):
    """
    Conver an image pixel coordinate (x,y) back to a tile position(col, row).

    """

    col = x // TILE_WIDTH
    row = y // TILE_HEIGHT


def capture_board_image():
    """Take a screenshot of just the Snake board and return a Pillow Image."""
    img = pyautogui.screenshot(region=REGION)
    return img

def main ():

    pass

if __name__  == "__main" :
    main()
    capture_board_image()