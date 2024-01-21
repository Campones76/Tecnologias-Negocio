# backend/views/home.py
from flask import Blueprint, render_template

selectpc_bp = Blueprint('SelectPC', __name__)

@selectpc_bp.route('/computers/Lenovo/Lenovo_IdeaPad_Slim_3')
def lenovo():
    return render_template('pc_lenovo.html')

@selectpc_bp.route('/computers/Asus/ASUS_TUF_Gaming_F15')
def asus():
    return render_template('pc_asus.html')

@selectpc_bp.route('/computers/Apple/Macbook_M1')
def apple():
    return render_template('pc_macbook.html')