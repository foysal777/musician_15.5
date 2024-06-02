
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home , name= 'homepage'),
    path('edit_album/<int:id>', views.edit_album , name= 'edit_album'),
    path('edit_name/<int:id>', views.edit_name , name= 'edit_name'),
    path('delete_post/<int:id>', views.delete_post , name= 'delete_post'),
    path('database/', views.database, name= 'database'),
    path('musician_app/', include( 'musician_app.urls' )),
    path('album_app/', include( 'album_app.urls' )),
    
]
