Getting started
===============

1. Create a handler
2. Bind a handler to a URL
3. Go places

Suppose, there is a blog entry, which like any Django projects initially has *models.py*, *handlers.py* and *urls.py*. The blog entry contains a **text field**, and a **slug field**. 

.. code-block:: python

   class Entry(models.Model):
       text = models.TextField()
       slug = models.SlugField(max_length=128, unique=True)

.. literalinclude:: handlers.py
   :language: python

Piston maps HTTP request (in this case ``GET``) directly to different method in the handler, in our case ``read()``. Similarly, PUT maps directly to ``update()``, POST is mapped to ``create()``, and DELETE is mapped to ``delete()``.              
