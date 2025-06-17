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
    # Normalize the status to lowercase to avoid mismatch
    return mapping.get(status.lower(), 'secondary')  # fallback to 'secondary'
