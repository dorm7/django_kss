upload: 
	python setup.py sdist bdist upload
test:
	nosetests django_kss -w django_kss
