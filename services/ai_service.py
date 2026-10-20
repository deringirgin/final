import os
import time
from google import genai


class MemeAIService:
    def __init__(self):
        env_keys = os.getenv("GEMINI_API_KEYS", "")
        fallback_key = os.getenv("GEMINI_API_KEY", "")
        keys_str = env_keys if env_keys else fallback_key

        self.api_keys = [
            k.strip() for k in keys_str.split(",") if k.strip()
        ]
        self.current_key_index = 0

    def _get_client(self):
        key = self.api_keys[self.current_key_index]
        return genai.Client(api_key=key)

    def _switch_to_next_key(self):
        if len(self.api_keys) > 1:
            self.current_key_index = (self.current_key_index + 1) % len(
                self.api_keys
            )
            return True
        return False

    def analyze_meme(self, filepath):
        max_retries = len(self.api_keys) * 2

        for attempt in range(max_retries):
            try:
                client = self._get_client()
                uploaded_file = client.files.upload(file=filepath)

                prompt = (
                    "Bu bir internet geyiği (meme). "
                    "Lütfen şunları yap:\n"
                    "1. Yazıları Türkçeye çevir.\n"
                    "2. Esprisini 2-3 cümleyle açıkla."
                )

                response = client.models.generate_content(
                    model="gemini-3.8-flash",
                    contents=[uploaded_file, prompt],
                )

                return response.text

            except Exception as e:
                error_str = str(e)
                if "429" in error_str or "RESOURCE_EXHAUSTED" in error_str:
                    if self._switch_to_next_key():
                        time.sleep(1)
                        continue

                if "503" in error_str or "UNAVAILABLE" in error_str:
                    time.sleep(2)
                    continue

                return f"Yapay zeka analiz hatası: {error_str}"
