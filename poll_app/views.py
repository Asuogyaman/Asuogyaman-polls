from django.shortcuts import render, redirect
from .models import *
from django.urls import path
from django.contrib.auth.models import User, auth


# Create your views here.
# def index(request):
#     total = party.objects.all()
#     amount =0
#     list =[]
#     for a in total: 
#         amount+=a.votes
    
#     for c in total:
#         y = (c.votes/amount)*100
#         list.append({'c':c, 'percentage':round(y,2)})

#     context = {'total' : total, "b": list}
#     return render(request, 'index.html', context)

def index(request):
    total = Vote.objects.all()
    total_ndc =0
    total_npp =0
    list_npp =[]
    list_ndc =[]
    for a in total: 
        total_ndc+=a.ndc_votes
        total_npp+=a.npp_votes
    total_votes = total_ndc + total_npp
    percent_ndc = round((total_ndc/total_votes) *100, 2)
    percent_npp = round((total_npp/total_votes) *100, 2)
    percent = [{'party': 'Npp', 'percent': percent_npp},{'party': 'ndc', 'percent': percent_ndc}]
    for c in total:
        y = (c.npp_votes/total_npp)*100
        z = (c.ndc_votes/total_ndc)*100
        list_npp.append({'c':c, 'percentage':round(y,2)})
        list_ndc.append({'c':c, 'percentage':round(z,2)})

    context = {'percent' : percent, "list_npp": list_npp, "list_ndc": list_ndc, 'total_votes': f"{total_votes:,}"}
    return render(request, 'index.html', context)



def parliamentary(request):
    total = Vote.objects.all()
    total_mp_npp =0
    total_mp_ndc =0
    list_mp_npp =[]
    list_mp_ndc =[]
    for a in total: 
        total_mp_npp+=a.mp_npp
        total_mp_ndc+=a.mp_ndc
    total_mp_votes = total_mp_npp + total_mp_ndc
    percent_mp_npp = round((total_mp_npp/total_mp_votes) *100, 2)
    percent_mp_ndc = round((total_mp_ndc/total_mp_votes) *100, 2)
    percent = [{'party': 'Pius Hadzide', 'percent': percent_mp_npp},{'party': 'Thomas Ampem', 'percent': percent_mp_ndc}]
    #Pie Chart
    for c in total:
        y = (c.mp_npp/total_mp_npp)*100
        z = (c.mp_ndc/total_mp_ndc)*100
        list_mp_npp.append({'c':c, 'percentage':round(y,2)})
        list_mp_ndc.append({'c':c, 'percentage':round(z,2)})

    context = {'percent' : percent, "list_npp": list_mp_npp, "list_ndc": list_mp_ndc, 'total_votes': f"{total_mp_votes:,}"}
    return render(request, 'parliamentary.html', context)


def logout(request):
    auth.logout(request)
    return redirect("/")