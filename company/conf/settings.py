from django.conf import settings

MAX_NAME_LENGTH = getattr(settings, 'COMPANY_MAX_NAME_LENGTH', 150)
MAX_SLUG_LENGTH = getattr(settings, 'COMPANY_MAX_SLUG_LENGTH', 50)
LOGO_MAX_SIZE   = getattr(settings, 'COMPANY_LOGO_MAX_SIZE', (1500, 1500))
