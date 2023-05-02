import os
import manimpango
print(manimpango.list_fonts())
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