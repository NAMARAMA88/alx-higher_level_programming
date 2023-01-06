#!/usr/bin/python3
"""Blocked class module"""


class LockedClass:
    """Object prevents dynamic attributes"""

   __slots__ = ['first_name']
