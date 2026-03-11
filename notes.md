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

	inside except block do not return Response, as the returned object will be assigned in some variable and when you serialize, it will not work because pk will not be found to serialize due to object type mismatch(model type & Response type)
	for update operation Serializer class will take existing object from db and new object from request

Mixins-
	- mixin classes provide the actions that are used to provide the basic view behavior. Note that the mixin classes provide action methods rather than defining the handler methods, such as .get() and .post(), directly.
	- reusable code classes in oop that provide specific functionalties
	- used to add common functionality (CRUD) to views

	Built-in mixins classes with their built in methods:

		ListModelMixin		list()		get all
		CreateModelMixin	create() 	post 
		RetriewModelMixin	retrieve()  get by id
		UpdateModelMixin	update()	put by id
		DestroyModelMixin	destroy()	delete by id

	to use mixins
		from rf import mixins, generics
		create class based view
		inherit required mixin
		inherit GenericApiView - foundational class for most api views, functionality for handling incoming http requests 

		ex- class EMployees(mixins.ListModelMixin, generics.genericapiview)

	internal flow-
		URL router
			↓
		Employees.as_view()
			↓
		APIView.dispatch()
			↓
		get()
			↓
		self.list()
			↓
		get_queryset()
			↓
		Employee.objects.all()
			↓
		get_serializer(queryset, many=True)
			↓
		EmployeeSerializer(...)
			↓
		Response(serializer.data)

	Conceptually Each component does one job:

		GenericAPIView			infrastructure (isvalid, save, request handling, response generation)
		ListModelMixin			GET list logic
		CreateModelMixin		POST create logic
		your class connects  	HTTP methods get/post/put/delete

GENERICS-
	in mixins operations are performed by built-in functions but we still need to write get post methods for crud 
	generics solves this by combining prebuilt view-classes and mixins that encapsulat common api  functionalities crud

	in genrics we dont specify funnctoin
	it just needs queryset serializer class and looukup field for pk operations

	It provieds classes-
	ListAPIView
	CreateAPIView
	RetrieveAPIView					pk
	UpdateAPIView					pk
	DestroyAPIView					pk

	also combinaton of these
	ListCreateAPIView
	RetrieveUpdateAPIView			pk
	RetrieveUpdateDestroyAPIView	pk

	Can't use these 2 non-pk views in different classes it gives error, we need to group pk operations in 1 class
		ListAPIView
		CreateAPIView

	case 1: 
	list and create are in diff class with diff name 
	with same url only 1st url view will execute
	django reslves top-to-bottom and stops at 1st url match

	case 2: 
	list and create are in diff class with diff name 
	with different url it will work 
	but it will lose REST consistency

	REST vs RPC-
	This is about API design philosophy.

	RPC (Remote Procedure Call)-
	API endpoints represent actions/functions.

	Example:
	POST /createEmployee
	POST /deleteEmployee
	POST /getEmployee

	Each endpoint corresponds to a procedure. and http method is not operation ? endpoint is

	Request:
	POST /createEmployee
	{
		"name": "John"
	}

	This mimics calling a function:
	createEmployee(name="John")

	REST (Representational State Transfer)-
	Endpoints represent resources, and HTTP methods represent actions. REST USES HTTP SMEANTICS

	Example resource:
	employees

	Endpoints:
	GET    		/employees/      -> list employees
	POST   		/employees/      -> create employee
	GET    		/employees/5/    -> retrieve employee
	PUT    		/employees/5/    -> update employee
	DELETE 		/employees/5/    -> delete employee

	Same URL, different HTTP method = operation.

	Side-by-side comparison-

	Operation			RPC						REST
	----------------------------------------------------------------
	list employees		/getEmployees			GET /employees/
	create employee		/createEmployee			POST /employees/
	get one employee	/getEmployee?id=5		GET /employees/5/
	update employee		/updateEmployee			PUT /employees/5/
	delete employee		/deleteEmployee			DELETE /employees/5/

	DRF is built around REST because DRF generic views assume:
		resource URL → one class
		HTTP method → operation
	So, a single class can handle multiple operations

	REST organizes APIs around data resources.
	RPC organizes APIs around functions/actions.

