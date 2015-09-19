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

Easy way of manipulating data from an API.              
Reutrns not the HTTP request, but just the **entry** that we retrieved from database.

.. code-block:: python

   entry = Resource(handler=Entry)

   urlpatterns += patterns(",
       url(
       	r'entries/(?P<slug>[\w-_]+)/', 
       	entry_resource, 
       	name='entry_url'))

The client will get a JSON object that is based on the entry data. 

This allows to: 

* ``GET`` ``/entry/<slug>/``
  
You can define a format in a query string. If you don't want JSON (default), then you can set, for example, YAML (also XML and Tickle):   

* ``GET`` ``/entry/<slug>/?format=YAML``

Extensive use of status codes. DUPLICATE_ENTRY, DELETED, NOT FOUND, those below run at handlers.py too. 

If item exists, method returs fuck off, if not — creates the new on.  

.. code-block:: python

   def create(self, request):
       if self.exists(**request.POST):
           return rc.DUPLICATE_ENTRY
       else:
           return Entry.objects.create(**request.POST)

Delete method maps directly to delete request.        

.. code-block:: python
   
   def delete(self, request, slug):
       entry = get_object_or_404(Entry, slug=slug)
       entry.delete
       return rc.DELETED

Use to retrieve any data, not just models data. As long as what you return is serializable, 

Streaming — video, chat app, google docs, OAuth support and shit.

