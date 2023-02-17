import random
import numpy as np
import matplotlib.pyplot as plt
from typing import List

# 冒泡排序
def bubble_sort(arr: List[int]):
    """
    冒泡排序(Bubble sort)
    :param arr: 待排序的List,此处限制了排序类型为int
    :return: 冒泡排序是就地排序(in-place)
    """
    # print("原始数据：", arr)
    counter = 0
    length = len(arr)
    if length <= 1:
        return arr,0
    for i in range(length):
        is_made_swap = False  ## 设置标志位，若本身已经有序，则直接break
        for j in range(length - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_made_swap = True
                counter+=1
        if not is_made_swap:
            break
    # print("冒泡排序结果：", arr)
    return counter
        
# 测试数据
if __name__ == '__main__':

    random.seed(0)
    arr = [i for i in range(100)]
    data = []
    for t in range(1000):
        random.shuffle(arr)
        count = bubble_sort(arr)
        data.append(count)
    print("排序次数表：", data)
    # Plot a histogram of the data
    # plt.hist(data, bins=len(set(data)), edgecolor='black', density=True)
    plt.hist(data, bins=len(set(data)), rwidth=1, density=True)

    # Plot the normal distribution curve over the histogram
    mean, std = np.mean(data), np.std(data)
    x = np.linspace(mean - 3*std, mean + 3*std, 100)
    y = 1 / (std * np.sqrt(2 * np.pi)) * np.exp(-(x - mean)**2 / (2 * std**2))
    plt.plot(x, y, 'r')

    # Add labels and title to the plot
    plt.xlabel('Data')
    plt.ylabel('Probability Density')
    plt.title('Normal Distribution Plot')

    # Show the plot
    plt.show()