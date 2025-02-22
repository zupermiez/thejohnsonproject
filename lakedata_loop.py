from lakedata_save_newfile import saveandprocess
import time

#starting coordinates
left, bottom, right, top = 24.875, 60.0, 25.0, 60.125

# Initialize loop counters
i = 0  #right-left movement
j = 0  #top-bottom movement

while True:
    # Update right and left coordinates
    newright = right - (i / 8)
    newleft = left - (i / 8)

    print("////////////////////////////////////////////////////////////////////////////////////////")
    print(f"Going LEFT: now round {i} at {newleft, bottom, newright, top}")
    j = 0

    while True:
        # Update top and bottom coordinates
        newtop = top + (j / 8)
        newbottom = bottom + (j / 8)
        print(f"Going UP now round {j} at {newleft, newbottom, newright, newtop} ")
        saveandprocess(newleft, newbottom, newright, newtop)
        time.sleep(2)
        j += 1
        if newtop >= 70:
            break

    i += 1
    if newright <= 23:
        break


'''
log
DONE 
60.125, 60.0, 25.125, 25.0 - 69.625, 69.5, 25.125, 25.0
60.125, 60.0, 25.25, 25.125 - all the way
60.125, 60.0, 25.5, 25.25 - all the way oops did too big
60.125, 60.0, 25.625, 25.50 - easy now loop works just takes forever
61.5, 61.375, 27.125, 27.0

60.125, 60.0, 27.25, 27.125 MISSING THIS IS STUCK ON ROUND 11

60.125, 60.0, 27.375, 27.25 - 69.0, 68.875, 27.375, 27.25) DONE
60.125, 60.0, 27.625, 27.5 DONE
60.125, 60.0 28.125, 28.0) DONE
API IS RATSHIT UP UNTIL 63.375 AND FROM 69.2 upwards
60.635, 60.5, 28.875, 28.75 DONE
60.635, 60.5, 29.625, 29.5 until this done this not
60.635, 60.5, 29.75, 29.625 until this done this not
boom until 30
'''
