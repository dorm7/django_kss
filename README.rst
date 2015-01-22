
************
introduction
************

help you launch your style guide site with KSS syntax

.. image:: pictures/screenshot.png

=====
start
=====

    pip install django-kss



Settings
======================

in yout settings.py

Add the app,

.. code-block:: python

    INSTALLED_APPS += (
        "django_kss",
    )


KSS Related Settings
====================

in settings.py 

Add setting in your project's settings with the two extra config

* PYKSS_DIRS:  Setup source file path, less sass or css
* PYKSS_STATIC_FILES: the full path in your assets. final page use it to show content


for example:

.. code-block:: python

    import os
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    PYKSS_DIRS = [os.path.join(BASE_DIR, 'static', 'css')]
    PYKSS_STATIC_FILES = ['css/forms.css', 'css/screen.css']


urls.py settings
================

Routing, add the following two lines in your project's urls.py

import:

    import django_kss.urls

add the url patterns:

    url(r'^$', include(django_kss.urls)),


Writing The KSS in your scss/less/css file
==========================================


.. code-block:: scss

	/*
	Buttons

	Styleguide 1
	*/


	/*
	Your standard form button.

	.btn-danger   -  danger
	.btn-warning  -  warning
	.btn-info     -  info


	Example:
		<button class="liftedBtn $modifier_class" >按鈕</button>

	Styleguide 1.1
	*/

	.liftedBtn{
		@extend .btn;
		position: relative;
		border-width: 0;
		letter-spacing: 1px;
		border-bottom-color: rgba(30,30,30,0.3);
		border-bottom-width: 0;
		transition: all 0.2s;
		bottom: 0;
		&:hover{
			bottom: $strong-border-width;
			border-bottom-width: $strong-border-width;
		}
	}


extend styleguide.html
======================

sometimes, you need to use extra css or js in your style guide. so the default template is not enough.
you can just use the following way to make a better style guide

put the following html in your any template folder

.. code-block:: html

    {% extends 'styleguide.html' %}

    {% load compress %}
    {% load staticfiles %}


    {% block style %}
        {% compress css %}
            <link rel="stylesheet" type="text/x-scss" href="{% static 'css/ntu.scss' %}">
        {% endcompress %}
    {% endblock %}


    {% block bottom %}
        <script src="{% static 'js/bootstrap.min.js' %}"></script>
    {% endblock %}

in your views.py, just specify the template

.. code-block:: python


    from django_kss.views import AutoStyleGuideView


    class StyleGuideView(AutoStyleGuideView):
        template_name = 'filename you like .html'


specify your the view in your urls.py ( replace the package name with yours )

.. code-block:: python

    url(r'^style_guide/(?P<section>\d*)$', style.views.StyleGuideView.as_view(), name='styleguide'),


Use the The Preconfigured Django Server
=======================================

    * git clone https://github.com/timtan/django_kss
    * cd django_kss
    * virtualenv venv
    * source venv/bin/activate
    * pip install -r requirements.txt
    * cd django_kss_project
    * python manage.py runserver
    * refer the KSS Related settings's section to full fill your need.




Feel Free to submit issue. I use the app frequently and happy to know if you like it. 
