from online.models import Choice, Poll, Vote
from django.contrib import admin

# Register your models here.
admin.site.register(Poll)
admin.site.register(Choice)
admin.site.register(Vote)