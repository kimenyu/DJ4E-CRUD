from django.urls import path

from . import views

urlpatterns = [
	path('', views.CatListView.as_view(), name='index'),
	path('breed_make/', views.BreedCreateView.as_view(), name = 'create'),
	path('view_breeds/', views.BreedListView.as_view(), name='breedView'),
	path('breed_update/<int:pk>/update_breed/', views.BreedUpdateView.as_view(), name='updating'),
	path('breed_delete/<int:pk>/delete_breed/', views.BreedDeleteView.as_view(), name='deleting'),
	path('cat_create/', views.CatCreateView.as_view(), name='catscreate'),
	path('cat_list/', views.CatListView.as_view(), name='list'),
	path('cat_update/<int:pk>/update_cat/', views.CatUpdateView.as_view(), name='cat_update'),
	path('cat_delete/<int:pk>/delete_cat/', views.CatDeleteView.as_view(), name='cat_delete'),
]