from django.urls import include, path
from rest_framework import routers
from expense_tracker.views import ExpenseViewSet

router = routers.DefaultRouter()
router.register(r'expenses', ExpenseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
