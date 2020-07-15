======================
sphinxcontrib-diagrams
======================

The Sphinx extension allows you to embed diagrams.net(drawio) format into a document.

::

    .. image:: example.drawio

::

    .. figure:: example.drawio

        caption of figure

Install
=======

::

   $ pip install sphinxcontrib-diagrams

This extension requires draw.io-export.

https://www.npmjs.com/package/draw.io-export


Configure Sphinx
================

Add ``sphinxcontrib.diagrams`` to ``extensions`` at `conf.py`::

     extensions += ['sphinxcontrib.diagrams']


And set your draw.io-export path to ``diagrams_exporter_path`` (default: ``drawio``)::

     diagrams_exporter_path = 'your draw.io-export path'


Usage
=====

::

    .. image:: example.drawio

::

    .. figure:: example.drawio

        caption of figure

.. _image: http://docutils.sourceforge.net/docs/ref/rst/directives.html#image
.. _figure: http://docutils.sourceforge.net/docs/ref/rst/directives.html#figure
