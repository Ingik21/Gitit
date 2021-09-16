
from types import WrapperDescriptorType


N = North
W = West
S = South
E = East

def location():
    tile_1_1 = North
    tile_1_2 = North, South, East
    tile_1_3 = South, East
    tile_2_1 = North
    tile_2_2 = South, West
    tile_2_3 = East, West
    tile_3_3 = South, West 
    tile_3_2 = North, South
    tile_3_3 = Victory
