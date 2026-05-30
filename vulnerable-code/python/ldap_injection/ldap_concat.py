# ==============================================================
# LDAP注入 (应被 rule5: injection-ldap-concat 检测)
# CWE-90: LDAP Injection
# ==============================================================

# 模拟 ldap 模块接口
class ldap:
    @staticmethod
    def search(query):
        pass


# --- 变体1: ldap.search 拼接 (核心规则匹配) ---
def unsafe_ldap_search(username):
    ldap.search("cn=" + username)  # 触发 rule5: ldap.search("cn=" + $INPUT)


# --- 变体2: 复杂LDAP过滤器 ---
def unsafe_ldap_filter(uid):
    ldap.search("(&(uid=" + uid + ")(objectClass=person))")  # LDAP注入


# --- 变体3: DN 拼接 ---
def unsafe_ldap_dn(common_name):
    base_dn = "dc=example,dc=com"
    search_filter = "(cn=" + common_name + ")"  # LDAP注入
    ldap.search(search_filter)


# --- 变体4: 多条件OR ---
def unsafe_ldap_multi(user1, user2):
    ldap.search("(|(cn=" + user1 + ")(cn=" + user2 + "))")  # LDAP注入


# --- 变体5: 邮件属性 ---
def unsafe_ldap_mail(email):
    ldap.search("(mail=" + email + ")")  # LDAP注入
