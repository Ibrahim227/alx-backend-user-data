#!/usr/bin/env python3
import bcrypt


def _hash_password(password: str) -> bytes:
    """returns bytes"""
    return bcrypt.hashpw(password)
