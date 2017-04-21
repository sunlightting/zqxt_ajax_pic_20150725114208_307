#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 

import os
import json
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
import urllib
import re

BASE_DIR = settings.BASE_DIR  # 项目目录
# 假设图片放在static/pics/里面
PICS = os.listdir(os.path.join(BASE_DIR, 'common_static/pics'))

print PICS  # 启动时终端上可以看到有哪些图片，我只放了一张，测试完后这一行可以删除


def index(request):
    return render(request, 'index.html')


def get_pic(request):
    color = request.GET.get('color')
    number = request.GET.get('number')
    name = '{}_{}'.format(color, number)

    # 过滤出符合要求的图片，假设是以输入的开头的都返回
    result_list = filter(lambda x: x.startswith(name), PICS)
    img_url = color
    save_path = 'E:\eclipse\zqxt_ajax_pic_20150725114208_307\zqxt_ajax_pic\common_static\pics\ 1.png'
 
    f = urllib.urlopen(img_url)
    with open(save_path, "wb") as code:
        code.write(f.read())
    img_url = number
    save_path = 'E:\eclipse\zqxt_ajax_pic_20150725114208_307\zqxt_ajax_pic\common_static\pics\ 2.png'
 
    f = urllib.urlopen(img_url)
    with open(save_path, "wb") as code:
        code.write(f.read())
    print 'result_list', result_list

    return HttpResponse(
        json.dumps(result_list),
        content_type='application/json')
