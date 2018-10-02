# 等比例压缩图片
# 参考 http://fc-lamp.blog.163.com/blog/static/174566687201282424018946/
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

def resizeImg(**args):
    # dst_w,dst_h  目标图片大小,  save_q  图片质量
    args_key = {'ori_img': '', 'dst_img': '', 'dst_w': '', 'dst_h': '', 'save_q': 75}
    arg = {}
    for key in args_key:
        if key in args:
            arg[key] = args[key]

    im = Image.open(arg['ori_img'])
    ori_w, ori_h = im.size
    widthRatio = heightRatio = None
    ratio = 1
    if (ori_w and ori_w > arg['dst_w']) or (ori_h and ori_h > arg['dst_h']):
        if arg['dst_w'] and ori_w > arg['dst_w']:
            widthRatio = float(arg['dst_w']) / ori_w
        if arg['dst_h'] and ori_h > arg['dst_h']:
            heightRatio = float(arg['dst_h']) / ori_h

        if widthRatio and heightRatio:
            if widthRatio < heightRatio:
                ratio = widthRatio
            else:
                ratio = heightRatio

        if widthRatio and not heightRatio:
            ratio = widthRatio
        if heightRatio and not widthRatio:
            ratio = heightRatio

        newWidth = int(ori_w * ratio)
        newHeight = int(ori_h * ratio)
    else:
        newWidth = ori_w
        newHeight = ori_h

    im.resize((newWidth, newHeight), Image.ANTIALIAS).save(arg['dst_img'], quality=arg['save_q'])

resizeImg(ori_img='7.png', dst_img='7.png', dst_w=32, dst_h=32, save_q=60)

#二值化处理
img = Image.open('7.png')
gray = img.convert('L')

WHITE, BLACK = 1, 0
img_new = gray.point(lambda x: WHITE if x > 128 else BLACK)
arr = np.array(img_new)

for i in range(arr.shape[0]):
    print(arr[i].flatten())