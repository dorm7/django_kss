
************
introduction
************

Help you launch your style guide site with django in KSS syntax. you can integrate the style giude in your site easily.
I use it every day. feel free to give me any suggestion.

 I now change the name to django-kss-styleguide https://pypi.python.org/pypi/django-kss-styleguide/

.. image:: pictures/screenshot.png

=====
start
=====

    pip install django-kss-styleguide



========
Settings
========

in yout settings.py

Add the app,

.. code-block:: python

    INSTALLED_APPS += (
		"compressor",
        "django_kss",
    )


================
Related Settings
================

in settings.py 

because scss is very common, we support it via djagno compressor
Add setting  about django compressor.

.. code-block:: python

	COMPRESS_PRECOMPILERS = (
		('text/x-scss', 'django_libsass.SassCompiler'),
	)
	STATICFILES_FINDERS = (
		'django.contrib.staticfiles.finders.FileSystemFinder',
		'django.contrib.staticfiles.finders.AppDirectoriesFinder',
		'compressor.finders.CompressorFinder',
	)
	#  Django Compressor for development. so it can put image to correct place
	COMPRESS_ENABLED = True
	COMPRESS_REBUILD_TIMEOUT = 0

	STATIC_ROOT = '/tmp/root'

in your app. 

add filename called styleguide.py in your app. 

.. code-block:: python

	styleguide = {
		'source_dir': 'static/css',
		'verbose_name': 'Sample APP2',   #Optional
		'target_files': 'static/css/form.scss'  # optional
	}


source_dir:  Where you write you kss comment and css files

verbose_name:  Your app name 

target_files:  If you use scss, put the scss file you want to compile


urls.py settings
================

Routing, add the following two lines in your project's urls.py

import:

.. code-block:: python

    import django_kss.urls

add the url patterns:

.. code-block:: python

    url(r'^$', include(django_kss.urls)),



html
====

for F2E or designer

put your complete html in templates/prototype/

you can view it automatically in the site


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




===============
One More Things
===============

the base template is already integrate livereload. 

to utilize livereload, 


.. code-block:: bash

	sudo pip install livereload


and type 'livereload .' in you repository root. 

you can see all the braowser will reflect your change



