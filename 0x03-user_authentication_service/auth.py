#!/usr/bin/env python3
import bcrypt


def _hash_password(password: str) -> bytes:
    """returns bytes"""
    value = password
    salt = bcrypt.gensalt()
    bytes = value.encode('utf-8')

    hash = bcrypt.hashpw(bytes, salt)
    return hash
