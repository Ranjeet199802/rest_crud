from rest_framework import serializers
from.models import Student


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll_no = serializers.IntegerField()
    course = serializers.CharField(max_length=100)
    city = serializers.CharField(max_length=100)

    # class Meta:
    #     model = Student
    #     fields = '__all__'
    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll_no = validated_data.get('roll_no', instance.roll_no)
        instance.course = validated_data.get('course', instance.course)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance
