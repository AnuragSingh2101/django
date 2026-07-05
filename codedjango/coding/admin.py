from django.contrib import admin
from .models import CodingChallenge, CodingReview, UserBookmark, CodingSolution



# Register your models here.
class CodingReviewInline(admin.TabularInline):
    model = CodingReview
    extra = 2


class CodingChallengeAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')
    inlines = [CodingReviewInline]


class UserBookmarkAdmin(admin.ModelAdmin):
    list_display = ('user', 'difficulty')
    filter_horizontal = ('coding_challenges',)


class CodingSolutionAdmin(admin.ModelAdmin):
    list_display = ('coding', 'user', 'date_created')



admin.site.register(CodingChallenge, CodingChallengeAdmin)
admin.site.register(UserBookmark, UserBookmarkAdmin)
admin.site.register(CodingSolution, CodingSolutionAdmin)
