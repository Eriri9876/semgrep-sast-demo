# ==============================================================
# 硬编码密钥 - 数据库密码 (应被 rule9: auth-hardcoded-password 检测)
# CWE-259: Hardcoded Password
# ==============================================================

# --- 变体1: 硬编码密码 (核心规则匹配) ---
PASSWORD = "123456"  # 触发 rule9: PASSWORD = "123456"


# --- 变体2: 数据库连接密码 ---
DB_PASSWORD = "admin123"  # 数据库密码硬编码
PASSWORD = "123456"  # 另一个硬编码 (重复触发 rule9)


# --- 变体3: 配置文件中的密码 ---
config = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "root123",  # 硬编码密码
    "database": "myapp"
}


# --- 变体4: API密钥包含密码 ---
SECRET_CONFIG = {
    "api_password": "changeme",  # 硬编码
    "PASSWORD": "123456"  # 触发 rule9
}


# --- 变体5: LDAP 密码 ---
LDAP_PASSWORD = "ldap_secret_2024"
