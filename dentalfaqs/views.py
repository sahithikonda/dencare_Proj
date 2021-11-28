from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect



posts = [
	{
		'author': 'question1',
		'title': 'what are early signs of dental trouble?',
		'content': 'Visit a dentist id you have any of these issues',
		'date_posted': '21 Nov 2020'
	},
	{
		'author': 'question2',
		'title': 'why do i need dental exams?',
		'content': 'Regular exams help spot trouble early to prevent bigger and more costly treatments later',
		'date_posted': '22 Nov 2020'
	},
	{
		'author': 'question3',
		'title': 'Are dental X-rays safe and needed?',
		'content': 'Medical and dental experts study the use of X-rays and set limits for their saftey. your dentist should take as few as possible. sometimes dentists may recommend X-rays to diagnose a special problem. Advancements in technology means todays digital X-rays release much less radiation',
		'date_posted': '30 Nov 2020'
	},
	{
		'author': 'question4',
		'title': 'Is clinics are sanatizing regularly to prevent covid-19 spread?',
		'content': 'Our clinics gives first priority to cleanliness and saftey of patients we regularly sanatize the common areas and also dental instruments that doctor use ',
		'date_posted': '1 Dec 2020'
	},
	{
		'author': 'question5',
		'title': 'How clinics are managing the appointments to stop spreading Covid-19?',
		'content': 'Clincs take care of spreading Coivd-19 by having less number of patients at a time and also we regularly sanatize all our clinics to stop spreading disease',
		'date_posted': '2 Dec 2020'
	},
	{
		'author': 'question6',
		'title': 'How much does the dental check-up costs?',
		'content': 'It mostly depends on which type consultation you are needed we normally provide different types of servives you can go to our service pages and also pricing pages more details ',
		'date_posted': '13 Dec 2020'
	},
	{
		'author': 'question7',
		'title': 'How can we get doctor appointment?',
		'content': 'we have booking option on our website where you can directly get an appointment by entering required details',
		'date_posted': '01 Jan 2021'
	},
	{
		'author': 'question8',
		'title': 'Do you provide direct emergency cases without appointments?',
		'content': 'Yes, we do take emergency cases',
		'date_posted': '13 Jan 2021'
	},

]

def home(request):
	context = {
		'posts': posts
		}
	return render(request, 'dentalfaqs/home.html', context )
	
# Create your views here.

def services(request):
	return render(request, 'dentalfaqs/services.html', {'title': 'Services'})

def Prices(request):
	return render(request, 'dentalfaqs/Prices.html', {'title': 'Prices'})

def Contact(request):
  return render(request, 'dentalfaqs/Contact.html', {'title': 'Contact'})

def getback(request):
  return render(request, 'dentalfaqs/getback.html')




 
  

        
        
       