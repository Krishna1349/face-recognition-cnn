from imutils.video import VideoStream
import face_recognition
import argparse
import imutils
import pickle
import time
import cv2

print("[INFO] quantifying faces...")
imagePaths = list(paths.list_images(args["dataset"]))
