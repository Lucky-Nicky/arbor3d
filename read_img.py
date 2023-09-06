# -*- coding: utf-8 -*-
with open("img/5.jpg","rb") as f:
    a=f.read()


print(a.__sizeof__()/1024/1024)