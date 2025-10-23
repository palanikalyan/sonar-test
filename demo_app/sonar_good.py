import os
import subprocess
import hashlib
import sqlite3
from typing import List, Tuple


def get_api_key() -> str:
    # Read secret from environment (no hard-coded secrets)
    return os.environ.get('API_KEY', '')


def get_user_by_name_safe(conn: sqlite3.Connection, name: str) -> List[Tuple[int, str]]:
    # Use parameterized query to avoid injection
    cursor = conn.cursor()
    cursor.execute('SELECT id, name FROM users WHERE name = ?', (name,))
    return cursor.fetchall()


def call_shell_safe(args: list) -> int:
    # Use argument list instead of shell=True
    return subprocess.call(args)


def strong_hash(data: str) -> str:
    # Use SHA-256 instead of MD5
    return hashlib.sha256(data.encode('utf-8')).hexdigest()


def handle_specific_exceptions():
    try:
        _ = 1 / 1
    except ZeroDivisionError:
        # handle the specific expected error
        # In real code, log and recover or re-raise with context; here we return a sentinel.
        return None


def prepare_db() -> sqlite3.Connection:
    conn = sqlite3.connect(':memory:')
    conn.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)')
    conn.execute("INSERT INTO users (name) VALUES ('alice')")
    return conn


if __name__ == '__main__':
    conn = prepare_db()
    print('API_KEY present:', bool(get_api_key()))
    print('User:', get_user_by_name_safe(conn, 'alice'))
    print('Call echo:', call_shell_safe(['echo', 'Hello']))
    print('sha256:', strong_hash('password'))
    handle_specific_exceptions()
