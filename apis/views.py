import io

from django.http.response import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Student

from apis.serializers import StudentSerializer


@csrf_exempt
def create_student(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        value = JSONParser().parse(stream)
        serializer = StudentSerializer(data=value)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("successfully created data", status=201, safe=False)
        else:
            return JsonResponse("something went wrong", safe=False)


@csrf_exempt
def get_data_by_id(request, pk):                        # aoi for get single user details
    try:
        data = Student.objects.get(id=pk)
    except Exception as e:
        return JsonResponse(
            {
                "message": "id not exists"
            }
        )

    if request.method == 'GET':

        if data:
            serializer = StudentSerializer(data, many=False)
            return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PATCH':                            # api for updations
        if data:
            req_data = request.body
            stream = io.BytesIO(req_data)
            value = JSONParser().parse(stream)

            if value:

                serializer = StudentSerializer(data, data=value, partial=True)

                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse(
                        {
                            "message": "data updated successfully"
                        }
                    )
                else:
                    return JsonResponse(
                        {
                            "message": "something went wrong"
                        }
                    )

            else:
                return JsonResponse(
                    {
                        "message": "data not found"
                    }
                )

    elif request.method == 'DELETE':        #api for delete data by id
        if data:
            data.delete()
            return JsonResponse(
                {
                    "message": "data deleted successfully"
                }
            )

        else:
            return JsonResponse(
                {
                    "message": "something went wrong"
                }
            )


def get_all_data(request):
    if request.method == 'GET':  # api to get all users
        data = Student.objects.all()
        serializer = StudentSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)
