# ==============================================================
# 硬编码密钥 - AWS Access Key (应被 rule15: secrets-aws-hardcoded 检测)
# CWE-798: Hardcoded Credentials
# ==============================================================

import boto3

# --- 变体1: AWS Access Key 直接赋值 (核心规则匹配) ---
AWS_ACCESS_KEY = "AKIA1234567890ABCDEF"  # 触发 rule15: regex AKIA[0-9A-Z]{16}


# --- 变体2: 在函数中使用 ---
def connect_s3():
    key = "AKIAJLKJ9876543210XYZ"  # 触发 rule15
    s3 = boto3.client('s3',
                      aws_access_key_id=key,
                      aws_secret_access_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY")
    return s3


# --- 变体3: 配置文件中的密钥 ---
aws_config = {
    "access_key": "AKIAABCDEFGHIJKLMNOP",  # 触发 rule15
    "secret_key": "abcdef1234567890abcdef1234567890abcdef12",
    "region": "us-east-1"
}


# --- 变体4: 多行字符串中的密钥 ---
config_yaml = """
aws:
  access_key_id: AKIAZYXWVUTSRQPONMLK  # 触发 rule15
  secret_access_key: test123
"""
