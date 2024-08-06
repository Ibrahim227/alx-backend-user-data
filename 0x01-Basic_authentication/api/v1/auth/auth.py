#!/usr/bin/env python3
"""Import required Module/Lib"""
from flask import request
from typing import List, TypeVar


class Auth:
    """A class to manage the API authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Require Auth
        Returns:
          - False - path nd excluded_paths will be used late
        """
        if path is None or path not in excluded_paths:
            return True

        if excluded_paths is None or excluded_paths == []:
            return True

    def authorization_header(self, request=None) -> str:
        """Authorization Header
        Return:
          - None - request will be the Flask request object
        """
        if request is None:
            return None

        if 'Authorization' not in request:
            return None

        else:
            return

    def current_user(self, request=None) -> TypeVar('User'):
        """Current User
        Return:
          - None - request will be the Flask request object
        """
        return None
