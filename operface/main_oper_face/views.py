from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from .models  import Instalator,Installation


def show_all_installators():
    Instalators = Instalator.objects.order_by('name')
    all_Instalator = []
    for Instalator_index in Instalators:
        Instalator_info = {
            'chat_id': Instalator_index.chat_id,
            'name': Instalator_index.name,
            'score': Instalator_index.score,
        }
        all_Instalator.append(Instalator_info)
    return(all_Instalator)

def show_all_selected_installations(chat_id):
    try:
        detail_installations = Installation.objects.filter(Instalator_id = chat_id)
    except:
        raise Http404("installations of this instalator not found")

    all_Installation = []
    for  Installation_index in detail_installations:
        Installation_info = {
            'id' : Installation_index.id,
            'location' : Installation_index.location,
            'Instalator_name' : Installation_index.Instalator_id.name,
            'Instalator_id' : Installation_index.Instalator_id.chat_id,
            'date' : Installation_index.date,
            'answer' : Installation_index.answer,
        }
        all_Installation.append(Installation_info)
    return(all_Installation)

def show_selected_installation(id):
    try:
        detail_installation = Installation.objects.get(id = id)
        detail_info = {
            'id' : detail_installation.id,
            'location' : detail_installation.location,
            'Instalator_name' : detail_installation.Instalator_id.name,
            'Instalator_id' : detail_installation.Instalator_id.chat_id,
            'date' : detail_installation.date,
            'location' : detail_installation.location,
            'photo_1' : detail_installation.photo_1,
            'photo_2' : detail_installation.photo_2,
            'photo_3' : detail_installation.photo_3,
            'photo_4' : detail_installation.photo_4,
            'photo_5' : detail_installation.photo_5,
        }
        answer = detail_installation.answer
        print(detail_info)
    except:
        raise Http404("selected installation not found")

    try:
        answer = str(answer).replace("("," ").replace(")"," ").replace(","," ").replace("'"," ")[3:][:-4].split('  ')
        detail_answer = {
            'one' : answer[1],
            'two' : answer[2],
            'three' : answer[3],
            'four' : answer[4],
            'five' : answer[5],
            'six' : answer[6],
        }
    except:
        raise Http404("not answer")
    return(detail_info,detail_answer)

    # try:
    #     for i in range(1,6):





def index(request):

    all_Instalator = show_all_installators()

    return render(
        request,
        'index.html',
        {'Instalator_info':all_Instalator,},
    )

def installations(request,chat_id):

    all_Instalator = show_all_installators()
    all_Installation = show_all_selected_installations(chat_id)

    return render(
        request,
        'detail_installations.html',
        {
            'Instalator_info':all_Instalator,
            'Installation_info':all_Installation,
        },
    )

def installation(request,chat_id,id):

    all_Instalator = show_all_installators()
    all_Installation = show_all_selected_installations(chat_id)
    selected_installation_info = show_selected_installation(id)

    return render(
        request,
        'detail_installation.html',
        {
            'Instalator_info':all_Instalator,
            'Installation_info':all_Installation,
            'detail_info':selected_installation_info[0],
            'answer':selected_installation_info[1],
        },
    )
