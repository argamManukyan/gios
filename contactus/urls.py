from django.urls import path


from .views import HomeView, privacy_policy

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('privacy-policy/', privacy_policy, name='privacy_policy'),
]