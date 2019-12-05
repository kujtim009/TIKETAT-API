# from rest_framework import permissions


# # class Iscustomer(BasePermission):
# #     def has_permission(self, request, view):
# #         if request.user and request.user.groups.filter(name='customers'):
# #             return True
# #         return False


# class Isstaff(permissions.BasePermission):
#     # def has_permission(self, request, view):
#     #     if request.user and request.user.groups.filter(name='Simple_user_group'):
#     #         return True
#     #     return False

#     def has_object_permission(self, request, view, obj):
#         # print("SAFE ETHODS: ", permissions.SAFE_METHODS)
#         # if request.method in permissions.SAFE_METHODS:
#         #     return True
#         return False

#     def has_permission(self, request, view):
#         print("SAFE ETHODS: ", request.user.is_adminuser)
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         return False
from rest_framework.permissions import (DjangoModelPermissions)

class CustomDjangoModelPermissions(DjangoModelPermissions):
    def __init__(self):
        self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']