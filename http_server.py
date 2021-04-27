import os

from flask import Flask, jsonify, request
from gevent.pywsgi import WSGIServer

from ftp.ftp_client import FTPClient

app = Flask(__name__)


@app.route("/do-not-call-this-function", methods=['POST'])
def doNotCallThisFunction():
    data = request.get_json()

    if not data or not data["image"]:
        return jsonify({"error": "required parameter not found."})

    image = data["image"]

    if not os.path.isfile(image):
        return jsonify({"error": "image not exists. request image: {0}".format(image)})

    if not os.access(image, os.R_OK):
        return jsonify({"error": "read permission deny. request image: {0}".format(image)})

    idx = image.rfind('/') + 1
    path = image[:idx]
    if not os.access(path, os.W_OK):
        return jsonify({"error": "write permission deny. save path: {0}".format(path)})

    return jsonify()


@app.route("/upload", methods=['POST'])
def upload():
    data = request.get_json()

    ftpClient = FTPClient()
    ftpClient.upload(data['remoteDir'],
                     data['remoteFileName'], data['remoteFileData'])

    return jsonify({'code': 0, 'msg': 'ok'})


@app.route("/download", methods=['POST'])
def download():
    data = request.get_json()

    ftpClient = FTPClient()
    remoteFileData = ftpClient.download(
        data['remoteDir'], data['remoteFileName'])

    return jsonify({'code': 0, 'msg': 'ok', 'remoteFileData': remoteFileData})


if __name__ == '__main__':
    http_server = WSGIServer(('127.0.0.1', 5000), app)
    http_server.serve_forever()
