#pack SimpTrain
import simpTrain



# - Description:
# - - This package provides basic, easy use machine learning and visual recognition functionalities. Including visual recognition object determination, handwriting text recognition, and more.



# - Documents:


# - Visual recognition:
#from simpTrain import vision
#vision.train()
#vision.predict(".\\pics\\testApple01.png")


# - Handwriting recognition:
results = simpTrain.handwriting.predict(".\\testPics\\testCarpetHandwriting.png")

print("results: ", results)
