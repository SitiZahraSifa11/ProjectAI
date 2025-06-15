# from flask import Flask, request, render_template
# import google.generativeai as genai

# # Konfigurasi API Gemini
# genai.configure(api_key="AIzaSyBMRZMAhtbe_AWQFEXeBvYf4ohqYm4LZOk")

# app = Flask(__name__)  # ✅ Perbaikan di sini
# model = genai.GenerativeModel("gemini-1.5-flash")

# @app.route("/", methods=["GET", "POST"])
# def index():
#     reply = ""
#     if request.method == "POST":
#         kebutuhan = request.form.get("kebutuhan")
#         budget = request.form.get("budget")
#         portabilitas = request.form.get("portabilitas")

#         prompt = (
#             f"Tolong berikan saya rekomendasi 3 laptop untuk kebutuhan {kebutuhan} "
#             f"dengan budget {budget} juta dan portabilitas {portabilitas}. "
#             "- Gunakan <h4> untuk nama laptop, dan tambahkan emoji laptop 💻 di depannya\n"
#             "- Spesifikasi ditulis dalam <ul> dan <li>\n"
#              "- Sertakan kelebihan dan kekurangan dalam <li>\n"
#             "- Link pembelian (atau beri saran untuk cari di marketplace)\n"
#             "Selalu Mulai dengan Halo Sobat WiserLapzone! dan font menggunakan Press Start 2P (saya sudah download), tidak perlu menambahkan catatan di akhir rekomendasi"
            
#         )


#         try:
#             response = model.generate_content(prompt)
#             reply = response.text  # langsung HTML
#         except Exception as e:
#             reply = f"<p style='color:red;'>Terjadi kesalahan: {e}</p>"

#     return render_template("main.html", reply=reply)

# # ✅ Perbaikan di sini
# if __name__ == "__main__":
#     app.run(debug=True)

# app.py
from flask import Flask, request, render_template, redirect, url_for, session
import google.generativeai as genai
import os

app = Flask(__name__)
app.secret_key = "lapzone-secret"  # Session Key

# Konfigurasi Gemini API
genai.configure(api_key="AIzaSyBMRZMAhtbe_AWQFEXeBvYf4ohqYm4LZOk")  # Ganti dengan API key Gemini Anda
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("main.html")

@app.route("/hasil", methods=["POST"])
def hasil():
    kebutuhan = request.form.get("kebutuhan")
    budget = request.form.get("budget")
    portabilitas = request.form.get("portabilitas")

    prompt = (
        f"Tolong berikan saya rekomendasi 3 laptop untuk kebutuhan {kebutuhan} "
        f"dengan budget {budget} juta dan portabilitas {portabilitas}. "
        "- Gunakan <h4> untuk nama laptop, dan tambahkan emoji laptop 💻 di depannya\n"
        "- Spesifikasi ditulis dalam <ul> dan <li>\n"
        "- Sertakan kelebihan dan kekurangan dalam <li>\n"
        "- Link pembelian (atau beri saran untuk cari di marketplace)\n"
        "Selalu Mulai dengan Halo Sobat Lapzone! dan font menggunakan Press Start 2P (saya sudah download), "
        "tidak perlu menambahkan catatan di akhir rekomendasi"
    )

    try:
        response = model.generate_content(prompt)
        session["reply"] = response.text
    except Exception as e:
        session["reply"] = f"<p style='color:red;'>Terjadi kesalahan: {e}</p>"

    return redirect(url_for("tampilkan_hasil"))

@app.route("/hasil")
def tampilkan_hasil():
    reply = session.get("reply", "")
    return render_template("hasil.html", reply=reply)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Port otomatis dari Railway
    app.run(host="0.0.0.0", port=port, debug=True)


# from flask import Flask, request, render_template, jsonify

# app = Flask(__name__)

# sensor_data = {
#     "suhu": None,
#     "status_lampu": None
# }

# @app.route("/", methods=["GET"])
# def index():
#     print("Render halaman utama dengan data:", sensor_data)
#     return render_template("main.html", suhu=sensor_data["suhu"], status_lampu=sensor_data["status_lampu"])

# @app.route("/update", methods=["POST"])
# def update():
#     try:
#         data = request.json
#         print("Data diterima (update):", data)
#         if data is None:
#             print("Data JSON kosong!")
#             return jsonify({"error": "JSON kosong"}), 400
#         sensor_data["suhu"] = data.get("suhu")
#         sensor_data["status_lampu"] = data.get("status_lampu")
#         print("Sensor data disimpan:", sensor_data)
#         return jsonify({"status": "berhasil"}), 200
#     except Exception as e:
#         print("Error:", e)
#         return jsonify({"error": str(e)}), 400

# @app.route("/debug", methods=["GET"])
# def debug():
#     print("Debug endpoint dipanggil, data sensor saat ini:", sensor_data)
#     return jsonify(sensor_data)

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000, debug=True)


# from flask import Flask, request, render_template, jsonify
# import os

# app = Flask(__name__, template_folder="templates")

# # Data sensor global
# sensor_data = {
#     "suhu": None,
#     "status_lampu": None,
#     "cahaya": None,
#     "gerbang": None
# }

# @app.route("/", methods=["GET"])
# def index():
#     return render_template("main.html", 
#         suhu=sensor_data["suhu"], 
#         status_lampu=sensor_data["status_lampu"],
#         cahaya=sensor_data["cahaya"],
#         gerbang=sensor_data["gerbang"]
#     )

# @app.route("/update", methods=["POST"])
# def update():
#     try:
#         data = request.json
#         print("Data diterima:", data)

#         if not data:
#             return jsonify({"error": "Data JSON kosong"}), 400

#         # Simpan data sensor
#         sensor_data["suhu"] = data.get("suhu")
#         sensor_data["status_lampu"] = data.get("status_lampu")
#         sensor_data["cahaya"] = data.get("cahaya")
#         sensor_data["gerbang"] = data.get("gerbang")

#         return jsonify({"status": "berhasil"}), 200

#     except Exception as e:
#         print("Error:", e)
#         return jsonify({"error": str(e)}), 400

# @app.route("/debug", methods=["GET"])
# def debug():
#     return jsonify(sensor_data)

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000, debug=True)

# from flask import Flask, request, render_template, jsonify

# app = Flask(__name__)

# sensor_data = {
#     "suhu": None,
#     "status_lampu": None
# }

# @app.route("/", methods=["GET"])
# def index():
#     return render_template("main.html", suhu=sensor_data["suhu"], status_lampu=sensor_data["status_lampu"])

# @app.route("/update", methods=["POST"])
# def update():
#     try:
#         data = request.json
#         if data is None:
#             return jsonify({"error": "JSON kosong"}), 400
#         sensor_data["suhu"] = data.get("suhu")
#         sensor_data["status_lampu"] = data.get("status_lampu")
#         print("Data diterima:", sensor_data)
#         return jsonify({"status": "berhasil"}), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 400

# @app.route("/debug", methods=["GET"])
# def debug():
#     return jsonify(sensor_data)

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000, debug=True)
