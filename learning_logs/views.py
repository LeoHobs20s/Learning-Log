from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls  import reverse

from .models import Topic
from .forms import TopicForm

def index(request):
    """ This view represents the Home page """
    return render(request, 'learning_logs/index.html')

def topics(request):
    """ This view represents the Topics page """

    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """ This view represent the Topic Page """

    topic = get_object_or_404(Topic, pk=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic, 'entries':entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """ This view will generate code for the new topic form """

    if request.method != 'POST':
        # No data submitted; create a blank form
        form = TopicForm()
    else:
        # Data submitted; process data
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topics'))
    
    context = {'form':form}
    return render(request, 'learning_logs/new_topic.html', context)