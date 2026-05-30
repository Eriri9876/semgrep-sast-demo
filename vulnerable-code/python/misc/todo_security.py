# ==============================================================
# 安全TODO标记 (应被 rule21: general-security-todo 检测)
# CWE-546: Suspicious Comment
# ==============================================================

# --- 变体1: TODO security (核心规则匹配) ---
# TODO: review security implications of this approach
# 触发 rule21: regex TODO.*security


# --- 变体2: TODO fix security ---
# TODO: fix the security vulnerability in authentication
# 触发 rule21


# --- 变体3: TODO hardcoded ---
# TODO: remove security bypass for production
def admin_bypass():
    return True


# --- 变体4: FIXME security ---
# FIXME: security issue - no input validation
def process_input(data):
    return data


# --- 变体5: HACK security ---
# HACK: security check disabled for testing
def login(username, password):
    # TODO: add proper security checks
    if username == "admin":
        return True
    return False
