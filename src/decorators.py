import os
from functools import wraps
from typing import Callable


def log(*, filename: str | None = None) -> Callable:
    def decorator(func):
        if filename is not None:
            current_path = os.getcwd()
            project_root = os.path.abspath(os.path.join(current_path, '..'))
            os.chdir(project_root)
            file_path = os.path.join('docs', filename)

        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"
                if filename:
                    with open(file_path, 'a') as f:
                        f.write(log_message + '\n')
                else:
                    print(log_message)
                return result
            except Exception as e:
                log_message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs} "
                if filename:
                    with open(file_path, 'a') as f:
                        f.write(log_message)
                else:
                    print(log_message)
                raise e
        return wrapper
    return decorator
