from flask import render_template, flash, redirect, url_for, Blueprint
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
    # form = RegistrationForm()
    # if form.validate_on_submit():
    #     email = form.email.data
    #     password = form.password.data
    #     role_id = form.role_id.data
    #
    #     # Kiểm tra email đã tồn tại chưa
    #     if User.query.filter_by(email=email).first():
    #         flash('Email đã được sử dụng. Vui lòng chọn email khác.', 'danger')
    #         return redirect(url_for('auth.register'))
    #
    #     # Tạo user_id mới
    #     user_id = generate_user_id()  # Cần định nghĩa hàm này
    #
    #     # Băm mật khẩu
    #     hashed_password = generate_password_hash(password)
    #
    #     # Tạo người dùng mới
    #     new_user = User(user_id=user_id, email=email, password=hashed_password, role_id=role_id)
    #     db.session.add(new_user)
    #     db.session.commit()
    #     flash('Đăng ký thành công!', 'success')
    #     return redirect(url_for('auth.login'))  # Redirect đến trang đăng nhập

    return render_template('register.html', form=form)
