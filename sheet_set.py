""" This is to make a file structure for creating sheet sets easily """

import os


# List all Scenic Elements in this List
ARR = ["Bed", "Bucket Shack", "Candy Counter", "Candy Shop Wagon", "Chocolate Wagon",
       "Ground Plan", "Elevator", "Factory",
       "Factory Gates", "Mixing Wagon", "Nut Wagon",
       "Office_Corridor", "Oompa Hanger", "Oompa Wagon", "Pipe", "Portal 1", "Portal 2", "Portal 3",
       "Portal 4", "Pro Details",
       "TV Panels", "TV Room Portal", "Wonka Boat", "Wonka Water"]

# Loop through Array of scenic elements and create directory path for each element
for item in ARR:
    # Make sure to change this path to exactly where you want sheet set saved
    PATH = 'C:/Users/crazy/OneDrive - ABT Performing Arts Association, Inc/Production/S19 Working Show Files/4. Charlie and the Chocolate Factory/Scenic/Shop Internal/Drafting/Sheet Set'
    os.makedirs(PATH + '/' + item + '/plates')
