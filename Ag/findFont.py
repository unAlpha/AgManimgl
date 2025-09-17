import matplotlib.font_manager as fm

# 获取所有可用字体
fonts = [f.name for f in fm.fontManager.ttflist]
# 去重并排序
unique_fonts = sorted(list(set(fonts)))

# 打印所有字体
for font in unique_fonts:
    print(font)