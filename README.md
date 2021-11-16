# Intro to Django

## Feature Tasks and Requirements

[x]Create web site in Django with 2 pages

[x]home page

[x]about page

[x]create views/urls/templates as needed for home and about pages

[x]use ancestor template to contain navigation elements

[x]Should be built the “Django way” aka match the structure of in-class demo




# to run test 

`  python manage.py test`






## steps:


1- `mk dir`

2- ` poetry init -n`

3- `django-admin startproject proj name .`   (now you have manage.py)


## create app

4- `python manage.py startapp  appname`


5- go to settings and add the app in installed apps

6- run the server to test 

## creat view for the app

1- (app ----> view.py)  i
`from django.views.generic import TempleteView , ListView  , DetailsView`

```
class HomePageView(TempleteView):
      template_name= ('home.html')
```

2- creat the template folder and file and then add it to the project settings
 
DIR=[BASE_DIR/'templates']

3-  creat (urls) file in app files import the views and give them names and endpoints

```
from .views import (HomePageView , AboutUsPageView)



urlpatterns=[
    path('' , HomePageView.as_view() , name='home'),
    path('about-us' , AboutUsPageView.as_view() , name='about_us')
]
```

* add the new urls file to project urls file 

```
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
     path('', include('appName.urls')),
]

```


## add models 

1- (app----> models.py)  creat class (schema)=====> model


2-  migrate model to database 

`python manage.py makemigration`

`python manage.py migrate`

3- give the admin access to it 

(app----> admin.py)

```
from snacks.models import Snack  (import your model)
# Register your models here.


admin.site.register(Snack)
```

4- creat a view for that model
### in view
template_name='name'
model=imported model

listView----> object_list

## pull request  

  [link](https://github.com/ashrf288/django-snacks/pull/1)


