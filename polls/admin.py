from django.contrib import admin
# Register your models here.
from .models import PollQuestion, Parties

# admin.site.register(Question)
# admin.site.register(Choice)

admin.site.site_header = "E-voting Admin"
admin.site.site_title = "E-voting Admin Area"
admin.site.index_title = "Welcome to the E-voting Admin Area"


class ChoiceInLine(admin.TabularInline):
	model = Parties
	extra = 3


class PollQuestionAdmin(admin.ModelAdmin):
	fieldsets = [(None, {'fields': ['question_text']}), ('Date Information', {
		'fields': ['pub_date'], 'classes': ['collapse']}), ]
	inlines = [ChoiceInLine]


admin.site.register(PollQuestion, PollQuestionAdmin)
