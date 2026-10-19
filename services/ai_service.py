import os
import time
from google import genai


class MemeAIService:
    def __init__(self):
        self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    def analyze_meme(self, filepath):
        max_retries = 3
        delay = 2

        for attempt in range(max_retries):
            try:
                uploaded_file = self.client.files.upload(file=filepath)

                prompt = (
                    "Bu bir internet geyiği (meme). "
                    "Lütfen şunları yap:\n"
                    "1. Yazıları Türkçeye çevir.\n"
                    "2. Esprisini 2-3 cümleyle açıkla."
                )

                response = self.client.models.generate_content(
                    model="gemini-3.8-flash",
                    contents=[uploaded_file, prompt],
                )

                return response.text

            except Exception as e:
                error_str = str(e)
                if (
                    ("503" in error_str or "UNAVAILABLE" in error_str)
                    and attempt < max_retries - 1
                ):
                    time.sleep(delay)
                    delay *= 2
                    continue

                return f"Yapay zeka analiz hatası: {error_str}"
