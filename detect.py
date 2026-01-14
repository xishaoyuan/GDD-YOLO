import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO



if __name__ == '__main__':
    model = YOLO(r'E:\yolo\ultralytics-yolo11-20250301\ultralytics-20250301\yolo11n.pt') # select your model.pt path
    model.predict(source=r'C:\Users\XiShaoyuan\Desktop\1.jpg',
                  imgsz=640,
                  project=r'E:\yolo\ultralytics-yolo11-20250301\ultralytics-20250301\runs\detect',
                  name='exp',
                  save=True,
                  # conf=0.2,
                  # iou=0.7,
                  # agnostic_nms=True,
                  # visualize=True, # visualize model features maps
                  line_width=2, # line width of the bounding boxes
                  show_conf=False, # do not show prediction confidence
                  show_labels=False, # do not show prediction labels
                  # save_txt=True, # save results as .txt file
                  # save_crop=True, # save cropped images with results
                )