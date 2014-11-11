from django.contrib import admin
from resources.models import Resource, UserReview


class UserReviewInline(admin.TabularInline):
    model = UserReview
    extra = 1


class ResourceAdmin(admin.ModelAdmin):
    inlines = [UserReviewInline]
    list_display = ('resource_title', 'resource_link', 'pub_date')

admin.site.register(Resource, ResourceAdmin)
