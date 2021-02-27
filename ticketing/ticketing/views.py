from django.http import HttpResponse
from django.shortcuts import render
from .models import Ticket
from django.contrib import messages


def home(request):
    return render(request, 'tickets/home.html')


def submit(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        body = request.POST.get('body')
        hacker = request.POST.get('hacker')
        if username is not '' and body is not '':
            new_ticket = Ticket(submitter=username, body=body, hacker=hacker)
            new_ticket.save()
            messages.success(request, "your message is submitted")
        else:
            messages.error(request, "please input both fields")

    return render(request, 'tickets/submit.html')


def tickets(request):
    allTickets = Ticket.objects.all()
    return render(request, 'tickets/tickets.html', {'tickets': allTickets})
