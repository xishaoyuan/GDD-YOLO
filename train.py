import warnings, os

warnings.filterwarnings('ignore')
from ultralytics import YOLO


if __name__ == '__main__':
    model = YOLO(r'E:\yolo\ultralytics-yolo11-20250301\ultralytics-20250301\yolo11-GlobalEdgeInformationTransfer.yaml')
    #model = YOLO('E:/yolo/ultralytics-yolo11-20250301/ultralytics-20250301/runs/train/exp2/weights/last.pt')
    # model.load('yolo11n.pt') # loading pretrain weights
    model.train(data=r'E:\yolo\ultralytics-yolo11-20250301\ultralytics-20250301\visdrone2019.yaml',
                cache=False,
                imgsz=640,
                epochs=300,
                batch=16,
                close_mosaic=0,
                workers=0, # Windows下出现莫名其妙卡主的情况可以尝试把workers设置为0
                # device='0,1', # 指定显卡和多卡训练参考<YOLOV11配置文件.md>下方常见错误和解决方案
                optimizer='SGD', # using SGD
                # patience=0, # set 0 to close earlystop.
                # resume=True, # 断点续训,YOLO初始化时选择last.pt
                # amp=False, # close amp | loss出现nan可以关闭amp
                # fraction=0.2,
                project='runs/train',
                name='exp',
                )