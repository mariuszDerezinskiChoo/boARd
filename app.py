from flask import Flask, request
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'database.db'
db = SQAlchemy(app)


app.config.update(
    SECRET_KEY = 'public static void main(String[] args)'
)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

authenticated = set()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(30),unique = True)
#    def __init__(self, name):
#        self.name = name
#    def is_authenticated(self):
##        if self.name in authenticated:
##            return True
#        return False
#    def is_active(self):
#        return True
#    def is_anonymous(self):
#        return False
#    def get_id(self):
#        return self.name
#%%
@login_manager.user_loader
def user_loader(name):
    return User(name)

@login_manager.request_loader
def request_loader(req):
    return User(req.get_json()['name'])

#%%
@app.route('/login', methods = ['POST'])
def login():
    if request.get_json()['name'] in authenticated:
        return "User already logged in!"
    user = User(request.get_json()['name'])
    login_user(user)
    authenticated.add(request.get_json()['name'])
    return "logged in"

#%%     
@app.route("/logout", methods = ['POST'])
@login_required
def logout():
    logout_user()
    name = request.get_json()['name']
    if name in authenticated:
        authenticated.remove(name)
        if 'Mariusz' in authenticated:
            return "Mariusz"
    return "logged out" + "Mariusz"



@app.route("/Hello_World", methods = ['GET'])
def test():
    return "Hello World!"

@app.route("/logged_in", methods = ['POST'])
@login_required
def testing():
    return "logged in"