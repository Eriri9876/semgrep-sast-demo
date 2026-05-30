# ==============================================================
# XSS - 额外变体 (反射型、DOM型、属性注入等)
# CWE-79: Cross-Site Scripting
# ==============================================================

from flask import Flask, request, make_response, Response

app = Flask(__name__)


# --- 变体4: HTTP响应直接写入 ---
@app.route("/response")
def xss_response():
    user_input = request.args.get("msg")
    resp = make_response(f"<html><body>{user_input}</body></html>")
    return resp


# --- 变体5: 响应头注入XSS ---
@app.route("/header")
def xss_header():
    redirect_url = request.args.get("url")
    resp = Response("", status=302)
    resp.headers["Location"] = redirect_url
    return resp


# --- 变体6: JSON 响应中的XSS ---
@app.route("/api/user")
def xss_json():
    name = request.args.get("name")
    return {"message": f"Hello {name}", "status": "ok"}


# --- 变体7: 拼接HTML ---
@app.route("/html")
def xss_html_builder():
    name = request.args.get("name")
    html = "<h1>Welcome " + name + "</h1>"
    return html


if __name__ == "__main__":
    app.run(debug=True)
