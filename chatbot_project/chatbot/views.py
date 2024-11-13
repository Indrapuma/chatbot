from django.shortcuts import render
from django.http import JsonResponse
from .models import Chat  # Opsional, hanya jika menyimpan riwayat chat

def chatbot_response(message):
    """Logika sederhana untuk respons chatbot"""
    
    if "hai" in message.lower():
        return "Halo! Ada yang bisa saya bantu?"
    elif "terima kasih" in message.lower():
        return "Sama-sama! Senang bisa membantu Anda."
    else:
        return "Maaf, saya tidak mengerti. Bisa diulangi?"

def chat_view(request):
    if request.method == "POST":
        user_message = request.POST.get('message')
        bot_response = chatbot_response(user_message)

        # Simpan ke database (opsional)
        Chat.objects.create(user_message=user_message, bot_response=bot_response)

        return JsonResponse({"response": bot_response})
    return render(request, "chatbot/chat.html")
