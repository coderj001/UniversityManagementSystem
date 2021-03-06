from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

'''
This is Class provide extra layer to the django default login system.
This class check user catagory (Admin:1, Staff:2 & Student:3).
And Redirect to specific View class
'''

class LoginCheckMiddleWare(MiddlewareMixin):

    def process_view(self,request,view_func,view_args,view_kwargs):
        modulename=view_func.__module__
        print(modulename)
        user=request.user
        if user.is_authenticated:
            if user.user_type == "1":
                if modulename == "managementApp.HodViews":
                    pass
                elif modulename == "managementApp.views" or modulename == "django.views.static":
                    pass
                else:
                    return HttpResponseRedirect(reverse("admin_home"))
            elif user.user_type == "2":
                if modulename == "managementApp.StaffViews" or modulename == "managementApp.EditResultVIewClass":
                    pass
                elif modulename == "managementApp.views" or modulename == "django.views.static":
                    pass
                else:
                    return HttpResponseRedirect(reverse("staff_home"))
            elif user.user_type == "3":
                if modulename == "managementApp.StudentViews" or modulename == "django.views.static":
                    pass
                elif modulename == "managementApp.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("student_home"))
            else:
                return HttpResponseRedirect(reverse("show_login"))

        else:
            if request.path == reverse("show_login") or request.path == reverse("do_login") or request.path == reverse("registerpage") or modulename == "django.contrib.auth.views":
                pass
            else:
                return HttpResponseRedirect(reverse("show_login"))