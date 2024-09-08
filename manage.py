import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_library.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Не удается импортировать Django. Убедитесь, что он установлен и "
            "доступен в переменной окружения PYTHONPATH."
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()