from flask import Blueprint , render_template

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html")

    # @views.route("/home")
    # def home2():
    #     return "Home page"