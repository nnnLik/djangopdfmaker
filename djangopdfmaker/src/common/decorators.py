from functools import wraps

from rest_framework import status
from rest_framework.response import Response


def serialize_and_validate(serializer_class):
    def decorator(view_func):
        @wraps(view_func)
        def wrapped_view(self, *args, **kwargs):
            serializer_instance = serializer_class(data=self.request.data)
            if serializer_instance.is_valid():
                kwargs.update(serializer_instance.validated_data)
                return view_func(self, *args, **kwargs)
            else:
                return Response(
                    serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST
                )

        return wrapped_view

    return decorator
