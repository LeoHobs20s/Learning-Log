from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    """ This class facilitates insertion of a topic in a form """

    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text':''}

class EntryForm(forms.ModelForm):
    """ This class facilitates insertion of an entry """

    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text':''}
        widget = {'text':forms.Textarea(attrs={'cols':80})}
