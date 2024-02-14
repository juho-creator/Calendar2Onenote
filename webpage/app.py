import json

import requests
from authlib.integrations.flask_client import OAuth
from flask import Flask, abort, redirect, render_template, session, url_for

app = Flask(__name__)

appConf = {
    "OAUTH2_CLIENT_ID": "743129496321-c74ioc7r9mnncs7c4qkahp1vuftkuo3g.apps.googleusercontent.com",
    "OAUTH2_CLIENT_SECRET": "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",
    "OAUTH2_META_URL": "https://accounts.google.com/.well-known/openid-configuration",
    "FLASK_SECRET": "854c281b-bb1c-4229-afe4-e8587afba691",
    "FLASK_PORT": 5000
}

app.secret_key = appConf.get("FLASK_SECRET")

oauth = OAuth(app)

oauth.register("myApp",
               client_id=appConf.get("OAUTH2_CLIENT_ID"),
                client_secret=appConf.get("OAUTH2_CLIENT_SECRET"),
                server_metadata_url=appConf.get("OAUTH2_META_URL"),
                client_kwargs={
                    "scope": "openid profile email https://www.googleapis.com/auth/user.birthday.read https://www.googleapis.com/auth/user.gender.read",
                }
            )



@app.route("/")
def home():
    try:
        return render_template("home.html",session=session.get("user"),
                           name =  session.get("user")["userinfo"]["name"])
    except:
        return render_template("home.html", session=session.get("user"),
                            pretty=json.dumps(session.get("user"), indent=4))


@app.route("/google-login")
def googleLogin():
    return oauth.myApp.authorize_redirect(redirect_uri=url_for("googleCallback", _external=True))

@app.route("/signin-google")
def googleCallback():
    token = oauth.myApp.authorize_access_token()
    session["user"] = token
    return redirect(url_for("home"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("home"))



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=appConf.get(
        "FLASK_PORT"), debug=True)
