# ==============================================================
# 安全的反序列化写法 (负样本 - 不应被反序列化规则误报)
# ==============================================================

import yaml
import json
import pickle


# --- 安全写法1: yaml.safe_load ---
def safe_yaml_load(yaml_str):
    data = yaml.safe_load(yaml_str)  # 安全的YAML加载
    return data


# --- 安全写法2: yaml.load with SafeLoader ---
def safe_yaml_safe_loader(yaml_str):
    data = yaml.load(yaml_str, Loader=yaml.SafeLoader)  # 使用SafeLoader
    return data


# --- 安全写法3: JSON 替代 pickle ---
def safe_json_deserialize(json_str):
    data = json.loads(json_str)  # JSON 是安全的
    return data


# --- 安全写法4: pickle 仅用于受信任数据 ---
def safe_pickle_trusted(filepath):
    # 仅当数据来源可信时使用pickle，且有签名验证
    with open(filepath, 'rb') as f:
        data = f.read()
    # verify_signature(data)  # 先验证签名
    obj = pickle.loads(data)
    return obj


# --- 安全写法5: 使用安全的序列化格式 ---
def safe_protobuf(data):
    # 使用 protobuf / msgpack 等安全格式
    import msgpack
    obj = msgpack.unpackb(data)
    return obj
