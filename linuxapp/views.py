from django.shortcuts import render
from django.utils import encoding #smart_unicode
from urllib.parse import parse_qsl

from .models import Service
from .models import Contact

# Create your views here.
def services(req):
    if req.method == 'POST':
        post = req.POST
        s = Service()
        s.icon = post['icon']
        s.title = post['title']
        s.detail = post['detail']
        s.save()
        services = Service.objects.all()
        print(services)
        return render(req, 'linuxapp/services.html', { 'services': services })
    else:
        print('ร้องขอทำมะดา')
        services = Service.objects.all()
        print(services)
        return render(req, 'linuxapp/services.html', { 'services': services })

def contact(req):
    if req.method == 'POST':
        post = req.POST
        c = Contact()
        c.name = post['name']
        c.email= post['email']
        c.message = post['message']
        c.save()
        contact = Contact.objects.all()
        print(contact)
        return render(req, 'linuxapp/contact.html', { 'contact': contact })
    else:
        print('ร้องขอทำมะดา')
        contact = Contact.objects.all()
        print(contact)
        return render(req, 'linuxapp/contact.html', { 'contact': contact })


def index(req):
    return render(req, 'linuxapp/index.html')
def contact(req):
    return render(req, 'linuxapp/contact.html')
def singlepost(req):
    return render(req, 'linuxapp/single-post.html')
def singleproject(req):
    return render(req, 'linuxapp/single-project.html')