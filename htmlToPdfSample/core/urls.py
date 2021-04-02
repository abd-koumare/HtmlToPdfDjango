from django.urls import path
from core import views

urlpatterns = [
    path('foo/v1/<int:pk>', views.PdfViewPage.as_view(), name='view-pdf-v1'),
    path('foo/v2/', views.pdf_view_page, name='view-pdf-v2'),
]