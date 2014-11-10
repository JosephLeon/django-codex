from django.contrib import admin
from resources.models import Resource, UserReview


class UserReviewInline(admin.StackedInline):
    model = UserReview
    extra = 1


class ResourceAdmin(admin.ModelAdmin):
    inlines = [UserReviewInline]

admin.site.register(Resource, ResourceAdmin)
