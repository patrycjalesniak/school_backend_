from .models import Exam
from rest_framework import permissions

class IsExamOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        exam = Exam.objects.get(id=obj.exam.id)
        return exam.owner == request.user
        # if exam.owner == request.user:
        #     return True
        # return False

class IsOwnerReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user