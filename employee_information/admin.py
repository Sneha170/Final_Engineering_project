from django.contrib import admin
from employee_information.models import Department, Position, Employees, Tools, Registration

# Register your models here.
admin.site.register(Department)
admin.site.register(Position)
admin.site.register(Employees)
admin.site.register(Tools)
admin.site.register(Registration)

