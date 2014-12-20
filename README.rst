
************
introduction
************

help you launch your style guide site with KSS syntax

.. image:: pictures/screenshot.png

=====
start
=====

    pip install django-kss



Installed APP Settings
======================

in settings.py

Add the two app,

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



extend styleguide.html
======================

some times, you need to use extra css or js in your style guide. so the default template is not enough.
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


Development
============

計畫可以方便的做 Style Guide.

DRY 要到一個極致。

只有寫 CSS, 接下來，就可以自動產生 Style Guide 的頁面。

CSS -> Generate List, Generate Page

所有的　input 由產生的　css 來做判斷，這樣才能跟所有的　CSS Preprocessor 整合。



計畫：

1. 做成　APP, 整進　Django
2. 畫面可以由 Bootsrap 的　tab 來分段較順手跟簡單。
3. 我們需要設定的，是檔案清單位置，還有 CSS 檔位置。
    * 檔案清單在　setting.py
    * CSS 位置都寫在　Settting.py 集中　setting


