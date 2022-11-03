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
    :py:class:`Parent <example.Unknown|example.Parent>`

The above three snippets will be rendered as :py:class:`example.Parent|example.Unknown`, :py:class:`example.Unknow|example.Parent` and :py:class:`Parent <example.Unknown|example.Parent>`. To use this feature, add the following to your Sphinx configuration file::

    extensions = [
        'sphinx_autodoc_toolbox.pydomain_multiple_targets',
    ]

In the `autosummary` directive, you can use the following syntax to create a cross reference to multiple targets::

    .. autosummary::

        example.Parent.parent_method|example.Child.parent_method

Which will be rendered as:

.. autosummary::

    example.Parent.parent_method|example.Child.parent_method

You can also specify the displayed name of the cross reference using `:`::

    .. autosummary::

        example.Parent.parent_method|example.Child.parent_method:parent_method

Which will be rendered as:

.. autosummary::

    example.Parent.parent_method|example.Child.parent_method:parent_method

In order to use this feature, you must add the following to your Sphinx configuration file::

    extensions = [
        'sphinx_autodoc_toolbox.autosummary_multiple_targets',
    ]
