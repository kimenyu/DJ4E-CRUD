from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('register/', views.registerpage, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logoutUser, name = 'logout'),
    path('view_auto/', views.view_make, name='autos'),
    path('add_make/', views.MakeCreateView.as_view(), name='create_make'),
    path('list_view/', views.MakeListView.as_view(), name='make-list'),
    path('make_delete/<int:pk>/delete/', views.MakeDeleteView.as_view(), name='delete'),
    path('make/<int:pk>/update/', views.MakeUpdateView.as_view(), name='update'),
    # path('list_view/', views.MakeListView.as_view(context_object_name='make_list'), name='list_view'),
    # path('create/', views.MakeCreateView.as_view(), name='create'),
]