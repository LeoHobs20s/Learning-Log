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
            field.widget.attrs['class'] = 'form-control'


class EntryForm(forms.ModelForm):
    """ This class facilitates insertion of an entry """

    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text':''}
        widget = {'text':forms.Textarea(attrs={'cols':80, 'class':'form-control'})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
