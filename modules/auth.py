from database import get_user_by_email, hash_password


def authenticate(email, password):
    """Authenticate user and return user dict or None."""
    user = get_user_by_email(email)
    if user and user['password'] == hash_password(password):
        return dict(user)
    return None


# Role-based permissions
ROLE_PERMISSIONS = {
    'admin': {
        'dashboard': True,
        'scanner': True,
        'terminal': True,
        'reports': True,
        'users': True,
        'settings': True,
        'ai': True,
    },
    'analyst': {
        'dashboard': True,
        'scanner': True,
        'terminal': False,
        'reports': True,
        'users': False,
        'settings': False,
        'ai': True,
    },
    'developer': {
        'dashboard': True,
        'scanner': True,
        'terminal': True,
        'reports': True,
        'users': False,
        'settings': False,
        'ai': True,
    },
}


def has_permission(role, feature):
    """Check if a role has access to a feature."""
    perms = ROLE_PERMISSIONS.get(role, {})
    return perms.get(feature, False)
