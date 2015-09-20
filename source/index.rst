.. Django Piston Sample documentation master file, created by
   sphinx-quickstart on Wed Sep 16 20:01:47 2015.


Welcome to Django Piston documentation!
#######################################

Piston is a Django-based mini-framework for creating RESTful APIs.

.. contents:: :local:
   :depth: 2

What Piston does
================

* simple and direct way to access databases
* includes authentication support (OAuth, Basic/Digest)
* can respond to requests via JSON/XML/YAML/Pickle
* supports streaming to clients and throttling
* makes extensive use of HTTP status codes (+ ``PUT`` and ``DELETE``) 

Getting started
===============

.. raw:: html
   
   <a style="margin-left: 20px; /*margin-top: 10px; font-size: 20px;*/" href="docs/start.html" class="btn btn-primary">Download Piston</a>

Workflow
========

The workflow is as simple as: 

1. Create a handler 
2. Bind a handler to a URL
3. Go places

Example
=======

Suppose, there is a blog entry, which initially has *models.py*, *handlers.py* and *urls.py* like any Django projects. The blog entry contains a **text field**, and a **slug field**:

.. code-block:: python
   :caption: models.py

   class Entry(models.Model):
       text = models.TextField()
       slug = models.SlugField(max_length=128, unique=True)

.. literalinclude:: handlers.py
   :language: python
   :caption: handlers.py


In this example, Piston maps the ``GET`` request directly to the a method in the handler, in this case the ``read`` method. Similarly, you can map ``PUT`` request directly to ``update()`` method, ``POST`` — to ``create``, and ``DELETE`` — to ``delete()``.

Easy way of manipulating data from an API.              
Reutrns not the HTTP request, but just the **entry** that we retrieved from database.

.. code-block:: python
   :caption: urls.py

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

Status codes
============

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



.. toctree::
   :maxdepth: 2
   :hidden:

   /docs/start
