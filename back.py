from flask import Flask, request, render_template
from flask_cors import CORS
import steamfront
import json
import settings

#CONECTA STEAM
API_KEY = settings.API_KEY
client = steamfront.Client(API_KEY)

# MEU ID
app = Flask(__name__)
CORS(app)
@app.route("/user", methods=["GET"])
def user():
    try:
        client = steamfront.Client(API_KEY)
        usuario = client.getUser(id64=request.headers["id"])
        raw = usuario.raw
        raw['total'] = usuario.app_count
        raw['games'] = usuario.raw_apps
        res = json.dumps(raw)
        response = app.response_class(
            response=res,
            status=200,
            mimetype='application/json'
        )
        return response
    except Exception as err:
        response = app.response_class(
            response=f"{err}",
            status=404,
        )
        return response
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template("index.html")

app.run(host='0.0.0.0',port=5000)