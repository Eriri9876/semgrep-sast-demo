# demo_vuln.py —— 故意写的漏洞样例，专门用来测流水线
# 正式项目里这里会换成 E 同学靶场组造的漏洞代码
import os
import sqlite3

def get_user(user_id):
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    # 漏洞1：SQL 注入 —— 把用户输入直接拼进 SQL 语句
    query = "SELECT * FROM users WHERE id = '" + user_id + "'"
    cursor.execute(query)
    return cursor.fetchall()

def run_command(filename):
    # 漏洞2：命令注入 —— 用户输入直接塞进系统命令
    os.system("cat " + filename)

# 漏洞3：硬编码密钥
API_KEY = "sk-1234567890abcdef_hardcoded_secret"
