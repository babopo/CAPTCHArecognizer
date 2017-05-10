# -*- coding: utf-8-*-


# 获取图片的标注信息及序号
def get_name(path):
    fullname = path.split("_")[-1]
    numname = path.split("_")[0]
    num = numname.split("/")[-1]
    realname = fullname.split(".")[0]
    return num, realname
