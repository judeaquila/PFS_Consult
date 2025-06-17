from django import template

register = template.Library()

@register.filter
def status_badge_class(status):
    mapping = {
        'pending': 'warning',
        'in_review': 'primary',
        'completed_documentation': 'secondary',
        'approved': 'success',
        'rejected': 'danger',
    }
    return mapping.get(status.lower(), 'secondary')

@register.filter
def payment_badge_class(status):
    mapping = {
        'paid': 'success',
        'unpaid': 'danger',
    }
    return mapping.get(status.lower(), 'secondary')