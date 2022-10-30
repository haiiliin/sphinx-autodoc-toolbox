===========
Basic Usage
===========

Installation
------------

To install the package, run the following command::

    pip install sphinx-autodoc-toolbox

This will install the package and its dependencies.

Extensions
----------

Collapsible members
~~~~~~~~~~~~~~~~

To use the collapsible members for autoclass, add the following to your Sphinx configuration file::

    extensions = [
        'sphinx_autodoc_toolbox.collapse',
    ]

Then, in your documentation, use the `autodoc` directives to generate the docs just as you would normally. 
below if an example incorporating with the `autoclasstoc <https://github.com/kalekundert/autoclasstoc>`_ extension:

.. autoclass:: example.Example
    :members:
    :private-members:
    :special-members:

    .. autoclasstoc::
