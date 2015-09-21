.. Django Piston Sample documentation master file, created by
   sphinx-quickstart on Wed Sep 16 20:01:47 2015.


Welcome to Django Piston documentation!
#######################################

Piston is a Django-based mini-framework for creating RESTful APIs.

.. contents:: :local:
   :depth: 2

What Piston does
================

* Provides a simple and direct way to access databases (models) via URL 
* Includes authentication support (OAuth, Basic/Digest)
* Allows to create custom emitters that respond to requests via JSON/XML/YAML/Pickle
* Supports streaming and throttling
* Makes extensive use of HTTP status codes (including PUT and DELETE)

Getting started
===============

Download the `latest version <https://pypi.python.org/pypi/django-piston/0.2.3>`_.

.. .. raw:: html 
   
   <a style="margin-left: 20px; /*margin-top: 10px; font-size: 20px;*/" href="https://pypi.python.org/pypi/django-piston/0.2.3" class="btn btn-primary">Get Piston</a>

Workflow
========

The workflow is simple and twofold: 

1. Create a handler
2. Bind a handler to a URL

Example
=======

.. _example:

Suppose, we need to access a blog entry in our database. Like any other Django project, the blog contains  database description in *models.py*, handlers requesting resources from the database in *handlers.py*, and URLs mapped to the handlers in *urls.py*.

The **entry** resides in the ``Entry`` model, and has ``text`` field and ``slug`` field, all defined in *models.py*:

.. code-block:: python

   class Entry(models.Model):
       text = models.TextField()
       slug = models.SlugField(max_length=128, unique=True)       

*handlers.py* defines handlers that allow certain HTTP requests towards the ``Entry`` model: 

.. code-block:: python
   
   class EntryHandler(BaseHandler):
	model = Entry
	methods_allowed = ('GET')

	def read(self, request, slug):
		entry = get_object_or_404(Entry, slug=slug)
		return entry

Piston maps HTTP requests directly to the method in the handler. In the example, the handler allows only ``GET`` request and maps it directly to the ``read`` method. Similarly, ``PUT`` request is mapped to ``update`` method, ``POST`` is mapped to ``create`` method, and ``DELETE`` is mapped to ``delete`` method. 

*urls.py* maps the handler to the URL pattern for the request:

.. code-block:: python

   entry_resource = Resource(handler=EntryHandler)

   urlpatterns += patterns('',
       url(r'entries/(?P<slug>[\w-_]+)/', entry_resource, name='entry_url'))

As a result, this example allows the client to retrieve a blog entry in JSON format over the request: ``GET /entry/<slug>/``.   	

Response
========

The handler does not return an HTTP response, but returns the **entry** itself. Piston returns responses using emitters. The default emitter uses JSON, however Piston also supports YAML, XML, and Pickle. You can define the format in the :ref:`query string<request>`. 

You can use Pison with not just models, but with any data that you wish to retrieve via API, as long as the data in the response is serializable.

Request
=======

The code in the :ref:`example <example>` allows a client to retrieve the **entry** over a neat request: 

* ``GET`` ``/entry/<slug>/``
  
To define the output format, add the ``format`` parameter to the query string:

.. _request:

* ``GET`` ``/entry/<slug>/?format=YAML``
 

Status codes
============

Piston allows handlers to respond with HTTP status codes in certain situations. 

Say, we have to call a ``create`` method to add an item into the database. If the item already exists, the method below will return ``rc.DUPLICATE_ENTRY``, which stands for ``409 Conflict/Duplicate``. If the item does not exist, the method will create the item:

.. code-block:: python

   def create(self, request):
       if self.exists(**request.POST):
           return rc.DUPLICATE_ENTRY
       else:
           return Entry.objects.create(**request.POST)

Similarly, the successfully called ``delete`` method will return ``rc.DELETED``, which stands for ``204 Empty body``:       

.. code-block:: python
   
   def delete(self, request, slug):
       entry = get_object_or_404(Entry, slug=slug)
       entry.delete
       return rc.DELETED

.. toctree::
   :maxdepth: 2
   :hidden:
