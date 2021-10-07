from django.urls import path
from Account import views

app_name='User'

urlpatterns=[
    path('user/create/',views.CreateUserView.as_view(),name='user_create'),
    path('user/token/', views.CreateTokenView.as_view(), name='user_token'),
    path('user/me/', views.ManageUserView.as_view(), name='user_me'),
    path('artist/create/', views.CreateArtistView.as_view(), name='artist_create'),
    path('artist/token/', views.CreateTokenView.as_view(), name='artist_token'),
    path('artist/me/', views.ManageUserView.as_view(), name='artist_me'),
    path('designer/create/', views.CreateDesignerView.as_view(), name='designer_create'),
    path('designer/token/', views.CreateTokenView.as_view(), name='designer_token'),
    path('designer/me/', views.ManageUserView.as_view(), name='designer_me'),
]