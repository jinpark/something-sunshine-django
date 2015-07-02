from django.shortcuts import render
from episodes.models import Episode
from django.views.decorators.clickjacking import xframe_options_exempt

def homepage(request, template="home.html"):
    context = {}
    context['episodes'] = Episode.objects.all()
    context['episode'] = None
    # ghetto way of handing per episode links
    try:
        episode_num = int(request.GET.get('episode'))
        episode = Episode.objects.get(number=episode_num)
        context['episode'] = episode
    except:
        pass
    return render(request, template, context)

def newhome(request, template="newhome.html"):
    ''' for testing new homepage designs '''
    context = {}
    context['episodes'] = Episode.objects.all()
    context['episode'] = None
    try:
        episode_num = int(request.GET('episode'))
        episode = Episode.objects.get(number=episode_num)
        context['episode'] = episode
    except:
        pass
    return render(request, template, context)

def feed(request, template="feed.xml"):
    ''' xml feed for itunes '''
    context = {}
    context['episodes'] = Episode.objects.all()
    return render(request, template, context, content_type="application/xml")

@xframe_options_exempt
def embed(request, id, template="embed.html"):
    ''' for twitter cards '''
    episode = Episode.objects.get(pk=id)
    return render(request, template, {'episode': episode})