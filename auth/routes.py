from flask import render_template, flash, redirect, url_for, Blueprint, request
from werkzeug.security import generate_password_hash
from extensions import db
from auth.models import User
from auth.utils.user import generate_user_id
# from auth.forms import RegistrationForm

auth_bp = Blueprint('auth', __name__, template_folder='templates')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Kiểm tra xem email đã tồn tại chưa
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return render_template('register.html', error="Email already exists.")

        # Tạo mã băm cho mật khẩu và tạo user_id duy nhất
        hashed_password = generate_password_hash(password)
        user_id = generate_user_id()  # Giả sử hàm này tạo user_id với cú pháp UID-001, UID-002,...

        # Tạo đối tượng User mới và thêm vào cơ sở dữ liệu
        new_user = User(user_id=user_id, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful!")
        return redirect(url_for('auth.login'))

    return render_template('register.html')