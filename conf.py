# ContainerLabPy Documentation Build Configuration

# Sphinx configuration file for ContainerLabPy documentation

project = "ContainerLabPy"
copyright = "2026, ContainerLabPy Team"
author = "ContainerLabPy Team"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon"
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "alabaster"
