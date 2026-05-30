# ==============================================================
# 安全的LDAP查询 (负样本 - 不应被LDAP注入规则误报)
# ==============================================================

import re


# 模拟 ldap 模块
class ldap:
    @staticmethod
    def search(query):
        pass


# --- 安全写法1: 转义特殊字符 ---
def safe_ldap_escape(username):
    # 转义LDAP特殊字符: * ( ) \ NUL
    safe_username = re.sub(r'[*()\\x00]', lambda m: '\' + hex(ord(m.group(0))), username)
    ldap.search("cn=" + safe_username)


# --- 安全写法2: 白名单验证 ---
def safe_ldap_whitelist(username):
    if not re.match(r'^[a-zA-Z0-9._-]+$', username):
        raise ValueError("Invalid username")
    ldap.search("cn=" + username)


# --- 安全写法3: 使用LDAP库的安全API ---
def safe_ldap_filter(user_input):
    # 使用 ldap3 库的过滤语法
    # from ldap3 import Server, Connection, ALL
    # conn.search('dc=example,dc=com', '(&(cn={}))'.format(escape_filter_chars(user_input)))
    pass


# --- 安全写法4: 预定义过滤器 ---
def safe_ldap_predefined(username):
    # 预先定义搜索条件模板
    search_filter = "(cn={})"
    safe_value = re.sub(r'[^a-zA-Z0-9\s]', '', username)
    ldap.search(search_filter.format(safe_value))
