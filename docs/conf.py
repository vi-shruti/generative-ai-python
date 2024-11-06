import re
from sphinx.util import logging

logger = logging.getLogger(__name__)

project = 'Google Generative AI - Python'
copyright = '2024, Google LLC'
author = 'Google LLC'

extensions = [
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.coverage',
    'myst_parser',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    ]

myst_url_schemes = ["http", "https", "mailto"]
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "fieldlist",
    "html_image",
    "replacements",
    "smartquotes",
    "strikethrough",
    "tasklist",
    "substitution"
]

source_suffix = {'.md': 'markdown',}
master_doc = 'index'  # Changed in version 2.0: Default is 'index' (previously 'contents').

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'alabaster'
# html_static_path = ['_static']

# def set_relative_links(app, docname, source):
#     source[0] = source[0].replace(
#         '../google/generativeai/',
#         '/api/google/generativeai/'
#     )


# def setup(app):
#     app.connect('source-read', set_relative_links)




def update_internal_links(app, docname, source):
    def replace_link(match):
        path = match.group(1)
        anchor = match.group(2) or ''
        if path.endswith('.md'):
            path = path[:-3] + '.html'
        return f'/generative-ai-python{path}{anchor}'

    def replace_relative_path(match):
        return '/api/google/generativeai/'

    # Pattern for links with potential anchors
    link_pattern = r'(/api/google/generativeai/[\w-]+)(\.md)?(#[\w-]+)?'
    # Pattern for relative paths
    path_pattern = r'\.\.\/google\/generativeai\/'

    # Replace links
    source[0] = re.sub(link_pattern, replace_link, source[0])
    # Replace relative paths
    source[0] = re.sub(path_pattern, replace_relative_path, source[0])

def setup(app):
    app.connect('source-read', update_internal_links)