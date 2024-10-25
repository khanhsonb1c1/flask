from extensions import db
from sqlalchemy import func
from auth.models import User


def generate_user_id():
    # Tìm user_id lớn nhất
    latest_user_id = db.session.query(func.max(User.user_id)).scalar()

    # Kiểm tra nếu chưa có user nào trong db
    if not latest_user_id:
        return "UID-001"

    # Tách phần số và tăng lên 1
    latest_number = int(latest_user_id.split("-")[1])
    new_number = latest_number + 1

    # Format lại user_id với độ dài tối thiểu là 3 chữ số
    return f"UID-{new_number:03d}"
