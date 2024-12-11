
from ultralytics import YOLO
from ultralytics.utils.torch_utils import model_info
import cv2
model = YOLO('../yolo-weights/yolov8l.pt') #weitghts
results = model("images1/img4.png", show=True ) #show=true for show image
cv2.waitKey(0) #delay image time
