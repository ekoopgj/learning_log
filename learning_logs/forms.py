from django import forms
from .models import Topic

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic            #根据模型创建一个表单
        fields = ['text']        #该表单只包含text字段
        labels = {'text':''}     #让Django不要为字段text生成标签