from django.urls import path

from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', n1 , name='index'),
    path('photography/', n2 , name='photography'),
    path('travel/' , n7 , name='travel'),

    path('contact/' , n4 , name='contact'),
    path('about/' , n5, name='about'),
    path('single/' , n6, name='single'),
    path('cb/' ,create_blog_post, name='cb'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)