from rest_framework import generics, parsers, status
from rest_framework.response import Response

from .serializers import GeneratePdfFromSourceSerializer
from .services import view_services


class GeneratePdfFromSourceView(generics.GenericAPIView):
    parser_classes = (
        parsers.FormParser,
        parsers.MultiPartParser,
        parsers.FileUploadParser,
    )
    serializer_class = GeneratePdfFromSourceSerializer

    def post(self, request, *args, **kwargs):
        serializer = GeneratePdfFromSourceSerializer(data=request.data)
        if serializer.is_valid():
            task_id, message = view_services.generate_pdf_from_source(
                serializer.validated_data["to_pdf"], serializer.validated_data["type"]
            )
            return Response(
                {"task_id": task_id, "result": message}, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
