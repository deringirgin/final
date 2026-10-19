import os
from flask import Flask, redirect, render_template, request
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
from services.ai_service import MemeAIService

load_dotenv()

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp"}
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# OOP Sınıfımızı çağırıyoruz
ai_service = MemeAIService()


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

            # Yapay zeka işini ayrı servise gönderiyoruz
            ai_result = ai_service.analyze_meme(filepath)

            return render_template(
                "result.html",
                filename=filename,
                result=ai_result,
            )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
