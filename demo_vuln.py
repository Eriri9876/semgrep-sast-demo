# demo_vuln.py —— 故意写的漏洞样例，用来测试流水线会不会拦截
# 这几个都是 Semgrep 标准规则集能稳定识别的危险写法
import subprocess
import yaml
import hashlib

# 漏洞1：命令注入 —— shell=True 且拼接外部输入
def run_command(filename):
    subprocess.Popen("cat " + filename, shell=True)

# 漏洞2：不安全反序列化 —— yaml.load 不指定 SafeLoader
def load_config(raw):
    return yaml.load(raw)

# 漏洞3：危险的 eval —— 直接执行字符串
def calculate(expr):
    return eval(expr)

# 漏洞4：弱哈希算法 —— 用 MD5 处理密码
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()
