# coding=utf-8

import os
import sys

# 启动方式
# python3 manage.py runserver 0.0.0.0:8000


def main():
    # 需要设置 settings
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ncov_api.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
