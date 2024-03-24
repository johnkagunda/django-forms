from django.urls import path
from myapp.views import members, details ,input_form # Adjust the import statement here
from django.contrib import admin

from myapp import views
urlpatterns = [
    # URL pattern for the members view
      path('admin/', admin.site.urls),
    path('members/', members, name='members'),

    # URL pattern for the details view with dynamic id
    path('details/<int:id>/', details, name='details'),
    
     path('home/' , views.input_form ),

]
