from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.conf import settings

# Create your views here.
from .models import my_artifact


#def index(request):
    #return HttpResponse("Hey")
def index(request):
    try:
        all_artifact = my_artifact.objects.all()
        if request.method == "GET":
            q = request.GET.get('search_box', None)
            try:
                res = my_artifact.objects.filter(artifact_name__contains=q)
                con = {'res': res}
                return render(request, 'artifacts/index_query.html', con)
            except:
                res = False
    except all_artifact.DoesNotExist:
        raise Http404("Artifact does not exist :")
    context = {'all_artifacts': all_artifact}
    return render(request, 'artifacts/index.html', context)


def detail(request, artifact_id):
    current_artifact= my_artifact.objects.get(pk=artifact_id)
    context={'this_artifact': current_artifact}
    if request.method == "GET":
        q = request.GET.get('search_box', None)
        try:
            res = my_artifact.objects.filter(artifact_name__contains=q)
            con = {'res': res}
            return render(request, 'artifacts/index_query.html', con)
        except:
            res = False
    return render(request, 'artifacts/detail.html', context)


def contactus(request):
    return render(request,'artifacts/contactus.html',{})