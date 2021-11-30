from flask import Flask, request, send_file
from flask_cors import CORS, cross_origin
from Model import MakePred
import os 



app = Flask(__name__)
CORS(app)



# @socketio.on('text_added', namespace='/')
# def Eval(text: str):
#     text = re.sub("[^a-zA-Z]", " ", text)
#     results = MakePred(text)
#     socketio.emit('sentiments_changed', results, namespace='/')

@cross_origin()
@app.route("/sentiment", methods = ["POST"])
def Eval():
    text = request.json["text"]
    return {"sentiments": MakePred(text)}
    
@app.route("/about", methods = ["GET"])
def serveAbout():
    return send_file(f"build/index.html")
@app.route("/static/media/<filename>", methods = ["GET"])
def serveAssets(filename):
    if os.path.isfile(f"build/static/media/{filename}"):
        return send_file(f"build/static/media/{filename}")
    return ""
@app.route("/static/js/<filename>", methods = ["GET"])
def serveJs(filename):
    if os.path.isfile(f"build/static/js/{filename}"):
        return send_file(f"build/static/js/{filename}")
    return ""
@app.route("/static/css/<filename>", methods = ["GET"])
def serveCss(filename):
    if os.path.isfile(f"build/static/css/{filename}"): 
        return send_file(f"build/static/css/{filename}")
    return ""
@app.route("/<filename>", methods = ["GET"])  
def serveFiles(filename):
    if os.path.isfile(f"build/{filename}"):
        return send_file(f"build/{filename}")
    return ""

@app.route("/", methods = ["GET"])
def serveHome():
    return send_file(f"build/index.html")



if __name__ == "__main__":
    app.debug = True
    app.run(port=5001)