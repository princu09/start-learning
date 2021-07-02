from django.contrib import admin
from django.urls import path, include
from study import urls

admin.site.site_header = "Start Learning By NFG"
admin.site.index_title = "Welcome to Start Learning NFG"

urlpatterns = [
    path('siteAdminApproveByNFG/', admin.site.urls),
    path('', include('study.urls')),
]