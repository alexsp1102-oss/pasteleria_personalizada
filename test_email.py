import smtplib, ssl
from email.message import EmailMessage

SENDER_EMAIL = "alex.s.p.11.02@gmail.com"
APP_PASSWORD = "pulr algu rroh mxur"   # App Password real de 16 caracteres
RECEIVER_EMAIL = "asandovalp003@alumno.uaememx.mx"

msg = EmailMessage()
msg["Subject"] = "Prueba directa"
msg["From"] = SENDER_EMAIL
msg["To"] = RECEIVER_EMAIL
msg.set_content("Hola Alex, este es un correo de prueba enviado fuera de Django.")

try:
    context = ssl._create_unverified_context()  # Contexto sin verificación (solo pruebas)
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls(context=context)
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.send_message(msg)

    print("✅ Correo enviado correctamente")

except Exception as e:
    print(f"❌ Error al enviar: {e}")
