.. Django Piston Sample documentation master file, created by
   sphinx-quickstart on Wed Sep 16 20:01:47 2015.


Welcome to Django Piston documentation!
#######################################

Piston is a Django-based mini-framework for creating RESTful APIs.

.. contents:: :local:
   :depth: 2

What Piston does
================

* Simple and direct way to access databases
* Includes authentication support (OAuth, Basic/Digest)
* Can respond to requests via JSON/XML/YAML/Pickle
* Supports streaming to clients and throttling
* Makes extensive use of HTTP status codes (including PUT and DELETE) 

Getting started
===============

.. raw:: html
   
   <a style="margin-left: 20px; /*margin-top: 10px; font-size: 20px;*/" href="docs/start.html" class="btn btn-primary">Download Piston</a>

Workflow
========

The workflow is simple and twofold: 

1. Create a handler
2. Map a handler to a URL

Example
=======

Suppose, we need to access a blog entry in our database. Like any other Django project, the blog contains the database description in *models.py*, handlers requesting resources from the database in *handlers.py*, and URLs mapped to the handlers in *urls.py*.

The entry contains a **text field** and a **slug field** defined in *models.py*:

.. code-block:: python

   class Entry(models.Model):
       text = models.TextField()
       slug = models.SlugField(max_length=128, unique=True)       

In *handlers.py*, we have a 

.. code-block:: python
   
   class EntryHandler(BaseHandler):
	model = Entry
	methods_allowed = ('GET')

	def read(self, request, slug):
		entry = get_object_or_404(Entry, slug=slug)
		return entry

In this example, Piston maps the ``GET`` request directly to the method in the handler, in this case the ``read`` method. Similarly, you can map ``PUT`` request directly to ``update`` method, ``POST`` — to ``create``, and ``DELETE`` — to ``delete``.

Easy way of manipulating data from an API.              
Reutrns not the HTTP request, but just the **entry** that we retrieved from database.

In *urls.py*, 

.. code-block:: python

   entry = Resource(handler=Entry)

   urlpatterns += patterns('',
       url(
       	r'entries/(?P<slug>[\w-_]+)/', 
       	entry_resource, 
       	name='entry_url'))


The client will get a JSON object that is based on the entry data. 

Request format
==============

This allows a client to retrieve the entry over a neat request: 

* ``GET`` ``/entry/<slug>/``
  
You can also define the output format in a query string. Apart from JSON (default), Piston supports YAML, XML, and Tickle. Add the ``format`` parameter to the request string:   

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
