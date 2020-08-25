ecommerce-project
=======================

**eccomerce-project** is a Django projects. It is a small project
that exposes APIs for the management of an ecommerce.


Meta
----

Author:
    Pedro Jesús González Vargas

Contributors:
    `pedrogzvargas <https://github.com/pedrogzvargas>`_

Status:
    maintained, in development

Version:
    0.1

Python Version:
    3.6

Django Version:
    3.1


Usage
-----

To build and run this project with ``docker-compose`` set variables in ``.env`` file::

    POSTGRES_DB=<value>
    POSTGRES_USER=<value>
    POSTGRES_PASSWORD=<value>
    POSTGRES_DB_LOCATION=<value>
    POSTGRES_DB_PORT=<value>

then run the next commands::

    $ docker-compose build --no-cache

    $ docker-compose up


Load fixtures::

    $ python manage.py eccomerce_fixtures


Run migrations::

    $ python manage.py migrate

Postman
-------
::

    postman/ecommerce.postman_environment.json
    postman/ecommerce.postman_collection.json
