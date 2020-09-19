import cv2 as cv
import sys

faces = 0


def num_faces(image_path):
    original_image = cv.imread(image_path)
    grayscale_image = cv.cvtColor(original_image, cv.COLOR_BGR2GRAY)
    face_cascade = cv.CascadeClassifier('haarcascade_frontalface_alt.xml')
    detected_faces = face_cascade.detectMultiScale(grayscale_image)
    faces = len(detected_faces)


if __name__ == "__main__":
    num_faces(sys.argv[1])
