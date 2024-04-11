from django.core.exceptions import PermissionDenied

class UserIsOwnerMixin(object):
    def dispatch(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.creator == self.request.user:
            return super().dispatch(request, *args, **kwargs)
        else:
            return PermissionDenied