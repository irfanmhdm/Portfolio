from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    bio = models.TextField()
    profile_image = models.ImageField(
        upload_to="profile/",
        blank=True,
        null=True
    )
    resume = models.FileField(
        upload_to="resume/",
        blank=True,
        null=True
    )
    email = models.EmailField()
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    technologies = models.CharField(max_length=300)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    image = models.ImageField(
        upload_to="projects/",
        blank=True,
        null=True
    )
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Certificate(models.Model):
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=150)
    issue_date = models.DateField()
    credential_url = models.URLField(blank=True)
    image = models.ImageField(
        upload_to="certificates/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ("Frontend", "Frontend"),
        ("Backend", "Backend"),
        ("Database", "Database"),
        ("Tools", "Tools"),
        ("Other", "Other"),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )
    level = models.PositiveIntegerField(
        default=70,
        help_text="Skill level from 0 to 100"
    )

    def __str__(self):
        return self.name


class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField(
        blank=True,
        null=True
    )
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.degree} - {self.institution}"