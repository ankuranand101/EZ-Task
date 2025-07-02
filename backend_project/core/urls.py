from django.urls import path, include
from .views import FileUploadView, GenerateDownloadLink, SecureFileDownload, home

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('upload/', FileUploadView.as_view(), name='file-upload'),
    path('generate-download/<int:file_id>/', GenerateDownloadLink.as_view(), name='generate-download'),
    path('download/<str:signed_id>/', SecureFileDownload.as_view(), name='secure-download'),

    # ✅ This must be at the bottom
    path('', home),  # 👈 Root URL to render index.html
]
