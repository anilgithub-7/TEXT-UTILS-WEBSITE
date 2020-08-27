from django.http import HttpResponse
from django.shortcuts import render

def index(request):
     return render(request,'index.html')            
def analyze(request):
     djtext= request.GET.get('text','off')
     removepunc=request.GET.get('removepunc','off')
     fullcap=request.GET.get('fullcap','off')
     newlineremover=request.GET.get('newlineremover','off')
     charactercount=request.GET.get('charactercount','off')
     extraspaceremover=request.GET.get('extraspaceremover','off')
     if removepunc == "on":
          punctuations ='''!()-[];:'"\,<>./?@#$%^&*_~'''
          analyzed= ""
          for char in djtext:
               if char not in punctuations:
                    analyzed= analyzed + char
          params={'purpose':"removing punctuations",'analyzed_text':analyzed}
          djtext=analyzed
     if(fullcap == "on"):
          analyzed=""
          for char in djtext:
               analyzed = analyzed + char.upper()
          params={'purpose':"capitalizing the letter",'analyzed_text':analyzed}
          djtext=analyzed
     if newlineremover == "on":
          analyzed=""
          for char in djtext:
               if char != "\n" and char !="\r":
                    analyzed=analyzed + char
          params={'purpose':"remove the new line",'analyzed_text':analyzed}
          djtext=analyzed
     if charactercount == "on":
          analyzed=""
          i=0
          for i in range(len(djtext)):
               i=i+1
               analyzed=i
          params={'purpose':"counts the number of character",'analyzed_text':analyzed} 
          djtext=analyzed    
     if extraspaceremover == "on":
          analyzed=""
          for index, char in enumerate(djtext):
               if djtext[index] == " " and djtext[index+1] == " ":
                    pass
               else:
                    analyzed = analyzed + char
          params={'purpose':"removes the extra space",'analyzed_text':analyzed}
          
     if (removepunc!="on" and fullcap!="on" and charactercount!="on" and extraspaceremover!="on" and newlineremover!="on"):
          return HttpResponse("choose any operation")         
     return render(request,'analyze.html',params)                         