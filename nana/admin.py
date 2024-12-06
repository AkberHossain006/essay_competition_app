from django.contrib import admin

# Register your models here.


from .models import Competition,EssayTopic,Essay


admin.site.register(Competition)
admin.site.register(EssayTopic)
admin.site.register(Essay)

