# ==============================================================
# 硬编码密钥 - API Key / Token (额外变体)
# CWE-798: Hardcoded Credentials
# ==============================================================

import requests

# --- 变体1: GitHub Token ---
GITHUB_TOKEN = "ghp_1A2b3C4d5E6f7G8h9I0jK1lM2nO3pQ4r5S6t"  # GitHub Personal Access Token


# --- 变体2: OpenAI API Key ---
OPENAI_API_KEY = "sk-proj-ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdef"  # OpenAI密钥


# --- 变体3: Stripe Secret Key ---
STRIPE_SECRET = "sk_live_51H3xYzAbCdEfGhIjKlMnOpQrStUvWxYz1234"  # Stripe密钥


# --- 变体4: JWT Secret ---
JWT_SECRET = "my-super-secret-jwt-key-1234567890"  # JWT签名密钥


# --- 变体5: 数据库连接字符串 ---
DATABASE_URL = "postgresql://admin:password123@localhost:5432/mydb"  # 数据库密码硬编码


# --- 变体6: 第三方服务密钥 ---
SENDGRID_API_KEY = "SG.abcdefghijklmnopqrstuvwxyz.1234567890"  # SendGrid API Key
