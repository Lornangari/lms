from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, ProfileView, CourseViewSet, EnrollmentViewSet, AnnouncementViewSet,  AssignmentViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('courses', CourseViewSet, basename='courses')
router.register('enrollments', EnrollmentViewSet, basename='enrollments')
router = DefaultRouter()
router.register('courses', CourseViewSet, basename='courses')
router.register('enrollments', EnrollmentViewSet, basename='enrollments')
router.register('announcements', AnnouncementViewSet, basename='announcements')
router.register('assignments', AssignmentViewSet, basename='assignments')



urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', ProfileView.as_view(), name='profile'),
    
]
