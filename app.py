from flask import Flask ,  render_template
# from flask_sqlalchemy  import SQLAlchemy
# from flask_login import Usermixin , login_user , LoginManager , login_required , logout_user, current_user
# from views import views

app = Flask(__name__)
# db= SQLAlchemy(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# app.config['SECRET_KEY'] = 'Shubh1710'

# app.register_blueprint(views , url_prefix="/views")

# class User(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(20), nullable=False, unique=True)
#     password = db.Column(db.String(80), nullable=False)

@app.route("/")
def portfolio():
    return render_template('index.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/register")
def register():
    return render_template('register.html')


if __name__ =='__main__':
    app.run(debug=True, port=8000)
# 
