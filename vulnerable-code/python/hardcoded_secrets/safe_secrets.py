# ==============================================================
# 安全的密钥管理 (负样本 - 不应被硬编码密钥规则误报)
# ==============================================================

import os

# --- 安全写法1: 从环境变量读取 ---
def safe_env_var():
    aws_key = os.environ.get("AWS_ACCESS_KEY_ID")
    api_key = os.getenv("API_KEY")
    return aws_key, api_key


# --- 安全写法2: 使用密钥管理服务 ---
def safe_secret_manager():
    # 使用 AWS Secrets Manager / HashiCorp Vault
    # secret = vault_client.read("secret/database")
    pass


# --- 安全写法3: 从配置文件(非代码)读取 ---
def safe_config_file():
    import json
    with open("/etc/app/config.json") as f:
        config = json.load(f)
    return config.get("api_key")


# --- 安全写法4: .env 文件 ---
def safe_dotenv():
    from dotenv import load_dotenv
    load_dotenv()
    db_password = os.getenv("DB_PASSWORD")
    return db_password


# --- 安全写法5: 使用临时凭证 ---
def safe_temp_credentials():
    import boto3
    # 使用 IAM Role 而非硬编码密钥
    sts = boto3.client('sts')
    temp_creds = sts.assume_role(
        RoleArn="arn:aws:iam::123456789012:role/MyRole",
        RoleSessionName="temp_session"
    )
    return temp_creds['Credentials']
