from django import template

register = template.Library()

@register.filter
def label_from_choices(value, choices):
    """Convert internal key to human-readable label based on choices."""
    return dict(choices).get(value, value)
