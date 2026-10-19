import os
from google import genai


class MemeAIService:
    def __init__(self):
        # Gemini istemcisini sınıf başladığında hazırlıyoruz
        self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    def analyze_meme(self, filepath):
        try:
            # Dosyayı yüklüyoruz
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
            return f"Yapay zeka analiz hatası: {str(e)}"
