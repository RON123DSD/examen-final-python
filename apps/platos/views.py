
from django.shortcuts import render

from apps.platos.models import Platos
def platos_list(request):



    # meseross = Meseros.objects.order_by('edad')
    platoss = Platos.objects.filter( precio__gt=40,procedencia="Peru")
    # platoss =Platos.objects.order_by('precio')

    return render(request, 'platos/templates/platos/platoss_list.html', context={'data': platoss})
