from flask import Flask
from flask_bcrypt import Bcrypt
from flask_session import Session
from backend.views.home import *
from backend.views.SigninView import *
from backend.views.SignupView import *
from backend.views.cart import *
from backend.views.favourites import *
from backend.views.computers import *
from backend.views.mouse import *
from backend.views.keyboards import *
from backend.views.adminchecker import *
from backend.views.AccountStateView import *
from backend.views.AccountInfoUpdater import *
from backend.views.StaffPanel import *
from backend.views.StaffSalesView import *
from backend.views.StaffInventoryView import *
from backend.views.About import *
from backend.views.SelectPC import *
from backend.views.routes import *
from backend.views.PurchaseHistory import *

app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)


bcrypt = Bcrypt(app)
login_manager.init_app(app)
@app.context_processor
def inject_user():
    return dict(user=current_user)

SECRET_KEY = "5cc130ab569ac767ea9a5a272747592658aedfe069b91a9ab2f8d4222e97861ddddec6639feac050e6efab0274f37122617195df39b2b296881d356ec3402740d7841af0beb99dfff6fce567d124ae62626950f3ee4489dd565c814c82b2cc38bd4924302bb395ef4fb2696252eb0803a9b3f86fe2e927843aabe0b12859e6b7cada48cdb9975489f588839648ff61ab2703456f8de8e99133578640d\/-!63c63ffb776-!"

app.config['SECRET_KEY'] = SECRET_KEY

# Register Blueprints
app.register_blueprint(home_bp)
app.register_blueprint(signin_bp)
app.register_blueprint(signup_bp)
app.register_blueprint(cart_bp)
app.register_blueprint(computers_bp)
app.register_blueprint(mouse_bp)
app.register_blueprint(keyboards_bp)
app.register_blueprint(adminchecker_bp)
app.register_blueprint(accountstate_bp)
app.register_blueprint(StaffPanel_bp)
app.register_blueprint(StaffSalesView_bp)
app.register_blueprint(StaffInventoryView_bp)
app.register_blueprint(about_bp)
app.register_blueprint(selectpc_bp)
app.register_blueprint(products_bp)
app.register_blueprint(accountupdate_bp)
app.register_blueprint(favourites_bp)
app.register_blueprint(producthistory_bp)


if __name__ == '__main__':
    app.run(debug=True)