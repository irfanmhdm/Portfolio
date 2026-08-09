from django.contrib import admin
from .models import Profile, Project, Certificate, Skill, Education


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "title", "email")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "featured", "created_at")
    list_filter = ("featured",)
    search_fields = ("title", "technologies")


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ("title", "organization", "issue_date")
    list_filter = ("organization",)
    search_fields = ("title", "organization")


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "level")
    list_filter = ("category",)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("degree", "institution", "start_date", "end_date")