from django.urls import path
from .views import task_list, task_create, task_detail
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('tasks/', task_list, name='task-list'),
    path('tasks/<int:id>/', task_detail, name='task-detail'),
]
urlpatterns += [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]