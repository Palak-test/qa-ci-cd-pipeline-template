import unittest
from testcontainers.core.health import ContainerHealthCheck
from unittest.mock import patch

class TestContainerHealthCheck(unittest.TestCase):
    @patch('requests.get')
    def test_wait_for_healthy_success(self, mock_get):
        mock_get.return_value.status_code = 200
        hc = ContainerHealthCheck('http://localhost:8080', timeout=5, interval=1)
        self.assertTrue(hc.wait_for_healthy())

    @patch('requests.get')
    def test_wait_for_healthy_timeout(self, mock_get):
        mock_get.side_effect = Exception('Connection refused')
        hc = ContainerHealthCheck('http://localhost:8080', timeout=2, interval=1)
        self.assertFalse(hc.wait_for_healthy())

if __name__ == '__main__':
    unittest.main()
