# ==============================================================
# 硬编码密钥 - SSH Private Key (应被 rule16: secrets-ssh-private-key 检测)
# CWE-798: Hardcoded Credentials
# ==============================================================

# --- 变体1: SSH 私钥直接嵌入代码 (核心规则匹配) ---
SSH_PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----  # 触发 rule16
MIIEpAIBAAKCAQEA0Z3VS2H3JqG8x7pL5mN9tR2wKfV4hB6jC8dE9sA1mN3oP5q
R7wT2xY6zA8bC0dE1fG3hI4jK5lM6nO7pQ8rS9tU1vW2xY3zA4bC5dE6fG7hI8
jK9lM0nO1pQ2rS3tU4vW5xY6zA7bC8dE9fG0hI1jK2lM3nO4pQ5rS6tU7vW8xY9
...
-----END RSA PRIVATE KEY-----"""


# --- 变体2: 函数中返回私钥 ---
def get_ssh_key():
    return """-----BEGIN RSA PRIVATE KEY-----  # 触发 rule16
MIIEogIBAAKCAQEAvN8qW3mK5oP2xT7sR8uV0wY1zA4bC5dE6fG7hI8jK9lM0nO
pQrS2tU3vW4xY5zA6bC7dE8fG9hI0jK1lM2nO3pQ4rS5tU6vW7xY8zA9bC0dE1f
G2hI3jK4lM5nO6pQ7rS8tU9vW0xY1zA2bC3dE4fG5hI6jK7lM8nO9pQ0rS1tU2vW
-----END RSA PRIVATE KEY-----"""


# --- 变体3: DSA 私钥格式 ---
DSA_KEY = "-----BEGIN DSA PRIVATE KEY-----\nMIIBvAIBAAKBgQD..."

# --- 变体4: OpenSSH 格式 ---
OPENSSH_KEY = "-----BEGIN OPENSSH PRIVATE KEY-----\nb3BlbnNzaC1rZXktdjEAAAAA..."
