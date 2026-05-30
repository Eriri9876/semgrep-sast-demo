# ==============================================================
# 认证缺陷 - HTTP明文传输 (应被 rule11: auth-http-transport 检测)
# CWE-319: Cleartext Transmission of Sensitive Information
# ==============================================================

import requests


# --- 变体1: requests.get HTTP (核心规则匹配) ---
def unsafe_http_get(api_path):
    resp = requests.get("http://" + api_path)  # 触发 rule11: requests.get("http://" + $URL)
    return resp.json()


# --- 变体2: requests.post HTTP ---
def unsafe_http_post(url, data):
    resp = requests.post("http://" + url, json=data)  # 触发 rule11
    return resp.status_code


# --- 变体3: requests.put HTTP ---
def unsafe_http_put(resource_id, data):
    return requests.put("http://api.example.com/users/" + resource_id, json=data)


# --- 变体4: 使用 HTTP 而非 HTTPS ---
API_BASE_URL = "http://api.myservice.com/v1"  # HTTP明文


def fetch_user_data(user_id):
    return requests.get("http://" + API_BASE_URL.replace("http://", "") + "/users/" + user_id)


# --- 变体5: 忽略SSL验证 ---
def unsafe_no_ssl_verify(url):
    resp = requests.get("https://" + url, verify=False)  # 禁用SSL验证
    return resp.text
