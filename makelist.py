# coding=utf-8
import os

def makeFileLists(imgPath, fileName='list.txt', withLabel=False, ext=['jpg','bmp','png']):
    '''
        makeFileList 函数用于包含多层目录的文件列表创建
        Params:
            imgPath     ：最上层的目录路径
            fileName    : 列表文件名称
            withLabel   : 默认为`False`,如果需要为每个图片路劲添加label,
                          则将该参数设置为`True`,图片所在目录的名称即为
                          该图片的label
            ext         : 图片格式
        Usage:
            makeFileLists('imagesRootPath', 'imageList.txt', False)
    '''
    # 判断路径是否存在
    if not os.path.exists(imgPath):
        print imagesPath, 'IS NOT EXIST, PLEASE CHECK IT!'

    # 判断路径是否为目录，如果是，则对目录下的子目录做递归操作
    elif os.path.isdir(imgPath):
        subPath = os.listdir(imgPath)
        subPath = [os.path.join(imgPath,path) for path in subPath]
        for path in subPath:
            makeFileLists(path, fileName, withLabel)
    # 如果路径不是目录，则为图片的相对路径
    else:
        # 只保存指定格式的图片
        if imgPath[-3:] in ext:
            # 以追加的方式打开文件
            f = open(fileName,'a')
            # 如果需要添加label,则将图片所在目录的名称作为label
            if withLabel:
                line = imgPath+' '+(imgPath.split('/'))[-2]+'\n'
            else:
                line = imgPath+'\n'
            # 写入文件
            f.writelines(line)
            f.close()

if __name__ == "__main__":
    imagesPath = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.path.sep + ".")
    fileName = 'list.txt'
    if os.path.exists('list.txt'):
        os.remove('list.txt')
    makeFileLists(imagesPath, fileName, True)
    
