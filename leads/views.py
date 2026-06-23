from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Lead

def landing(request):
    if request.method == "POST":
        # Datos del formulario (acepta ambos nombres de campo)
        nombre = request.POST.get("nombre_completo") or request.POST.get("nombre")
        correo = request.POST.get("correo_electronico") or request.POST.get("correo")
        telefono = request.POST.get("telefono")
        tipo_evento = request.POST.get("tipo_evento") or request.POST.get("tipo")
        fecha_evento = request.POST.get("fecha_evento")
        numero_personas = request.POST.get("numero_personas")
        sabor = request.POST.get("sabor_interes")
        tamano = request.POST.get("tamano")
        descripcion = request.POST.get("descripcion") or request.POST.get("mensaje")
        entrega = request.POST.get("entrega_domicilio") == "on"
        privacidad = request.POST.get("acepta_privacidad") == "on"

        # 1️⃣ Guardar en la base de datos (CRM)
        Lead.objects.create(
            nombre_completo=nombre,
            telefono=telefono,
            correo_electronico=correo,
            tipo_evento=tipo_evento,
            fecha_evento=fecha_evento,
            numero_personas=numero_personas,
            sabor_interes=sabor,
            tamano=tamano,
            descripcion=descripcion,
            entrega_domicilio=entrega,
            acepta_privacidad=privacidad,
        )

        # 2️⃣ Enviar correo a TI (tu dirección institucional)
        send_mail(
            subject=f"Nueva cotización de {nombre}",
            message=(
                f"Nombre: {nombre}\n"
                f"Correo: {correo}\n"
                f"Teléfono: {telefono}\n"
                f"Tipo evento: {tipo_evento}\n"
                f"Fecha: {fecha_evento}\n"
                f"Personas: {numero_personas}\n"
                f"Sabor: {sabor}\n"
                f"Tamaño: {tamano}\n"
                f"Descripción: {descripcion}\n"
                f"Entrega domicilio: {entrega}\n"
                f"Acepta privacidad: {privacidad}"
            ),
            from_email="alex.s.p.11.02@gmail.com",  # remitente
            recipient_list=["a1exs4nd0v4lp3r3z@gmail.com"],  # institucional
            fail_silently=False,
        )

        # 3️⃣ Enviar correo automático al USUARIO
        send_mail(
            subject="Gracias por contactarnos",
            message=(
                "Hemos recibido tu solicitud de cotización. "
                "En breve te responderemos con una propuesta personalizada."
            ),
            from_email="alex.s.p.11.02@gmail.com",  # remitente
            recipient_list=[correo],
            fail_silently=False,
        )

        return redirect("gracias")

    return render(request, "leads/landing.html")


def gracias(request):
    return render(request, "leads/gracias.html")


def inicio(request):
    return render(request, "leads/inicio.html")


def contacto(request):
    return render(request, "leads/contacto.html")
