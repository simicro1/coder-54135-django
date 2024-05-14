from django.http import HttpResponse
from django.template import Context, Template
from django.shortcuts import render


def saludo(request):
    return HttpResponse("¡Hola Django!")


def saludo_vista(request):
    return HttpResponse("<h1>Segunda vista</h1>")


def nombre(request, nombre: str, apellido: str):
    nombre = nombre.capitalize()
    apellido = apellido.capitalize()
    return HttpResponse(f"{apellido}, {nombre}")


def probando_template(request):
    mi_html = open("./templates/template1.html", encoding="UTF-8")
    mi_template = Template(mi_html.read())
    mi_html.close()
    mi_contexto = Context({"saludo": "¡Bienvenido!", "autor": "Coderhouse"})
    mi_documento = mi_template.render(mi_contexto)
    return HttpResponse(mi_documento)


def fecha_hora(request):
    from datetime import datetime

    ahora = datetime.now()
    return HttpResponse(f"<h1>⌛ Fecha y hora: {ahora:%d/%m/%Y %H:%M:%S.%f} </h1>")


def mis_notas(request):
    lista_de_notas = [2, 3, 5, 7, 9, 10, 10]
    contexto = {"notas": lista_de_notas}
    return render(request, "notas.html", contexto)


def ver_persona(request):
    formulario = {"persona": {"nombre": "Hugo", "edad": 38}}
    return render(request, "personas.html", context=formulario)
