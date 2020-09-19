#pack SimpTrain
import simpTrain

# - Description:
# - - This package provides basic, easy use machine learning and visual recognition functionalities. Including visual recognition object determination, handwriting text recognition, and more.

# - Documents:
# - Visual recognition
from simpTrain import vision

vision.train()

p = vision.predict(".\\testApple01.png")

print(p)
