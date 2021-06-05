import pydicom
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 数据路径
file_path = r"C:\Users\孔啊吱\Desktop\kaggle_covid19\data\f6293b1c49e2.dcm"

# read_file
# data0 = pydicom.read_file(file_path)
# file_data = data0.pixel_array
# print(file_data)
# dcmread
data0 = pydicom.dcmread(file_path)
file_data = data0.pixel_array



# 借助numpy与PIL.Image
data = np.array(data0.pixel_array)

data_img = Image.fromarray(data0.pixel_array)
data_img_rotated = data_img.rotate(angle=45,resample=Image.BICUBIC)

# 绘图
fig, ax = plt.subplots(figsize=(10, 8))
# ax.imshow(img, cmap="gray")
plt.imshow(data0.pixel_array,cmap=plt.cm.bone)
# 划定矩形
# rect1 = patches.Rectangle((666.21393, 1160.51975),1030.91449 ,742.0592, linewidth=1.5, edgecolor='r', facecolor='none')
# rect2 = patches.Rectangle((2135.39156, 1359.73028),515.45728,443.24341,linewidth=1.5, edgecolor='r', facecolor='none')
# ax.add_patch(rect1)
# ax.add_patch(rect2)
plt.show()