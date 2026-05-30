# ==============================================================
# 不安全反序列化 - pickle (应被 rule18: config-insecure-deserialize 检测)
# CWE-502: Insecure Deserialization
# ==============================================================

import pickle
import base64


# --- 变体1: pickle.loads 直接反序列化 (核心规则匹配) ---
def unsafe_pickle_loads(data):
    obj = pickle.loads(data)  # 触发 rule18: pickle.loads($DATA)
    return obj


# --- 变体2: pickle.load 从文件 ---
def unsafe_pickle_load(filename):
    with open(filename, 'rb') as f:
        obj = pickle.load(f)  # 不安全反序列化
    return obj


# --- 变体3: base64 + pickle ---
def unsafe_pickle_b64(encoded_data):
    data = base64.b64decode(encoded_data)
    obj = pickle.loads(data)  # 触发 rule18
    return obj


# --- 变体4: cPickle ---
def unsafe_cpickle(data):
    import cPickle
    obj = cPickle.loads(data)  # Python 2 风格
    return obj


# --- 变体5: 网络接收后反序列化 ---
def unsafe_network_pickle(socket_data):
    # 模拟从网络接收数据后反序列化
    obj = pickle.loads(socket_data)  # 触发 rule18
    process(obj)
