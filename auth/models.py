from extensions import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'  # Tên bảng trong cơ sở dữ liệu

    id = db.Column(db.Integer, primary_key=True)  # Khóa chính tự động tăng
    user_id = db.Column(db.String(10), unique=True, nullable=False)  # user_id duy nhất
    email = db.Column(db.String(120), unique=True, nullable=False)  # Email, phải duy nhất
    password = db.Column(db.String(255), nullable=False)  # Mã băm mật khẩu
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)  # Khóa ngoại đến bảng roles
    is_active = db.Column(db.Boolean, default=True, nullable=False)  # Trạng thái hoạt động
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Ngày tạo tài khoản
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)  # Ngày cập nhật thông tin

    # Khai báo mối quan hệ với bảng roles
    role = db.relationship('Role', backref='users', lazy=True)

    def __repr__(self):
        return f"<User {self.user_id}>"
