# ==============================================================
# SQL注入 - %格式化 (应被 rule2: injection-sqli-no-param 检测)
# CWE-89: SQL Injection
# ==============================================================

import sqlite3
import mysql.connector

# --- 变体1: %s占位符 + %格式化 (核心规则匹配) ---
def unsafe_query_percent(user_input):
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM table WHERE id = %s" % user_input)  # 触发 rule2
    return cur.fetchall()


# --- 变体2: 多参数 % 格式化 ---
def unsafe_query_percent_multi(uid, name):
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE id = %s AND name = '%s'" % (uid, name))  # 触发 rule2
    return cur.fetchall()


# --- 变体3: UPDATE 使用 % 格式化 ---
def unsafe_update_percent(new_name, uid):
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    cur.execute("UPDATE users SET name = '%s' WHERE id = %s" % (new_name, uid))  # 触发 rule2
    conn.commit()


# --- 变体4: .format() 方法 ---
def unsafe_query_format(user_id):
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE id = {}".format(user_id))  # 另一种注入模式
    return cur.fetchall()


# --- 变体5: f-string 拼接 ---
def unsafe_query_fstring(user_id):
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM users WHERE id = {user_id}")  # f-string SQL注入
    return cur.fetchall()
