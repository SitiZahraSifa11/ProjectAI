from flask import Flask, request, render_template
import google.generativeai as genai
import markdown 
# Masukkan API Key Gemini
genai.configure(api_key="AIzaSyBdmZCJuwCJuIiL9HEvSX-mheeGfJ672mc")

app = Flask(__name__)
model = genai.GenerativeModel("gemini-2.0-flash")

@app.route("/", methods=["GET", "POST"])
def index():
    reply = ""
    if request.method == "POST":
        kebutuhan = request.form["kebutuhan"]
        budge = request.form["budget"]
        portabilitas = request.form["portabilitas"]

        prompt = (
            f"Halo Sobat Wiser! Tolong berikan saya rekomendasi 3 laptop untuk kebutuhan {kebutuhan} "
            f"dengan budget {budget} juta dan portabilitas {portabilitas}. "
            f"Format markdown, info lengkap seperti:\n"
            "- Nama laptop\n"
            "- Gambar laptop\n"
            "- Spesifikasi (CPU, RAM, Storage, GPU, Berat, Harga)\n"
            "- Kelebihan & kekurangan\n"
            "- Cocok untuk siapa\n"
            "- Link pembelian (Tokopedia/Shopee)\n"
            "Tampilkan dengan rapi ya."
        )

        response = model.generate_content(prompt)
        reply_raw = response.text
        reply = markdown.markdown(reply_raw)

    return render_template("index.html", reply=reply)

if __name__ == "__main__":
    app.run(debug=True)