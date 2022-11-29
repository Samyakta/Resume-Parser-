
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Recruiter import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('filter/', views.filter,name='filter'),
    path('resumedata', views.resumedata,name='resumedata'),
    path('login/', views.login,name="login"),
    path('signup/', views.signup,name="signup"),
    path('upload/', views.upload,name="upload"),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)