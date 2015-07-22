from django.shortcuts import render_to_response
from django.template import RequestContext
from medicine.forms import VisitForm


def home(request):
    tip = ""
    if request.method == 'POST':
        form = VisitForm(request.POST)
        if form.is_valid():
            visit = form.save()
            tip = "Thanks for writing. Your number %d" % visit.id
            form = VisitForm()
    else:
        form = VisitForm()
    return render_to_response('index.html',
                              {"form": form, "tip": tip},
                              context_instance=RequestContext(request))
