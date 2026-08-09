from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    ProfileViewSet,
    ProjectViewSet,
    CertificateViewSet,
    SkillViewSet,
    EducationViewSet,
)


router = DefaultRouter()

router.register("profile", ProfileViewSet, basename="profile")
router.register("projects", ProjectViewSet, basename="projects")
router.register("certificates", CertificateViewSet, basename="certificates")
router.register("skills", SkillViewSet, basename="skills")
router.register("education", EducationViewSet, basename="education")


urlpatterns = [
    path("", include(router.urls)),
]