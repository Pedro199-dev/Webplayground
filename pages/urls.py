from django.urls import path
from .views import PageListViews, PageDetailView

urlpatterns = [
    path('', PageListViews.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/', PageDetailView.as_view(), name='page'),
]