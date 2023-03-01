import os

root_path = 'C:/Users/kongzejian/PycharmProjects/yolov7/datasets/test/right'  # 要修改的图像所在的文件夹路径

filelist = os.listdir(root_path)  # 遍历文件夹
i = 0
for item in filelist:
    src = os.path.join(os.path.abspath(root_path), item)  # 原本的名称
    dst = os.path.join(os.path.abspath(root_path),
                           os.path.basename(root_path)+'___'+str(i) + '.jpg')  # 这里我把格式统一改成了 .jpg
    os.rename(src, dst)  # 意思是将 src 替换为 dst
    i += 1
    print('rename from %s to %s' % (src, dst))

print('ending...')