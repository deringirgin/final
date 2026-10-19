import os
from flask import Flask, redirect, render_template, request
from google import genai
from werkzeug.utils import secure_filename
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp"}
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]

        if file.filename == "":
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
            filepath = os.path.join(
                app.config["UPLOAD_FOLDER"], filename
            )
            file.save(filepath)

            try:
                with open(filepath, "rb") as f:
                    uploaded_file = client.files.upload(file=f)

                prompt = (
                    "Bu bir internet geyiği (meme). "
                    "Lütfen şunları yap:\n"
                    "1. Yazıları Türkçeye çevir.\n"
                    "2. Esprisini 2-3 cümleyle açıkla."
                )

                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=[uploaded_file, prompt],
                )

                ai_result = response.text

            except Exception as e:
                ai_result = f"Hata oluştu: {str(e)}"

            return render_template(
                "result.html",
                filename=filename,
                result=ai_result,
            )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
