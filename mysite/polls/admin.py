"""This module is blha."""
from django.contrib import admin

from django.db.models import Choice
from django.db.models import Question


class QuestionAdmin(admin.ModelAdmin):
    """TBD.

    hoge
    """

    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information',
         {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
