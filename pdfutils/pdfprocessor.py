import pdfplumber

# 加载一个pdf

pdf = pdfplumber.open('./test.pdf')

# 得到pdf的元数据和页数
print(pdf.metadata)
print(pdf.pages)

# pdf 中每一页都对应一个Page对象
page1 = pdf.pages[0]  # 第一个page对象
page2 = pdf.pages[1]  # 第一个page对象

# 获得page对象中各种属性
print(page1.page_number)
print(page1.width)  # 像素
print(page1.height)  # 像素

# 提取内容
# 1. 提取文本内容
print(page1.extract_text())
print(page1.extract_text(layout=True))  # 提取文本后是否按照原来的布局提取文本内容

print(page1.extract_table())  # 提取表格，放到了二维数组中

# 2. 提取图片，没有图片就提不到
print(page1.images)  # page1中没有图片
print(page2.images)  # page2中有图片，会都提取出来

image = page2.images[0]
ppoint = (image['x0'], image['top'], image['x1'], image['bottom'])  # 图片的左上点和右下点的坐标
page2.crop(ppoint).to_image(antialias=True, resolution=1080).show()  # 剪裁图片，展示出来
page2.crop(ppoint).to_image(antialias=True, resolution=1080).save('./test1.png')  # 剪裁图片，存储
# 整个页面全部提取成图片
page1.to_image(antialias=True, resolution=1080).show() # 加属性antialias， 抗锯齿数，像素更多resolution，高清
