# ==============================================================
# 不安全反序列化 - YAML (应被 rule19: config-yaml-unsafe-load 检测)
# CWE-502: Insecure Deserialization
# ==============================================================

import yaml


# --- 变体1: yaml.load 不安全加载 (核心规则匹配) ---
def unsafe_yaml_load(yaml_str):
    data = yaml.load(yaml_str)  # 触发 rule19: yaml.load($DATA)
    return data


# --- 变体2: yaml.load 从文件 ---
def unsafe_yaml_load_file(filename):
    with open(filename, 'r') as f:
        data = yaml.load(f)  # 触发 rule19
    return data


# --- 变体3: yaml.load 指定 Loader ---
def unsafe_yaml_loader(yaml_str):
    data = yaml.load(yaml_str, Loader=yaml.Loader)  # 仍然不安全
    return data


# --- 变体4: yaml.load_all ---
def unsafe_yaml_load_all(yaml_str):
    for doc in yaml.load_all(yaml_str):  # 不安全
        process(doc)


# --- 变体5: 网络接收 YAML ---
def unsafe_network_yaml(request_data):
    config = yaml.load(request_data)  # 触发 rule19
    return config
