from django import template
from task.models import Like

register = template.Library()

@register.filter(name="endswith")
def endswith(value, arg):
    return value.lower().endswith(arg.lower())


@register.filter(name="user_like")
def user_like(user, comment):
    if Like.objects.filter(user=user, comment=comment).exists():
        return True
    else:
        return False