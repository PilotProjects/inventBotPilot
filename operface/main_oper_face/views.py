from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from .models  import Instalator,Installation

from transliterate import translit, get_available_language_codes

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
        #    'answer' : Installation_index.answer,
        }
        all_Installation.append(Installation_info)
    return(all_Installation)



def custom_translite(answer_list):
    for index in range(0,len(answer_list)):
        answer_list[index] = translit(answer_list[index], 'ru')
    return(answer_list)

def show_selected_installation(id):
    try:
        detail_installation = Installation.objects.get(id = id)
        detail_info = {
            'id' : detail_installation.id,
            'location' : detail_installation.location,
            'Instalator_name' : detail_installation.Instalator_id.name,
            'Instalator_id' : detail_installation.Instalator_id.chat_id,
            'Instalator_score' : detail_installation.Instalator_id.score,
            'date' : detail_installation.date,
            'location' : detail_installation.location,
            'photo_1' : detail_installation.photo_1,
            'photo_2' : detail_installation.photo_2,
            'photo_3' : detail_installation.photo_3,
            'photo_4' : detail_installation.photo_4,
            'photo_5' : detail_installation.photo_5,
        }
        start_answer = detail_installation.start_answer
        finish_answer = detail_installation.finish_answer
    except:
        raise Http404("selected installation not found")

    try:
        start_answer = custom_translite(str(start_answer).replace("start_","")[1:][:-1].split('  '))
        finish_answer = custom_translite(str(finish_answer).replace("final_","")[1:][:-1].split('  '))

        detail_start_answer = {
            'one' : start_answer[0],
            'two' : start_answer[1],
            'three' : start_answer[2],
            'four' : start_answer[3],
            'five' : start_answer[4],
            'six' : start_answer[5],
            'seven' : start_answer[6],
        }
        detail_finish_answer = {
            'one' : finish_answer[0],
            'two' : finish_answer[1],
            'three' : finish_answer[2],
            'four' : finish_answer[3],
            'five' : finish_answer[4],
            'six' : finish_answer[5],
            'seven' : start_answer[6],
        }
        detail_answer = {
            'start' : detail_start_answer,
            'final' : detail_finish_answer,
        }
    except:
        raise Http404("not answer")
    return(detail_info,detail_answer)


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
