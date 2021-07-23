import io

from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.utils.decorators import method_decorator
from django.views import View
from .models import Student

from apis.serializers import StudentSerializer


@method_decorator(csrf_exempt, name='dispatch')
class CreateStudent(View):
    """
    class based api view for create student using serializer
    """

    def post(self, request, *args, **kwargs):
        try:
            json_data = request.body
            stream = io.BytesIO(json_data)
            value = JSONParser().parse(stream)
            if value:
                serializer = StudentSerializer(data=value)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse("successfully created data", status=201, safe=False)
                else:
                    return JsonResponse("something went wrong", safe=False)
            else:
                return JsonResponse(
                    {
                        "message": "didnot get value"
                    }
                )
        except Exception as e:
            return JsonResponse(
                {
                    "message": "something went wrong"
                },
                status=500
            )


@method_decorator(csrf_exempt, name='dispatch')
class GetStudent(View):
    """
    class based api view for getting student details using serializer
"""

    def get(self, request):
        id = request.GET.get('id')

        if id:
            try:
                data = Student.objects.get(id=id)
            except Exception as e:
                data = None
            if data:
                serializer = StudentSerializer(data, many=False)
                return JsonResponse(serializer.data, status=202)
            else:
                return JsonResponse(
                    {
                        "message": "data not found"
                    }, status=404

                )

        else:

            data = Student.objects.all()
            if data:
                serializer = StudentSerializer(data, many=True)
                return JsonResponse(serializer.data, safe=False)
            else:
                return JsonResponse(
                    {
                        "message": "data not found"
                    },
                    status=404
                )


@method_decorator(csrf_exempt, name='dispatch')
class UpdateStudent(View):
    """
    class based api view for updating student details paritally using serializer
"""

    def patch(self, request, pk):
        try:
            data = Student.objects.get(id=pk)
        except Exception as e:
            return JsonResponse(
                {
                    "message": "data not found"
                },
                status=404
            )

        if data:
            req_data = request.body
            stream = io.BytesIO(req_data)
            parsed_data = JSONParser().parse(stream)
            serializer = StudentSerializer(data, data=parsed_data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return JsonResponse(
                    {
                        "message": "data updated successfully"
                    },
                    status=201
                )
            else:
                return JsonResponse(
                    {
                        "message": "data not updated"
                    },
                    status=404
                )


@method_decorator(csrf_exempt, name='dispatch')
class DeleteStudent(View):
    """
        class based api view for deleting student record
    """

    def delete(self, request, pk):
        try:
            data = Student.objects.get(id=pk)
        except Exception as e:
            data = None

        if data:
            data.delete()
            return JsonResponse(
                {
                    "message": "data deletedd successfully"
                },
                status=200
            )

        else:
            return JsonResponse(
                {
                    "message": "data not found"
                },
                status=404
            )
#
