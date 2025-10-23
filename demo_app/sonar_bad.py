import subprocess
import hashlib
import sqlite3
import pickle

# Intentionally vulnerable examples SonarQube commonly detects
# 1) Hard-coded credential
PASSWORD = 'P@ssw0rd123!'


def vulnerable_sql(name: str):
    # 2) SQL concatenation / injection risk
    conn = sqlite3.connect(':memory:')
    conn.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)')
    conn.execute("INSERT INTO users (name) VALUES ('alice')")
    cursor = conn.cursor()
    # unsafe concatenation
    query = "SELECT id, name FROM users WHERE name = '" + name + "'"
    cursor.execute(query)
    return cursor.fetchall()


def use_eval(expr: str):
    # 3) Use of eval is dangerous
    return eval(expr)


def unsafe_pickle_loads(data: bytes):
    # 4) Using pickle.loads on untrusted data is insecure
    return pickle.loads(data)


def call_shell(user_input: str):
    # 5) Using shell=True with formatted input
    subprocess.call(f"echo {user_input}", shell=True)


def weak_hash(data: str) -> str:
    # 6) Weak hash (MD5)
    return hashlib.md5(data.encode('utf-8')).hexdigest()


def swallow_exceptions():
    # 7) Broad exception that hides errors
    try:
        1 / 0
    except Exception:
        # silently ignore
        pass


if __name__ == '__main__':
    print('PASSWORD (hard-coded):', PASSWORD)
    print("SQL result:", vulnerable_sql("alice' OR '1'='1"))
    print('eval 2+2 =>', use_eval('2+2'))
    # unsafe_pickle_loads is present but we won't call it with attacker data here
    call_shell('safe-example')
    print('md5:', weak_hash('password'))
    swallow_exceptions()
