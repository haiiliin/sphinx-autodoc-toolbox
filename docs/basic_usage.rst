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
~~~~~~~~~~~~~~~~~~~

To use the collapsible members for autoclass, add the following to your Sphinx configuration file::

    extensions = [
        'sphinx_autodoc_toolbox.collapse',
    ]

Then, in your documentation, use the `autodoc` directives to generate the docs just as you would normally. 
below if an example incorporating with the `autoclasstoc <https://github.com/kalekundert/autoclasstoc>`_ extension:

.. autoclass:: example.Parent
    :members:
    :private-members:
    :special-members:

    .. autoclasstoc::

.. autoclass:: example.Child
    :members:
    :private-members:
    :special-members:

    .. autoclasstoc::

Cross references to Python objects with multiple targets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can use the following syntax to create a cross reference to multiple targets, only the first target that exists will be rendered::

    :py:class:`example.Parent|example.Unknown`
    :py:class:`example.Unknown|example.Parent`

The above two snippets will render as :py:class:`example.Parent|example.Unknown` and :py:class:`example.Unknow|example.Parent`. To use this feature, add the following to your Sphinx configuration file::

    extensions = [
        'sphinx_autodoc_toolbox.multiple_targets',
    ]
