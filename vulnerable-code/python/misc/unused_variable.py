# ==============================================================
# 未使用变量 (应被 rule22: general-unused-variable 检测)
# CWE-563: Unused Variable
# ==============================================================

# --- 变体1: 分配后未使用 (核心规则匹配) ---
def unused_var_simple():
    result = expensive_computation()  # 触发 rule22: $VAR = $VALUE ... $FUNC(...)
    process_something()
    # result 未被使用


# --- 变体2: 多个未使用变量 ---
def unused_var_multi(x, y):
    temp = x + y
    debug_val = str(temp)
    save_to_db()  # 触发 rule22
    # temp, debug_val 未使用


# --- 变体3: 异常处理后未使用 ---
def unused_var_exception():
    error_msg = "Operation failed"
    try:
        risky_operation()
    except Exception:
        log_error()  # 触发 rule22
    # error_msg 未使用


# --- 变体4: 资源分配后未使用 ---
def unused_var_resource(filename):
    file_data = open(filename).read()
    cleanup_resources()  # 触发 rule22
    # file_data 未使用


# --- 变体5: 计算结果丢弃 ---
def unused_var_computation(a, b):
    checksum = hashlib.md5((a + b).encode()).hexdigest()
    send_data(b)  # 触发 rule22
    # checksum 未使用
