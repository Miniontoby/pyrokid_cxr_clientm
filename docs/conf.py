# -- Path setup ----------------------------------------
import os
import sys
sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -------------------------------
project = 'pyrokid_crx_clientm'
copyright = '2025, Miniontoby'
author = 'Miniontoby'

# -- General configuration -----------------------------
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output ---------------------------
html_theme = 'alabaster'
