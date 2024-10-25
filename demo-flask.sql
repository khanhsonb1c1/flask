CREATE DATABASE demo_flask;


CREATE TABLE roles (
    id INT PRIMARY KEY IDENTITY(1,1),
    role_id VARCHAR(10) UNIQUE NOT NULL,
    role_name NVARCHAR(50),
    allowed_modules NVARCHAR(MAX)
);

INSERT INTO roles (role_id, role_name, allowed_modules)
VALUES 
('ROL-001', 'Admin', 'dashboard,users,settings'),
('ROL-002','User', 'dashboard');


select * from roles
drop table roles
drop table users


CREATE TABLE users (
    id INT PRIMARY KEY IDENTITY(1,1),
	user_id VARCHAR(10) UNIQUE NOT NULL,
    email NVARCHAR(120) NOT NULL UNIQUE,  -- Email, phải duy nhất
    password NVARCHAR(255) NOT NULL,  -- Mã băm mật khẩu
    role_id INT NOT NULL,  -- Khóa ngoại, liên kết với bảng roles
    is_active BIT NOT NULL DEFAULT 1,  -- Trạng thái hoạt động của tài khoản
    created_at DATETIME DEFAULT GETDATE(),  -- Ngày tạo tài khoản
    updated_at DATETIME DEFAULT GETDATE(),  -- Ngày cập nhật thông tin
    CONSTRAINT FK_role FOREIGN KEY (role_id) REFERENCES roles(id)  -- Khóa ngoại tham chiếu bảng roles
);