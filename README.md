# WebApp
Learning Web App development with Django

command to initilaize project files
django-admin startproject <ProjectName>

command to initialize app within project
python manage.py startapp <AppName>

You take a request in each url you want to direct towards, so the frist thing you so is write a function that takes in a request and then give back the page you want to show
We also have to map urls to the pages. for thsi create a new urls.py fro you application, it is gonna be similiar to the urls.py in the django project.
The main urls.py from the django project also has tio be updaed because theats the entry point of the wee application
-- the include function chops off the string it has already seen and then uses the remainder to search for the URL. that is why in the first path we wrote, we left it empty
Once we add new paths/urls, the default page wil not be showna nd we have to specificy the default.



-- THe thinking abehind Django is that you create a Django project and insdie that you can have multiple applications.
-- We can hvae blog style application and then we can have  store lile application in the same website, this will be another application in the same project
-- so this gives alittle abstarction, since you can develop applications and if you like it, use them as parts of different projects
-- the first appliction for this project will be a Blog Style application


Create a templates folder in you subapplication to serve more complicated HTMl files, since by default django looks for a templates subdirectory. Due to how django is configured, we need to make a folder inside our templated for our application.

Need to add installed application to settings.py of the project. (from apps.py in the installed project)

Add a base.html file for repeated code in HTML cuz DRY

CSS and Javascript files need to in a directory called static