# ==============================================================
# SQL注入 - 字符串拼接 (应被 rule1: injection-sqli-concat 检测)
# CWE-89: SQL Injection
# ==============================================================

import sqlite3
import mysql.connector

# --- 变体1: 直接字符串拼接 ---
def unsafe_query_concat(user_id):
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    query = "SELECT * FROM users WHERE id = " + user_id  # 触发 rule1
    cur.execute(query)
    return cur.fetchall()


# --- 变体2: 多变量拼接 ---
def unsafe_query_multi_concat(uid, table):
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    sql = "SELECT * FROM " + table + " WHERE uid = " + uid  # 触发 rule1
    cur.execute(sql)
    return cur.fetchall()


# --- 变体3: WHERE 条件拼接 ---
def unsafe_query_where_concat(condition):
    query = "DELETE FROM users WHERE " + condition  # 触发 rule1
    conn = sqlite3.connect("test.db")
    conn.execute(query)
    conn.commit()


# --- 变体4: ORDER BY 拼接 ---
def unsafe_query_orderby_concat(sort_col):
    q = "SELECT name, email FROM users ORDER BY " + sort_col  # 触发 rule1
    conn = sqlite3.connect("test.db")
    return conn.execute(q).fetchall()


# --- 变体5: INSERT 语句拼接 ---
def unsafe_insert_concat(name, email):
    sql = "INSERT INTO users (name, email) VALUES ('" + name + "', '" + email + "')"  # 触发 rule1
    conn = sqlite3.connect("test.db")
    conn.execute(sql)
    conn.commit()
