from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from django.urls  import reverse

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

def index(request):
    """ This view represents the Home page """
    return render(request, 'learning_logs/index.html')


@login_required
def topics(request):
    """ This view represents the Topics page """

    topics = Topic.objects.filter(owner=request.user).order_by('date_added') 
    context = {'topics':topics}
    return render(request, 'learning_logs/topics.html', context)


@login_required
def topic(request, topic_id):
    """ This view represent the Topic Page """

    topic = get_object_or_404(Topic, pk=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    if topic.owner != request.user:
        raise Http404
    context = {'topic':topic, 'entries':entries}
    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    """ This view will generate code for the new topic form """

    if request.method != 'POST':
        # No data submitted; create a blank form
        form = TopicForm()
    else:
        # Data submitted; process data
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('topics'))
    
    context = {'form':form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """ Adding new entry data """

    topic = get_object_or_404(Topic, pk=topic_id)

    if request.method != 'POST':
        # No data submitted; create a blank form
        form = EntryForm()
    else:
        # POST data submitted; process data
        form = EntryForm(data=request.POST)
        new_entry = form.save(commit=False)
        new_entry.topic = topic
        new_entry.save()
        return HttpResponseRedirect(reverse('topic', args=[topic_id]))
    
    context = {'topic':topic, 'form':form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """ Edit existing entries """

    entry = get_object_or_404(Entry, pk=entry_id)
    topic = entry.topic

    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # No Data Submitted; create blank form 
        form = EntryForm(instance=entry)
    else:
        # POST Data submitted; process data
        form = EntryForm(instance=entry, data=request.POST)
        form.save()
        return HttpResponseRedirect(reverse('topic', args=[topic.id]))
    
    context = {'topic':topic, 'entry':entry, 'form':form}
    return render(request, 'learning_logs/edit_entry.html', context)