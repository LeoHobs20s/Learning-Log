from django import forms

from .models import Topic

class TopicForm(forms.ModelForm):
    """ This class facilitates inserting a topic in a form """

    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text':''}
