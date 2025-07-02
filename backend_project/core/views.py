from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.http import FileResponse, Http404
from django.core.signing import Signer, BadSignature

from .models import UploadedFile
from .serializers import FileUploadSerializer

from django.shortcuts import render

def home(request):
    return render(request, 'index.html')


signer = Signer()

class FileUploadView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if request.user.role != "OPS":
            return Response({"detail": "Only OPS users can upload files."}, status=403)

        serializer = FileUploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GenerateDownloadLink(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, file_id):
        if request.user.role != "CLIENT":
            return Response({"detail": "Only clients can generate download links."}, status=403)

        try:
            file = UploadedFile.objects.get(id=file_id)
        except UploadedFile.DoesNotExist:
            raise Http404("File not found")

        signed_id = signer.sign(str(file.id))
        download_url = f"/api/download/{signed_id}/"

        return Response({
            "download_link": download_url,
            "message": "success"
        })

class SecureFileDownload(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, signed_id):
        try:
            file_id = signer.unsign(signed_id)
            file = UploadedFile.objects.get(id=file_id)

            if request.user.role != "CLIENT":
                return Response({"detail": "Only clients can download files."}, status=403)

            return FileResponse(file.file, as_attachment=True)

        except (BadSignature, UploadedFile.DoesNotExist):
            raise Http404("Invalid or expired link")
