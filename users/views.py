from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from dentalfaqs.models import Book



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'you have registered with Dencare successfully')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def book(request):
    if request.method == 'POST':
        form = Book(request.POST)
        form.save()
        books = Book.objects.all()        
        context = {'books': books}
    if request.method == "POST":
        your_name = request.POST['your_name']
        your_phone = request.POST['your_phone']
        your_email = request.POST['your_email']
        your_address = request.POST['your_address']
        Choose_your_slot = request.POST['Choose_your_slot']
        Choose_day = request.POST['Choose_day']
        Choose_Doctor = request.POST['Choose_Doctor']
        Type_of_service = request.POST['Type_of_service']
        return render(request, 'users/confirmation.html',
            {
            'your_name': your_name,
            'your_phone': your_phone,
            'Choose_your_slot': Choose_your_slot,
            'Choose_day': Choose_day,
            'Choose_Doctor': Choose_Doctor,
            'Type_of_service': Type_of_service
             })
    
    return render(request, 'users/book.html')

def confirmation(request):
    return render(request, 'users/confirmation.html')

def thankyou(request): 
    return render(request, 'users/thankyou.html')

def survey(request):
    yes_count=0
    no_count=0
    if request.method == 'POST': 
        Choose_your_answer1 = request.POST['Choose_your_answer1']
        Choose_your_answer2 = request.POST['Choose_your_answer2']
        Choose_your_answer3 = request.POST['Choose_your_answer3']
        Choose_your_answer4 = request.POST['Choose_your_answer4']
        Choose_your_answer5 = request.POST['Choose_your_answer5']
        Choose_your_answer6 = request.POST['Choose_your_answer6']
        if Choose_your_answer1 == 'Yes':
            yes_count = yes_count + 1
        else:
            no_count =  no_count + 1
        if Choose_your_answer2 == 'Yes':
            yes_count = yes_count + 1
        else:
            no_count =  no_count + 1
        if Choose_your_answer3 == 'Yes':
            yes_count = yes_count + 1
        else:
            no_count =  no_count + 1
        if Choose_your_answer4 == 'Yes':
            yes_count = yes_count + 1
        else:
            no_count =  no_count + 1
        if Choose_your_answer5 == 'Yes':
            yes_count = yes_count + 1
        else:
            no_count =  no_count + 1
        if Choose_your_answer6 == 'Yes':
            yes_count = yes_count + 1
        else:
            no_count =  no_count + 1

        if (yes_count >= no_count): 
            return render(request, 'users/book.html')
        else:
            return render(request, 'users/thankyou.html')

    return render(request, 'users/survey.html')

    




