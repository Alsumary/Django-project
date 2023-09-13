from django.contrib import admin
from .models import UserManage, category, articles, comments, subscriptions

admin.site.register(UserManage)
admin.site.register(category)
admin.site.register(articles)
admin.site.register(comments)
admin.site.register(subscriptions)