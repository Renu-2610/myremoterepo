from django.shortcuts import render
from django.template import loader #template loader
from django.http import HttpResponse

def index(request):
    template = loader.get_template('index.html') #getting template
    return HttpResponse(template.render()) #rendering the template in HttpResponse
    #return render(request,'index.html')  
def contactus(request):
    template = loader.get_template('contactus.html')
    return HttpResponse(template.render())
def form(request):
    template = loader.get_template('registration_form.html')
    return HttpResponse(template.render())
def setsession(request):  
    request.session['sname'] = 'renu'  
    request.session['semail'] = 'renu.sssit@gmail.com'  
    return HttpResponse("session is set")  
def getsession(request):  
    studentname = request.session['sname']  
    studentemail = request.session['semail']  
    return HttpResponse(studentname+" "+studentemail)
def setcookie(request):  
    response = HttpResponse("Cookie Set")  
    response.set_cookie('sname', 'javatpoint.com') 
    response.set_cookie('semail', 'semail@javatpoint.com')  
    return response    
def getcookie(request):  
    studentname = request.COOKIES['sname']  
    studentemail = request.COOKIES['semail']  
    return HttpResponse(studentname+" "+studentemail)