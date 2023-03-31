from rest_framework import serializers

class CapitalSerializer(serializers.Serializer):
    date = serializers.DateField()
    letter = serializers.CharField(max_length=50)
    group = serializers.CharField(source='group.name', max_length=50)
    teacher = serializers.CharField(source='teacher.name', max_length=100)
    category = serializers.CharField(source='discipline.name', max_length=50)
    office = serializers.CharField(source='office.name', max_length=50)
    time = serializers.CharField(max_length=50)
