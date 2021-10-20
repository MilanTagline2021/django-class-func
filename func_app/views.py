import io
from django.shortcuts import render
from django.http import HttpResponse
from func_app.models import Student
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt

from .serializers import StudentSerializer
# Create your views here.

@csrf_exempt
def get_student_api(request):
    if request.method=='GET':
        json_data=request.body
        stream = io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id', None)
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        
        stu=Student.objects.all()
        serializer=StudentSerializer(stu, many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    if request.method=="POST":
        json_data=request.body
        stream = io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer=StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res={"msg":"Data inserted"}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    if request.method=="PUT":
        json_data=request.body
        stream = io.BytesIO(json_data) 
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu, data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res={"msg":"Data Updated"}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    if request.method=="DELETE":
        json_data=request.body
        stream = io.BytesIO(json_data) 
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        stu=Student.objects.get(id=id)
        stu.delete()
        res={"msg":"Data Deleted"}
        return HttpResponse(res,safe=False)