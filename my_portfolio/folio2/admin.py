from django.contrib import admin
from folio2.models import aboutme, projects, skills 

class skillsAdmin(admin.ModelAdmin):
    skills_data=('skill_logo','skill_heading','skill_detail','skill_perce')
admin.site.register(skills,skillsAdmin)    

class projectsAdmin(admin.ModelAdmin):
    project_data=('project_img','project_p','project_btn')
admin.site.register(projects,projectsAdmin)

class aboutmeAdmin(admin.ModelAdmin):
    aboutme_data=('about_img','about_resume')
admin.site.register(aboutme,aboutmeAdmin)    
# Register your models here.
