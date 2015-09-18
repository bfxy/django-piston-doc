Some code test
==============

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
