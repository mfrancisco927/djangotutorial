from recommender.forms import SearchForm
from django.shortcuts import render
from django.http import Http404, JsonResponse
from .models import *
from .forms import *
from django.views.decorators.http import require_POST, require_GET


def find_albums(artist):
   return list(Musicdata.objects.filter(artists__contains = artist).order_by('-popularity').values('id','name'))

@require_POST
def searchform_post(request):
    # create a form instance and populate it with data from the request:
    form = SearchForm(request.POST)
    # check whether it's valid:
    if form.is_valid():
        # process the data in form.cleaned_data as required
        return JsonResponse( {
            'albums' : find_albums(form.cleaned_data['artist'])
        })
    else:
        raise Http404('Something went wrong')


@require_GET
def searchform_get(request):
    form = SearchForm()
    return render(request, 'recommender/searchform.html', {'form': form})

