from django.urls import path,include
from app import views

urlpatterns = [    
    path('summarize/',views.display_summary,name='summarizer'),
]
