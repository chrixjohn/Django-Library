
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('home/',views.index),
    path('display/',views.display,name='display'),
    path('edit/<int:pk>/', views.edit,name='edit'),
    path('delete/<int:pk>/', views.delete,name='delete'),
    path('user/', include('users.urls')),

]
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)