from django.contrib import admin
from django.urls import path
from .views import*


urlpatterns = [
   #path('admin/', admin.site.urls),
    path('hello1/',hello1, name='hello'),
    path('',newhomepage, name='newhomepage'),
    path('package/',travelpackage, name='package'),
    path('print/',print1, name='print'),
    path('p/', print_to_console, name='print_to_console'),
    path('otpgen/',randomcall,name='randomcall'),
    path('otp/',randomlogic,name='randomlogic'),
    path('date/',getdate1,name='getdate1'),
    path('date1/', get_date, name='get_date'),
    path('registercall/',register_call,name='register_call'),
    path('registerlogin/',registerloginfunction,name='registerloginfunction'),
    path('pie/', pie_chart, name='pie_chart'),
path('rentcar/', rentcar, name='rentcar'),
path('weathercall/', weatherpagecall, name='weatherpagecall'),
    path('weatherlogic/',weatherlogic,name='weatherlogic'),
    path('feedbackcall/', feedback_call, name='feedback_call'),
    path('contactmail/', contactmail, name='contactmail'),
path('login/', login, name='login'),
path('signup/', signup, name='signup'),
     path('login1/', login1, name='login1'),
    path('signup1/', signup1, name='signup1'),
path('logout/', logout, name='logout'),

]