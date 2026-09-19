import json
import re


from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .services.rag_pipeline import get_rag_response
from .services.tts_service import EdgeTTSService

# Natural female voice
tts_service = EdgeTTSService(voice="en-US-AvaNeural")


def chat_page(request):
    """Renders the chatbot interface."""
    return render(request, "chat.html")


def clean_for_speech(text):
    """
    Convert AI response into speech-friendly text.
    """

 # Remove markdown bullets at beginning of lines
    text = re.sub(r'^\s*[-*•]\s+', '', text, flags=re.MULTILINE)

    # Remove markdown headers
    text = re.sub(r'^#+\s*', '', text, flags=re.MULTILINE)

    # Remove bold/italic markers
    text = text.replace("**", "")
    text = text.replace("*", "")

    # Convert new lines to pauses
    text = text.replace("\n", ". ")

    # Remove repeated dots
    text = re.sub(r'\.{2,}', '.', text)

    # Clean spaces
    text = re.sub(r'\s+', ' ', text)

    # Prevent extremely long voice responses
    max_chars = 350
    if len(text) > max_chars:
        text = text[:max_chars]

        # Cut at last sentence if possible
        last_dot = text.rfind(".")
        if last_dot > 50:
            text = text[:last_dot + 1]

    return text.strip()





@csrf_exempt
def chat_api(request):
    """
    Handles user queries and returns both text and audio.
    """

    if request.method == "POST":
        
        try:
            body = json.loads(request.body)
            user_message = body.get("message")
         

            if not user_message:
                return JsonResponse(
                    {"error": "Empty message"},
                    status=400
                )

            # Get AI response
            answer = get_rag_response(user_message)

            # Create speech-friendly version
            speech_text = clean_for_speech(answer)

            # Generate audio
            try:
                audio_base64 = tts_service.generate_audio_sync(
                    speech_text
                )
            except Exception as tts_error:
                print(f"Edge TTS Error: {tts_error}")
                audio_base64 = None
          

            return JsonResponse({
                "status": "success",
                "response": answer,       # full answer shown in chat
                "audio": audio_base64     # shortened answer spoken
            })

        except Exception as e:
            return JsonResponse(
                {"error": str(e)},
                status=500
            )

    return JsonResponse(
        {"error": "Invalid request method"},
        status=400
    )
