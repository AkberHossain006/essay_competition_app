from django.shortcuts import render, redirect, get_object_or_404
from .models import Competition,EssayTopic,Essay
from .forms import EssayForm
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.utils import timezone


def index(request):
    return render(request, 'nana/index.html')


def about(request):
    return render(request, 'nana/about.html')


def contact(request):
    return render(request, 'nana/contact.html')




def system(request):
    return render(request, 'nana/system.html')



@login_required
def competitions(request):
    competitions = Competition.objects.all()
    context = {'competitions': competitions}
    return render(request, 'nana/competitions.html', context)
@login_required
def competition(request, competition_id):
    competition = Competition.objects.get(id=competition_id)

    essay_topics = EssayTopic.objects.filter(competition_id=competition)
    context = {'competition': competition, 'essay_topics': essay_topics,'now': timezone.now()}
    return render(request, 'nana/essaytopics.html', context)


@login_required
def new_essay(request, topic_id):
    topic = get_object_or_404(EssayTopic, id=topic_id)
    deadline_expired = topic.competition.deadline < timezone.now()
    if request.method != 'POST':
        form = EssayForm()
    else:
        form = EssayForm(data=request.POST)
        if form.is_valid():
            new_essay = form.save(commit=False)  # Don't save to DB yet
            new_essay.essay_topic = topic  # Correctly set the essay_topic field
            new_essay.author = request.user  # Set the author to the logged-in user
            new_essay.save()  # Save the essay
            return redirect('nana:index')  # Redirect to competition page
    context = {'topic': topic, 'form': form,'deadline_expired': deadline_expired}
    return render(request, 'nana/essay.html', context)