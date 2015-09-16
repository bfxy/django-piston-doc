.. Django Piston Sample documentation master file, created by
   sphinx-quickstart on Wed Sep 16 20:01:47 2015.

Welcome to Django Piston documentation!
================================================

Sample code block below: 

.. code-block:: python
   :caption: models.py

   # models.py
   class Entry(models.Model):
       text = models.TextField()
       slug = models.SlugField(max_length=128, unique=True)

Sample code block above.

Sample external code below:        

.. literalinclude:: handlers.py
   :language: python
   :emphasize-lines: 12,15-18

   class EntryHandler(BaseHandler):
       model = Entry
       methods_allowed = ('GET',)

       def read(self, request, slug):
           entry = get_object_or_404(Entry, slug=slug)
           return entry

Sample external code above.           

Contents:

.. toctree::
   :maxdepth: 2
