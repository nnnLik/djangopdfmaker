from rest_framework import generics, parsers, status
from rest_framework.response import Response
from src.common.decorators import serialize_and_validate
from src.core.models import Task

from .serializers import GeneratePdfFromSourceSerializer, TaskSerializer
from .services import view_services


class GeneratePdfFromSourceView(generics.GenericAPIView):
    parser_classes = (
        parsers.FormParser,
        parsers.MultiPartParser,
        parsers.FileUploadParser,
    )
    serializer_class = GeneratePdfFromSourceSerializer

    @serialize_and_validate(GeneratePdfFromSourceSerializer)
    def post(self, request, *args, **kwargs):
        task_id, message = view_services.generate_pdf_from_source(
            kwargs["to_pdf"], kwargs["type"]
        )
        return Response(
            {"task_id": task_id, "result": message}, status=status.HTTP_200_OK
        )


class TaskDetailsView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
