# ==============================================================
# 存储型XSS (应被 rule7: xss-stored-template 检测)
# CWE-79: Cross-Site Scripting
# ==============================================================

from flask import Flask, render_template, request

app = Flask(__name__)


# --- 变体1: render_template 传递用户输入 (核心规则匹配) ---
@app.route("/stored")
def stored_xss():
    user_data = request.args.get("comment")
    return render_template("index.html", data=user_data)  # 触发 rule7: render_template("index.html", data=$USER_INPUT)


# --- 变体2: render_template 多参数 ---
@app.route("/profile")
def profile_xss():
    bio = request.form.get("bio")
    name = request.form.get("name")
    return render_template("index.html", data=bio, username=name)  # 触发 rule7


# --- 变体3: 从数据库读取后直接渲染 ---
@app.route("/post/<int:post_id>")
def post_xss(post_id):
    # 模拟从数据库读取未转义的数据
    post_content = "<script>alert('xss')</script>"
    return render_template("index.html", data=post_content)  # 触发 rule7


if __name__ == "__main__":
    app.run(debug=True)
