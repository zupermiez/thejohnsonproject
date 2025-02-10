from lakedata_save_newfile import saveandprocess
import time


#starting coordinates
north, south, east, west = 60.125, 60.0, 25.75, 25.625

for i in range(31):
    neweast, newwest = (east + (i / 8)), (west + (i / 8))
    print("###############################GOING RIGHT#################################################################")
    print(f"#######################NEW COORDS {i} at {north, south, neweast, newwest} ######################################################")

    for j in range(80):
        newnorth, newsouth = (north + (j / 8)), (south + (j / 8))
        print("/////////////////////////////////GOING UP///////////////////////////////////////////////////////////////")
        print( f"////////////// STARTING ROUND {j} at {newnorth, newsouth, neweast, newwest} /////////////////////////////////////////////////////")
        print("////////////////////////////////////////////////////////////////////////////////////////////////////////")

        saveandprocess(newnorth, newsouth, neweast, newwest)
        time.sleep(2)

'''
log
DONE 
60.125, 60.0, 25.125, 25.0 - 69.625, 69.5, 25.125, 25.0
60.125, 60.0, 25.25, 25.125 - all the way
60.125, 60.0, 25.5, 25.25 - all the way oops did too big
60.125, 60.0, 25.625, 25.50 - easy now loop works just takes forever
61.5, 61.375, 27.125, 27.0

NEXT TO SCAN
61.5, 61.375, 27.25, 27.125


'''