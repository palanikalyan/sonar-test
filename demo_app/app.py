import os
import subprocess
import hashlib


def get_secret_from_env():
    # Intentional insecure practice: reading a secret from env and echoing
    secret = os.environ.get('API_SECRET', 'default_secret')
    print('Using secret:', secret)
    return secret


def run_shell(cmd):
    # Intentional insecure practice: shell=True and formatted command
    subprocess.call(f"echo Running: {cmd} && {cmd}", shell=True)


def compute_md5(data: str) -> str:
    # Weak hash used intentionally for demo
    return hashlib.md5(data.encode('utf-8')).hexdigest()


def main():
    s = get_secret_from_env()
    print('MD5 of secret:', compute_md5(s))
    # Unsafe shell execution
    run_shell('dir' if os.name == 'nt' else 'ls -la')


if __name__ == '__main__':
    main()
