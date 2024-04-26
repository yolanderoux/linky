from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.urls import reverse

from .models import Link
from .forms import LinkForm

# Create your views here.
def index(request):
    links = Link.objects.all()
    context = {
        "links": links
    }
    return render(request, 'linky/index.html', context)

def create(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))
    else:
        form = LinkForm()
    context = {
        "form": form
    }
    return render(request, 'linky/create.html', context)

def root_link(request, link_slug):
    link = get_object_or_404(Link, slug=link_slug)
    link.click()
    return redirect(link.destination)