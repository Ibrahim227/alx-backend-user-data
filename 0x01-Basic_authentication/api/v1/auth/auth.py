#!/usr/bin/env python3
"""Import required Module/Lib"""
from flask Import request
from typing import List, TypeVar


class Auth:
    """A class to manage the API authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Require Auth
        Returns:
          - False - path nd excluded_paths will be used late
        """
        return False

    def authorization_header(self, request=None) -> str:
        """Authorization Header
        Return:
          - None - request will be the Flask request object
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Current User
        Return:
          - None - request will be the Flask request object
        """
        return None
