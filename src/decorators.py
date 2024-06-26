from functools import wraps
from typing import Callable, Tuple, Any, Dict


def log(
    *, filename: str | None = None
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Logs a function call to a file or console :param filename: takes one optional argument filename, which specifies
    the path to the file where the logs will be written. If filename is not specified, the logs will be output to the
    console
    """

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Tuple[Any, ...], **kwargs: Dict[str, Any]) -> Any:
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"
                if filename:
                    with open(filename, "a") as f:
                        f.write(log_message + "\n")
                else:
                    print(log_message)
                return result
            except Exception as e:
                log_message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, "a") as f:
                        f.write(log_message)
                else:
                    print(log_message)
                raise e

        return wrapper

    return decorator
