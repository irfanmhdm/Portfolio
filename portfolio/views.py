from rest_framework import viewsets

from .models import (
    Profile,
    Project,
    Certificate,
    Skill,
    Education,
)

from .serializers import (
    ProfileSerializer,
    ProjectSerializer,
    CertificateSerializer,
    SkillSerializer,
    EducationSerializer,
)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by("-created_at")
    serializer_class = ProjectSerializer


class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all().order_by("-issue_date")
    serializer_class = CertificateSerializer


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all().order_by("-start_date")
    serializer_class = EducationSerializer