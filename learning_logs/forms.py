from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    """ This class facilitates insertion of a topic in a form """

    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text':''}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control text-bg-dark'


class EntryForm(forms.ModelForm):
    """ This class facilitates insertion of an entry """

    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text':''}
        widget = {'text':forms.Textarea(attrs={'cols':80, 'placeholder':'Enter Text Here ...'})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control text-bg-dark'
