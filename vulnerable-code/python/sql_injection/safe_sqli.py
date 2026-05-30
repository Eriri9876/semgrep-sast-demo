# ==============================================================
# 安全的SQL写法 (负样本 - 不应被任何SQL注入规则误报)
# ==============================================================

import sqlite3

# --- 安全写法1: 参数化查询 (?) ---
def safe_query_param(uid):
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE id = ?", (uid,))
    return cur.fetchall()


# --- 安全写法2: 命名参数 ---
def safe_query_named(uid):
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE id = :uid", {"uid": uid})
    return cur.fetchall()


# --- 安全写法3: ORM 方式 ---
def safe_query_orm(uid):
    # 使用 ORM 的 filter 方法
    # User.objects.filter(id=uid)
    pass


# --- 安全写法4: 存储过程 ---
def safe_query_sp(uid):
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    cur.callproc("get_user_by_id", [uid])
    return cur.fetchall()


# --- 安全写法5: 使用转义 + 白名单校验 ---
def safe_query_whitelist(table_name):
    ALLOWED_TABLES = ["users", "products", "orders"]
    if table_name not in ALLOWED_TABLES:
        raise ValueError("Invalid table name")
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table_name}")  # 经过白名单过滤
    return cur.fetchall()
