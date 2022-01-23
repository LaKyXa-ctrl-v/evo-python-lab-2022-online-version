from django.shortcuts import render, redirect, reverse
from .forms import PersonForm
from .models import Person
from django.views.generic.edit import FormView
import urllib.parse
# Create your views here.


class PersonFormView(FormView):
    template_name = 'start.html'
    form_class = PersonForm
    success_url = '/login/'
    extra_context = {'title': 'Сторінка для привітання'}

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        self.request.session["user_data"] = form.cleaned_data
        Person.objects.create(**form.cleaned_data)
        return redirect(reverse('wellcome') + "?" + urllib.parse.urlencode(form.cleaned_data))

    def form_invalid(self, form):
        self.request.session["user_data"] = form.cleaned_data
        return redirect(reverse('login_done') + "?" + urllib.parse.urlencode(form.cleaned_data))

# def login(request):

#     if request.method == 'POST':
#         form = PersonForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login_done')
#         else:
#             error = "Щось пішло не так =("
#     else:
#         form = PersonForm()
#     error = ''
#     data = {
#         'form': form,
#         'error': error,
#     }
#     return render(request, 'start.html', data)


def home(request):
    person_list = Person.objects.filter().order_by('-pk')
    return render(request, 'home.html', {"person_list": person_list})


def wellcome(request):
    return render(request, 'wellcome.html', {'user_data': request.session["user_data"]})


def login_done(request):
    return render(request, 'login_done.html', {'user_data': request.session["user_data"]})
