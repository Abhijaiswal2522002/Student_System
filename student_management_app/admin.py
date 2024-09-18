from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    CustomUser, AdminHOD, Staffs, Courses, Subjects, Students, Attendance,
    AttendanceReport, LeaveReportStudent, LeaveReportStaff, FeedBackStudent,
    FeedBackStaffs, NotificationStudent, NotificationStaffs
)
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Custom User Admin
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Define the fields to be displayed in the admin
    list_display = ('username', 'email', 'user_type', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'user_type')
    search_fields = ('username', 'email')
    ordering = ('-date_joined',)
    
    # The fields to be displayed in the user detail view
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'user_type')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    # Fields to be included in the forms
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'user_type')},
        ),
    )
    
    # Define which fields should be included in the forms
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

# Register models with the admin site
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(AdminHOD)
admin.site.register(Staffs)
admin.site.register(Courses)
admin.site.register(Subjects)
admin.site.register(Students)
admin.site.register(Attendance)
admin.site.register(AttendanceReport)
admin.site.register(LeaveReportStudent)
admin.site.register(LeaveReportStaff)
admin.site.register(FeedBackStudent)
admin.site.register(FeedBackStaffs)
admin.site.register(NotificationStudent)
admin.site.register(NotificationStaffs)
