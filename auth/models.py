from extensions import db
from datetime import datetime


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.String(10), unique=True, nullable=False)
    role_name = db.Column(db.String(50), unique=True, nullable=False)
    allowed_modules = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f"<Role {self.role_name}>"

class User(db.Model):
    __tablename__ = 'users'  # Tên bảng trong cơ sở dữ liệu

    id = db.Column(db.Integer, primary_key=True)  # Khóa chính tự động tăng
    user_id = db.Column(db.String(10), unique=True, nullable=False)  # user_id duy nhất
    email = db.Column(db.String(120), unique=True, nullable=False)  # Email, phải duy nhất
    password = db.Column(db.String(255), nullable=False)  # Mã băm mật khẩu
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), default=1, nullable=False)  # Khóa ngoại đến bảng roles
    is_active = db.Column(db.Boolean, default=True, nullable=False)  # Trạng thái hoạt động
    created_at = db.Column(db.DateTime, default=datetime.now())  # Ngày tạo tài khoản
    updated_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())  # Ngày cập nhật thông tin

    # Khai báo mối quan hệ với bảng roles
    role = db.relationship('Role', backref='users', lazy=True)

    def __repr__(self):
        return f"<User {self.user_id}>"
