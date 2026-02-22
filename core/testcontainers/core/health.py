"""
health.py: Container Health Checks for ContainerLabPy
"""

import time
import requests

class ContainerHealthCheck:
    """
    Provides health check utilities for containers.
    """
    def __init__(self, url, timeout=30, interval=2):
        self.url = url
        self.timeout = timeout
        self.interval = interval

    def wait_for_healthy(self):
        """
        Wait until the container at self.url responds with status 200 or timeout is reached.
        """
        start = time.time()
        while time.time() - start < self.timeout:
            try:
                response = requests.get(self.url)
                if response.status_code == 200:
                    return True
            except Exception:
                pass
            time.sleep(self.interval)
        return False
