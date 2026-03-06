**** mysite ****

alternate command for creating django project
	python -m django startproject project_name

mention rest_framework in INSTALLED APPS in project's settings.py

instead of ModelForm in Django, we create Serializer in DjangoRestFramework
	serializers.py
	converts python model to json object for api request/response
	imported from rest_framework
	pass serializers.ModelSerializer in Serializer class

in views.py
	pass generics.apiview-operation-class in views classes instead of passing models.Model

in urls.py
	path 2nd param will be views.Classname.as_view()

we can define custom view instead of generic django views to perform an op
	by giving method name as http method name according to op we want to perform

we can also make custom API View if we dont want to use generic apiviews
	in class pass APIView
		define method (name as http methods) and perform operation