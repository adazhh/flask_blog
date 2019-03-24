# -*- coding: utf-8 -*-
# 辅助函数
"""
    :author: Grey Li (李辉)
    :url: http://greyli.com
    :copyright: © 2018 Grey Li <withlihui@gmail.com>
    :license: MIT, see LICENSE for more details.
"""
# 前者是Python2，后者是Python3
try:
    from urlparse import urlparse, urljoin
except ImportError:
    from urllib.parse import urlparse, urljoin

from flask import request, redirect, url_for

def is_safe_url(target):
    # request.host_url获取程序内的主机URL
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc

# 防止重定向漏洞
def redirect_back(default='blog.index', **kwargs):
    for target in request.args.get('next'), request.referrer:
        if not target:
            continue
        if is_safe_url(target):
            return redirect(target)
    return redirect(url_for(default, **kwargs))

# 补充
# urljoin的用法
# 连接两个参数的url, 将第二个参数中缺的部分用第一个参数的补齐,如果第二个有完整的路径，则以第二个为主
# print(parse.urljoin('https://movie.douban.com/', 'index'))
# print(parse.urljoin('https://movie.douban.com/', 'https://accounts.douban.com/login'))
# 下面是结果
# https://movie.douban.com/index6     https://accounts.douban.com/login