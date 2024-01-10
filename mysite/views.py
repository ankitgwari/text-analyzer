from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    
    return render(request,'index.html')

def response(request):

    text=request.GET.get('feedback','no feedback')
    removepunc=request.GET.get('removepunc','off')
    upper=request.GET.get('upper','off')
    extraspace=request.GET.get('extraspace','off')
    newline=request.GET.get('newline','off')
    


    if(removepunc=="on"):
        fbck=""
        punctuation='''",.<>?/:;\!'''
        
        for char in text:
            if char not in punctuation :
                fbck=fbck+char
        
        text=fbck
        array={'name':request.GET.get('name','user'),
                'Feedback':fbck
        }

    if(upper=="on"):
        fbck=""
        fbck=text.upper()
        
        text=fbck
        array={'name':request.GET.get('name','user'),
            'Feedback':fbck
        }

    if(extraspace=="on"):
        fbck=""
        for index,char in enumerate(text):
            if not(text[index]==" " and text[index+1]==" ") :
                fbck=fbck+char
        
        text=fbck
        array={'name':request.GET.get('name','user'),
                'Feedback':fbck
        }

    if(newline=="on"):
        fbck=""
        for char in text:
            if char!="\n" and char!="\r":
                fbck=fbck+char
        
        array={'name':request.GET.get('name','user'),
                'Feedback':fbck
        }

    if( removepunc!="on" and upper!="on" and extraspace!="on" and newline!="on" ):
        return HttpResponse("<h1>Error!</h1>")
    return render(request,"response.html",array)
