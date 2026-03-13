from flask import Flask, request, send_from_directory, jsonify
import os
import uuid

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    file_id = str(uuid.uuid4())
    filename = file_id + "_" + file.filename
    filepath = os.path.join(UPLOAD_FOLDER, filename)

    file.save(filepath)

    return jsonify({"message": "File uploaded", "file_id": file_id})


@app.route("/download/<file_id>", methods=["GET"])
def download_file(file_id):

    for file in os.listdir(UPLOAD_FOLDER):
        if file.startswith(file_id):
            return send_from_directory(UPLOAD_FOLDER, file, as_attachment=True)

    return jsonify({"error": "File not found"}), 404


if __name__ == "__main__":
    app.run(port=5001, debug=True)