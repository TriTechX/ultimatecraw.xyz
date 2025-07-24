from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify, Response
import httpx
from flask_login import LoginManager, UserMixin, AnonymousUserMixin, login_user, logout_user, login_required, current_user
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["500 per hour"]
)

app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1)
app.secret_key = "crawcodesmells"

@app.route("/ads.txt")
def ads_txt():
    return send_from_directory("static", "ads.txt", mimetype="text/plain")

@app.route("/")
def landing_page():
    return render_template("landing.html")

@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for("landing_page"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
