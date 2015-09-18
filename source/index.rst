.. Django Piston Sample documentation master file, created by
   sphinx-quickstart on Wed Sep 16 20:01:47 2015.

Welcome to Django Piston documentation!
================================================

Sample code block below: 

.. code-block:: python

   class Entry(models.Model):
       text = models.TextField()
       slug = models.SlugField(max_length=128, unique=True)

Sample code block above.

Sample external code below:        

.. literalinclude:: handlers.py
   :language: python

Sample external code above.           

Contents:

.. toctree::
   :maxdepth: 2
