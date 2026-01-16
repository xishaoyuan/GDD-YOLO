import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO(r'C:\Users\XiShaoyuan\Desktop\exp4\weights\best.pt') # 选择训练好的权重路径
    model.val(data=r'E:\yolo\ultralytics-yolo11-20250301\ultralytics-20250301\visdrone2019.yaml',
              split='val', # split可以选择train、val、test 根据自己的数据集情况来选择.
              imgsz=640,
              batch=16,
              # iou=0.7,
              # rect=False,
              save_json=True, # if you need to cal coco metrice
              project='runs/val',
              name='exp',
              )