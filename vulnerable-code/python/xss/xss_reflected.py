# ==============================================================
# 反射型XSS (应被 rule6: xss-reflected-print 检测)
# CWE-79: Cross-Site Scripting
# ==============================================================

from flask import Flask, request
import cgi

app = Flask(__name__)


# --- 变体1: print 直接输出用户输入 (核心规则匹配) ---
def xss_print_direct():
    user_input = request.args.get("name")
    print(user_input)  # 触发 rule6: print($USER_INPUT)


# --- 变体2: print 多参数 ---
def xss_print_multi():
    comment = request.form.get("comment")
    print("用户评论:", comment)  # XSS - 用户输入直接打印


# --- 变体3: print + HTML标签 ---
def xss_print_html():
    msg = request.args.get("msg")
    print("<div>" + msg + "</div>")  # XSS - 反射到HTML


@app.route("/reflect")
def reflect_xss():
    name = request.args.get("name", "")
    print(name)  # 触发 rule6
    return f"<h1>Hello {name}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
