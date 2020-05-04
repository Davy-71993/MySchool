from django.shortcuts import render

def index(request):
    context = {

    }
    return render(request, 'chat/index.html', context)


def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })

 





