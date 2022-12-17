from django.shortcuts import render

def owner_list(request):
    # data_context={
    #     'nombre_owner':'Katty Paredes',
    #     'edad': 24,
    #     'pais': 'Perú',
    #     'dni': '12345678',
    #     'vigente': True
    # }
    # owners = [
    #      {
    #          'nombre': 'Daniel Ordeano',
    #          'edad': 20,
    #          'pais': 'Perú',
    #          'dni': '12245648',
    #          'vigente': True
    #      },
    #      {
    #          'nombre': 'Katty Paredes',
    #          'edad': 24,
    #          'pais': 'Brasil',
    #          'dni': '43340679',
    #          'vigente': True
    #      },
    #      {
    #          'nombre': 'Carlos Carbajal',
    #          'edad': 28,
    #          'pais': 'Perú',
    #          'dni': '42305699',
    #          'vigente': True
    #      },
    #      {
    #          'nombre': 'Juan Ríos',
    #          'edad': 34,
    #          'pais': 'México',
    #          'dni': '11395600',
    #          'vigente': True
    #      }
    #  ]
    """"crear un objeto para la base de datos para la tabla de owner"""
    # p=Owner(nombre="Rosmery" , pais= "España",edad="21")
    # p.save()#guarda el registro en B.D
    # p.nombre="Beatriz"
    # p.save()

    """obtener todos los elemento de una tabla en la B.D"""
    #owners = Owner.objects.all()

    """Filtración de datos: .filter()    EN LA WE B SOLO ESE NOMBRE"""
    #owners = Owner.objects.filter(nombre="Omar")
    """Filtración de datos con AND de SQL: filter()"""
    #owners = Owner.objects.filter(nombre="Rosmery", edad=28)


    """Filtración de datos más precisos con: __contains"""
    #owners = Owner.objects.filter(nombre__contains="Rosmery")

    """Filtración de datos más precisos con: __endswith()"""
    #owners = Owner.objects.filter(nombre__endswith="go")

    """Obtener un sólo dato u objeto de la tabla"""
    # owners = Owner.objects.get(dni="56238923")
    # owners = Owner.objects.get(nombre="Rossmery")
    # print("El dato es: {}".format(owners))
    # print("Tipo de dato: {}".format(type(owners)))

    """Ordenar por cualquier atributo o campo en la Base de Datos"""

    """Ordenar alfabéticamente por nombre"""
    owners=Owner.objects.order_by('edad')

    """Ordenar concatenando diferentes métodos de ORMs"""
    # owners = Owner.objects.filter(nombre="Rossmery").order_by("-edad")

    return render(request, 'owner/owners_list.html', context={'data':owners})
