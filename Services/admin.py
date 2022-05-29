from django.contrib import admin
from Services.models import courses , cloud_computing , software_testing , machine_learning , android_App , ios_App , front_end ,back_end,full_stack

# Register your models here.

# courses list class
# coursesAdmin
class coursesAdmin(admin.ModelAdmin) :
    list_display =('course_name','course_intro','course_intro_link', 'full_course_link')
admin.site.register(courses,coursesAdmin)

# cloud_computing
class cloudAdmin(admin.ModelAdmin) :
    list_display =('language','language_info','reference_link')
admin.site.register(cloud_computing,cloudAdmin)

# software_testing
class softwareAdmin(admin.ModelAdmin) :
    list_display =('language','language_info','reference_link')
admin.site.register(software_testing,softwareAdmin)

# machine_learning
class machineAdmin(admin.ModelAdmin) :
    list_display =('language','language_info','reference_link')
admin.site.register(machine_learning,machineAdmin)

# android_App
class androidAdmin(admin.ModelAdmin) :
    list_display =('language','language_info','reference_link')
admin.site.register(android_App,androidAdmin)

# ios_App
class iosAdmin(admin.ModelAdmin) :
    list_display =('language','language_info','reference_link')
admin.site.register(ios_App,iosAdmin)

# front end
class front_endAdmin(admin.ModelAdmin) :
    list_display =('language','language_info','reference_link')
admin.site.register(front_end,front_endAdmin)

# back end
class back_endAdmin(admin.ModelAdmin) :
    list_display =('language','language_info','reference_link')
admin.site.register(back_end,back_endAdmin)

# full stack development
class full_stackAdmin(admin.ModelAdmin) :
    list_display =('language','language_info','reference_link')
admin.site.register(full_stack,full_stackAdmin)
