import cv2
import matplotlib.pyplot as plt
from paddleocr import PaddleOCR

# 初始化OCR模型
ocr = PaddleOCR()

# 加载图片
img = cv2.imread('test.png')

# 进行OCR识别
result = ocr.ocr(img)

# 输出识别结果
for line in result:
    print(line)

# 可视化识别结果
boxes = [line[0] for line in result]
scores = [line[1] for line in result]
texts = [line[2][0] for line in result]
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.axis('off')
plt.show()