import json
from django.shortcuts import render,json
from scripts.summarizer import summarize 
from django.http import JsonResponse

# Create your views here.

def display_summary(request):
    summary=summarize('/home/satya/Desktop/Hackathon/summarization/Summarization/radha2016.pdf')
    return JsonResponse({"summary":summary},safe=False)
    
