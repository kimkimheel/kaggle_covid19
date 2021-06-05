import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

study_data = pd.read_csv(open(r'C:\Users\孔啊吱\Desktop\kaggle_covid19\data\csv_file\train_study_level.csv'))

# 提取数据各列列名，统计各类型数量
result_type = list(study_data.columns)[1:]
type_count_dict = dict()
for each in result_type:
    type_count_dict[each] = study_data[each].sum()

# plot bar_chart
plt.style.use('dark_background')
fig,ax = plt.subplots(figsize=(8,8))
plt.bar(list(type_count_dict.keys()),list(type_count_dict.values()),align='center',
        color=['mediumturquoise','darkturquoise','turquoise','paleturquoise'])
plt.xticks(rotation=15)  #  横坐标旋转
ax.set_title("'Number of types of study data'")
for each in type_count_dict:   # 加标签
    # print(each)
    plt.text(each, type_count_dict[each]+0.05, '%.0f' % type_count_dict[each], ha='center', va= 'bottom',fontsize=11)
plt.show()

# plot pie_chart
fig1,ax1 = plt.subplots(figsize=(8,8))
plt.pie(type_count_dict.values(),labels=type_count_dict.keys(),autopct='%1.2f%%',
        colors=['mediumturquoise','darkturquoise','turquoise','paleturquoise'])
plt.show()