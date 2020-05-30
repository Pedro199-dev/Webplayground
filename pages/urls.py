from django.urls import path
from .views import PageListViews, PageDetailView, PageCreate

pages_patterns = ([
    path('', PageListViews.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/', PageDetailView.as_view(), name='page'),
    path('create/', PageCreate.as_view(), name='create')
], 'pages')