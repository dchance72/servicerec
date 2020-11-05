from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings

# Create your views here.
from .models import Firearm,CheckEvent
from .forms import CheckForm, FirearmForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect

settings.LOGIN_URL='/login/'


def default(request):
    return redirect('/login/')


@login_required
def index(request):
    firearms_list = Firearm.objects.order_by('id')
    context = {'firearms_list': firearms_list}
    return render(request, 'tracksvc/index.html', context)


@login_required
def fdetail(request, firearm_id):
    firearm = Firearm.objects.get(pk=firearm_id)
    check_event_list = CheckEvent.objects.filter(firearm=firearm_id)
    context = {'check_event_list': check_event_list,
    'firearm': firearm,
    }
    return render(request, 'tracksvc/fdetail.html', context)


@login_required
def get_check_data(request, firearm_id):
    if request.method == 'POST':
        form = CheckForm(request.POST)
        if form.is_valid():
            ce = CheckEvent()
            ce.when = form.cleaned_data['when']
            ce.user = form.cleaned_data['user']
            ce.state = form.cleaned_data['state']
            ce.notes = form.cleaned_data['notes']
            ce.firearm = Firearm.objects.get(pk=firearm_id)
            ce.save()
            return HttpResponseRedirect(reverse('fdetail', args=(firearm_id,)))
    else:
        form = CheckForm(initial={'user': request.user})
        f = Firearm.objects.get(pk=firearm_id)
    return render( request, 'tracksvc/addcheck.html', {'form': form, 'firearm': f})


def add_firearm(request):
    if request.method == 'POST':
        form = FirearmForm(request.POST)
        if form.is_valid():
            f = Firearm()
            f.make = form.cleaned_data['make']
            f.model = form.cleaned_data['model']
            f.serial = form.cleaned_data['serial']
            f.location = form.cleaned_data['location']
            f.save()
            return HttpResponseRedirect(reverse('index', args=()))
    else:
        form = FirearmForm()
    return render(request, 'tracksvc/addfirearm.html', {'form': form})
