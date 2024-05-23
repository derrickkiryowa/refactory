from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name=''),
    path('register', views.register, name='register'),
    path('my_login', views.my_login, name = 'my_login'),
    path('user_logout', views.user_logout, name = 'user_logout'),

    path('dashboard', views.dashboard, name = 'dashboard'),
    path('baby', views.baby, name = 'baby'),
    path('baby_reg', views.baby_reg, name = 'baby_reg'),

    path('babyedit/<int:pk>', views.babyedit, name = 'babyedit'),
    path('baby_view/<int:pk>', views.baby_view, name ='baby_view'),
    path('baby_delete/<int:pk>', views.baby_delete, name='baby_delete'),

    # sitters
    path('sitter', views.sitter, name ='sitter'),
    path('sitter_reg', views.sitter_reg, name ='sitter_reg'),
    
    path('sitteredit/<int:pk>', views.sitteredit, name ='sitteredit'),
    path('sitter_view/<int:pk>', views.sitter_view, name ='sitter_view'),
    path('sitter_delete/<int:pk>', views.sitter_delete, name ='sitter_delete'),
   

    #procurement
    path('procure', views.procure, name ='procure'),
    path('assignprocure', views.assignprocure, name ='assignprocure'),
    path('dollsale', views.dollsale, name ='dollsale')

    ]
    
