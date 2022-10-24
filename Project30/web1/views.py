from django.shortcuts import render
from .forms import MyForm
from .models import MyModel


def page1(request):
    if request.method == 'POST':
        # name = request.POST.get('name')
        # age = request.POST.get('age')
        form = MyForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            model1 = MyModel(surname=data['surname'], name=data['name'], age=data['age'])
            model1.save()
        # print(name)
        # print(age)
    else:
        form = MyForm()
    context = {
        'form': form,
    }
    return render(request, 'base.html', context)
