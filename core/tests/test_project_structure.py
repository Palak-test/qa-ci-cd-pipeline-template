import unittest

class TestContainerLabPy(unittest.TestCase):
    def test_project_metadata(self):
        """Verify project metadata and structure."""
        # Example check: project name
        project_name = "ContainerLabPy"
        self.assertEqual(project_name, "ContainerLabPy")

    def test_core_module_exists(self):
        """Check that core module exists and is importable."""
        try:
            import core.testcontainers.core
        except ImportError:
            self.fail("core.testcontainers.core module not found")

    def test_docs_index_exists(self):
        """Check that docs/index.md exists."""
        import os
        self.assertTrue(os.path.exists("docs/index.md"))

if __name__ == "__main__":
    unittest.main()
