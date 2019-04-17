# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Topic
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import TopicForm

# Create your views here.
def index(request):
    """学习笔记的主页"""
    return render(request,'learning_logs/index.html')

def topics(request):
    """显示所有的主题"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request,'learning_logs/topics.html',context)

def topic(request,topic_id):
    """显示单个主题的所有的条目"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic,'entries':entries}
    return render(request,'learning_logs/topic.html',context)

def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':  #确定请求方法是GET还是POST
        #未提交数据：创建一个新表单
        form = TopicForm()        #实例化TopicForm没有给定实参,Django将创建一个可供用户填写的空表单
    else:
        #POST提交的数据，对数据进行处理
        form = TopicForm(request.POST) #使用用户输入的数据创建一个TicForm实例
        if form.is_valid():            #检查标签是否有效
            form.save()                #如果有效就调用save(),且不指定任何实参
            return HttpResponseRedirect(reverse('learning_logs:topics'))   #重定向到显示条目所属主题的页面,用户将看到其编辑条目的新版本

    context = {'form':form}     #通过上下文字典将表单发送给模板
    return render(request, 'learning_logs/new_topic.html',context)
