import time

def retry(func, max_attempt=3, base_delay=1.0, retry_on=Exception):
    if max_attempt < 1:
        raise ValueError("max_attempt must be at least 1")
    
    for attempt in range(1, max_attempt + 1):
        try:
            return func()
        except retry_on:
            if attempt == max_attempt:
                raise
            else:
                delay = base_delay * (2 ** (attempt - 1))
                time.sleep(delay)




if __name__ == "__main__":
    calls = {"count": 0}

    def flaky():
        calls["count"] += 1
        if calls["count"] < 3:
            raise ConnectionError("fail")
        return "ok"

    print(retry(flaky, base_delay=0.1))
    print("calls made:", calls["count"])

    def always_fails():
        raise ConnectionError("fail")

    try:
        retry(always_fails, base_delay=0.1)
    except ConnectionError:
        print("raised after retries")

    def wrong_error():
        raise ValueError("not retryable")

    attempts = {"count": 0}

    def counted_wrong_error():
        attempts["count"] += 1
        raise ValueError("not retryable")

    try:
        retry(counted_wrong_error, base_delay=0.1, retry_on=ConnectionError)
    except ValueError:
        print("non retryable error stopped after", attempts["count"], "call")