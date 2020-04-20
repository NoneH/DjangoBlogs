#!/usr/bin/env python
# encoding: utf-8
"""
@version: Python 3.7.0
@author: Xingyu Bu
@license: Apache Licence 
@contact: 1774142766@qq.com
@site: 
@software: PyCharm
@file: form.py
@time: 2020/4/20 13:54
"""

from django import forms


class CommentForm(forms.Form):
    """
    评论表单
    """
    name = forms.CharField(label='称呼', max_length=16, error_messages={
        'required': '请填写您的称呼',
        'max_length': '称呼太长咯'
    })

    content = forms.CharField(label='评论内容', error_messages={
        'required': '请填写您的评论内容！',
        'max_length': '评论内容太长咯'
    })