from django.shortcuts import render
from .models  import Instalator,Installation

def index(request):
    Instalators = Instalator.objects.order_by('name')
    Installations = Installation.objects.order_by('id')
    all_Instalator = []
    all_Installation = []


    for Instalator_index in Instalators:
        Instalator_info = {
            'chat_id': Instalator_index.chat_id,
            'name': Instalator_index.name,
            'score': Instalator_index.score,
        }
        all_Instalator.append(Instalator_info)

    for Installation_index in Installations:
        Installation_info = {
            'id' : Installation_index.id,
            'location' : Installation_index.location,
            'Instalator_name' : Installation_index.Instalator_id.name,
            'date' : Installation_index.date,
            'answer' : Installation_index.answer,
        }
        all_Installation.append(Installation_info)


    print(all_Instalator)
    print(all_Installation)

    return render(
        request,
        'index.html',
        {
        'Instalator_info':all_Instalator,
        'Installation_info':all_Installation,
        },
    )
