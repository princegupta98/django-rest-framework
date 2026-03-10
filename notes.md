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

**** rest_main ****

WebApp Endpoints(Traditional Apps)-
	directly access from web browsers
	return html pages

Api Endpoints(Modern Apps)-
	return data (json/xml)
	returns data to integrate into frontend
	usually starts from api/v1
	specify version number in url endpoint
	accessed programatically

In web application, both web app endpoints and api endpoints are there
	web app endpoint are used for public url
	api endpoint are used to response data

In modern apps, instead of web app endpoints frontend routes are used with api endpoints.

create default database tables 
	python manage.py migrate

create superuser
	p15:p15

create model in student app
	python manage.py makemigrations
	register model in admins module in student app
	python manage.py migrate

can check Student in admin panel

for api endpoint we send response using JsonResponse whihc expects dict type
	1. we can convert queryset data to list type value by value and pass JsonResponse safe as False. But this manual serialization is not recommended for developing RestAPIs
	2. we can use django-rest-framework inbuilt Serializer class. It serializes coplex data to json and also handles validatioin

Serialization-
	convert model instance(QuerySet) to json [vice/versa for deserialization]
	translator for data
	db data to format easily sent over the internet

	Serializer
		Model Serializer- provides fields for model, reduces code

Function Based Views-
	for fucntion based views in drf we need to use api_view decorator and pass request method in it
		use Response from rf.response
		use status from rf
		use api_view from rf.decorators

	to save data using Serializer pass data in its custom serializer class

	fetch specific data using primary key and path param
		Classes created in django models have unique property DoesNotExist which is used as exception if data is not found

	updating data requires the object to be updated to be passed in Serializer along with request data

	deleting data requires simple delete() call on the object

Class Based Views-
	- more structured and organized way to handle requests
	- no conditional checks for methods instead we use instance methods such as get() post() put() delete() which automatically gets mapped to crud ops
	- code reusability

	for class based
	import APIView from rf.views instead of api_view decorator
	create member function for each HTTP method inside this class, as its a member function self is required

