from django.urls import path
from .views import ExamView, TaskView
from rest_framework.routers import DefaultRouter
from rest_framework_extensions.routers import NestedRouterMixin

class NestedDefaultRouter(NestedRouterMixin, DefaultRouter):
    pass

router = NestedDefaultRouter()

router.register("exams", ExamView, basename="exams").\
    register("tasks", TaskView, basename="exam-tasks", parents_query_lookups=["exam"])

router.register("tasks",TaskView, basename="tasks")

urlpatterns = router.urls