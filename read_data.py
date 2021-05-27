import pydicom
import numpy as np
from PIL import Image
from matplotlib import pyplot

# 数据路径
file_path = r"C:\Users\孔啊吱\Desktop\kaggle_covid19\data\3dcdfc352a06.dcm"

# read_file
data0 = pydicom.read_file(file_path)
file_data = data0.pixel_array
print(file_data)
# dcmread
data1 = pydicom.dcmread(file_path)


# 借助numpy与PIL.Image
data = np.array(data0.pixel_array)

data_img = Image.fromarray(data0.pixel_array)
data_img_rotated = data_img.rotate(angle=45,resample=Image.BICUBIC)

# 绘图
pyplot.imshow(data0.pixel_array,cmap=pyplot.cm.bone)
pyplot.show()