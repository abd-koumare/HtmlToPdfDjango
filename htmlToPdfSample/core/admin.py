from django.contrib import admin
from core.models import Foo, FeeRequest, FeeReason

admin.site.register(Foo)
admin.site.register(FeeRequest)
admin.site.register(FeeReason)
