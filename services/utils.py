from django.utils.timezone import now

def generate_custom_id(prefix: str) -> str:
    timestamp = now().strftime('%Y%m%d%H%M%S')
    return f"{prefix}-{timestamp}"