# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'HPX Cookbook'
copyright = '2019, Yorlik, https://github.com/McKillroy/hpx_snippets'
author = 'Yorlik'

# The full version, including alpha/beta/rc tags
release = '0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
   'breathe',
    #'exhale',
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.autosectionlabel',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# Tell sphinx what the primary language being documented is.
primary_domain = 'cpp'
default_domain = 'cpp'

# Tell sphinx what the pygments highlight language should be.
highlight_language = 'cpp'

# pygment styles:
# ['default', 'emacs',    'friendly', 'colorful',     'autumn', 'murphy',        'manni',        'monokai', 
#  'perldoc', 'pastie',   'borland',  'trac',         'native', 'fruity',        'bw',           'vim', 
#  'vs',      'tango',    'rrt',      'xcode',        'igor',   'paraiso-light', 'paraiso-dark', 'lovelace', 
#  'algol',   'algol_nu', 'arduino',  'rainbow_dash', 'abap']
# best: tango, rainbow_dash, abap
pygments_style = 'default'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
##########################################################################
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'canonical_url': '',
    'analytics_id': '',  #  Provided by Google in your dashboard
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    #'vcs_pageview_mode': '',
    'style_nav_header_background': '#2980B9',
    # Toc options
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}
##########################################################################
# html_theme = 'agogo'
# html_theme = 'classic'
#html_theme = 'alabaster'
##########################################################################
# import guzzle_sphinx_theme
# html_theme_path = guzzle_sphinx_theme.html_theme_path()
# html_theme = 'guzzle_sphinx_theme'
# html_theme_options = {
#     # Set the name of the project to appear in the sidebar
#     "project_nav_name": "HPX Cookbook",
# }
## ##########################################################################
## import sphinx_bootstrap_theme
## html_theme = 'bootstrap'
## html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
## # Theme options are theme-specific and customize the look and feel of a
## # theme further.
## html_theme_options = {
##     # Navigation bar title. (Default: ``project`` value)
##     'navbar_title': "HPX Cookbook",
## 
##     # Tab name for entire site. (Default: "Site")
##     'navbar_site_name': "Site",
## 
##     # A list of tuples containing pages or urls to link to.
##     # Valid tuples should be in the following forms:
##     #    (name, page)                 # a link to a page
##     #    (name, "/aa/bb", 1)          # a link to an arbitrary relative url
##     #    (name, "http://example.com", True) # arbitrary absolute url
##     # Note the "1" or "True" value above as the third argument to indicate
##     # an arbitrary url.
##     'navbar_links': [
##         ("Examples", "examples"),
##         ("Link", "http://example.com", True),
##     ],
## 
##     # Render the next and previous page links in navbar. (Default: true)
##     'navbar_sidebarrel': True,
## 
##     # Render the current pages TOC in the navbar. (Default: true)
##     'navbar_pagenav': True,
## 
##     # Tab name for the current pages TOC. (Default: "Page")
##     'navbar_pagenav_name': "Page",
## 
##     # Global TOC depth for "site" navbar tab. (Default: 1)
##     # Switching to -1 shows all levels.
##     'globaltoc_depth': 2,
## 
##     # Include hidden TOCs in Site navbar?
##     #
##     # Note: If this is "false", you cannot have mixed ``:hidden:`` and
##     # non-hidden ``toctree`` directives in the same page, or else the build
##     # will break.
##     #
##     # Values: "true" (default) or "false"
##     'globaltoc_includehidden': "true",
## 
##     # HTML navbar class (Default: "navbar") to attach to <div> element.
##     # For black navbar, do "navbar navbar-inverse"
##     'navbar_class': "navbar navbar-inverse",
## 
##     # Fix navigation bar to top of page?
##     # Values: "true" (default) or "false"
##     'navbar_fixed_top': "true",
## 
##     # Location of link to source.
##     # Options are "nav" (default), "footer" or anything else to exclude.
##     'source_link_position': "nav",
## 
##     # Bootswatch (http://bootswatch.com/) theme.
##     #
##     # Options are nothing (default) or the name of a valid theme
##     # such as "cosmo" or "sandstone".
##     #
##     # The set of valid themes depend on the version of Bootstrap
##     # that's used (the next config option).
##     #
##     # Currently, the supported themes are:
##     # - Bootstrap 2: https://bootswatch.com/2
##     # - Bootstrap 3: https://bootswatch.com/3
##     'bootswatch_theme': "sandstone",
## 
##     # Choose Bootstrap version.
##     # Values: "3" (default) or "2" (in quotes)
##     'bootstrap_version': "3",
## }
##########################################################################


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
