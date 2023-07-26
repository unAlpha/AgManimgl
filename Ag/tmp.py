import os
# import manimpango
# print(manimpango.list_fonts())
# os.system("ffmpeg -y -loop 1 \
#         -i \"/Users/pengyinzhong/Downloads/X/交付/抖音切割/images/1.jpg\" \
#         -t 0.1 \
#         -vf \"fps=50,format=yuv420p,scale=1920:1080:force_original_aspect_ratio=decrease,\
#         pad = 1920:1080:(ow-iw)/2:(oh-ih)/2\" \
#         -c:v libx264 -b:v 10000k -vbsf h264_mp4toannexb \
#         \"/Users/pengyinzhong/Downloads/X/交付/抖音切割/img_1.ts\""
#         )

# import numpy as np
# import matplotlib.pyplot as plt

# # Generate a set of random data with normal distribution
# data = np.random.normal(100, 10, 1000)

# # Plot a histogram of the data
# plt.hist(data, bins=30, edgecolor='black', density=True)

# # Plot the normal distribution curve over the histogram
# mean, std = np.mean(data), np.std(data)
# x = np.linspace(mean - 3*std, mean + 3*std, 100)
# y = 1 / (std * np.sqrt(2 * np.pi)) * np.exp(-(x - mean)**2 / (2 * std**2))
# plt.plot(x, y, 'r')

# # Add labels and title to the plot
# plt.xlabel('Data')
# plt.ylabel('Probability Density')
# plt.title('Normal Distribution Plot')

# # Show the plot
# plt.show()

# ########3D图像与平面映射
# import matplotlib.pyplot as plt
# import numpy as np
# from mpl_toolkits.mplot3d import Axes3D
# fig=plt.figure(facecolor='white')
# ax=Axes3D(fig)

# #X,Y value
# x=np.arange(-4,4,0.25)
# y=np.arange(-4,4,0.25)
# X,Y=np.meshgrid(x,y)
# R=np.sqrt(X**2+Y**2)
# #height value
# Z=np.cos(R)

# #r,cstride:黑线的密度   rstride:横轴间距；cstride:纵轴间距
# #rainbow：彩虹色
# ax.plot_surface(X,Y,Z,rstride=1,cstride=1,edgecolor='black',cmap=plt.get_cmap('rainbow'))

# #zdir->z；沿纵轴方向压等高线，映射到地面
# ax.contourf(X,Y,Z,zdir='z',offset=-2,cmap='rainbow')
# ax.set_zlim(-2,2)
# plt.show()

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
# Define the x range and the SymPy symbol
x_vals = np.linspace(-2, 2, 1000)
x = sp.symbols('x')

# Define the original function and its Taylor series expansion
func_sympy = x/(1-x)**2
taylor_series = sp.series(func_sympy, x, 0, 7).removeO()
taylor_func = sp.lambdify(x, taylor_series, 'numpy')

# Calculate the function values and Taylor series values
y_func = taylor_func(x_vals)  # Use the same x range as before
y_taylor = taylor_func(x_vals)

plt.figure(figsize=(10, 6))

# Plot the original function
plt.plot(x_vals, y_func, label='x/(1-x)^2')

# Plot the Taylor series expansion
plt.plot(x_vals, y_taylor, label='Taylor series expansion')

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Taylor series expansion of x/(1-x)^2 up to degree 7')
plt.legend()

# Set the x and y axis limits
plt.xlim([-2, 2])
plt.ylim([-1, 1])

# Show the plot
plt.grid(True)
plt.show()


