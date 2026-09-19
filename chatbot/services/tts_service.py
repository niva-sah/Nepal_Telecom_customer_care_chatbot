import edge_tts
import base64
import asyncio
from threading import Thread


class EdgeTTSService:

    def __init__(self, voice="en-US-AvaNeural"):
        self.voice = voice

    async def _text_to_base64_audio(self, text: str) -> str:

        # Slower rate sounds more natural
        communicate = edge_tts.Communicate(
            text=text,
            voice=self.voice,
            rate="-10%"
        )

        audio_data = b""

        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_data += chunk["data"]

        return base64.b64encode(audio_data).decode("utf-8")

    def generate_audio_sync(self, text: str) -> str:

        result = []

        def run_in_thread():

            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

            try:
                res = loop.run_until_complete(
                    self._text_to_base64_audio(text)
                )
                result.append(res)

            except Exception as e:
                result.append(e)

            finally:
                loop.close()

        thread = Thread(target=run_in_thread)
        thread.start()
        thread.join()

        if not result:
            return None

        if isinstance(result[0], Exception):
            print(f"[TTS Error] {result[0]}")
            return None

        return result[0]