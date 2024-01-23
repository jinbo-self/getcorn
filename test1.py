from PIL import Image
import numpy as np
from ultralytics import YOLO

# 加载模型
if __name__ == '__main__':
    # model = YOLO("yolov8n.yaml")  # 从头开始构建新模型
    model = YOLO("best.pt")  # 加载预训练模型（建议用于训练）

    # 使用模型
    # model.train(data="game.yaml", epochs=100,batch=100)  # 训练模型
    # metrics = model.val()  # 在验证集上评估模型性能
    results = model("D:\\mrzhuge\\HACK_COIN\\crypto_unicorns\\datasets\\game_data\\images\\test\\18.jpg")  # 对图像进行预测
    print(len(results))
    for r in results:
        boxes = r.boxes  # Boxes object for bbox outputs
        for box in boxes:
            print("坐标:", np.array(box.xyxy.cpu())[0], "类别序号:", int(np.array(box.cls.cpu())[0]), "类别:",
                  r.names[int(np.array(box.cls.cpu())[0])])

        im_array = r.plot()  # plot a BGR numpy array of predictions
        im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
        im.show()  # show image
        im.save('results.jpg')  # save image

