# ==============================================================
# 安全的XSS防护写法 (负样本 - 不应被XSS规则误报)
# ==============================================================

from flask import Flask, render_template, escape, Markup
import html

app = Flask(__name__)


# --- 安全写法1: HTML转义 ---
def safe_xss_escape(user_input):
    safe_output = html.escape(user_input)
    print(safe_output)  # 已转义，安全


# --- 安全写法2: Markup 标记安全内容 ---
def safe_xss_markup(content):
    safe_content = Markup.escape(content)
    return safe_content


# --- 安全写法3: 使用 escape() ---
@app.route("/safe")
def safe_xss():
    name = escape(request.args.get("name", ""))
    return f"<h1>Hello {name}</h1>"


# --- 安全写法4: 白名单过滤 ---
def safe_xss_whitelist(user_input):
    import re
    # 只允许字母数字和空格
    safe = re.sub(r'[^a-zA-Z0-9\s]', '', user_input)
    print(safe)


# --- 安全写法5: render_template 传递转义后的数据 ---
@app.route("/safe-template")
def safe_template():
    from markupsafe import escape
    user_data = escape(request.args.get("comment", ""))
    return render_template("index.html", data=user_data)  # 已转义
