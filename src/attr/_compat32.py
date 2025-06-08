"""Compatibility helpers for Python 3.2.x."""

# NOTE: This module provides minimal fallbacks for features that were
# introduced after Python 3.2 so that the package can be imported on
# very old interpreters. It is *not* a full backport of modern features.

try:
    import enum as _enum
except ImportError:  # pragma: no cover - Python < 3.4
    class Enum(object):
        pass

    def auto():
        return Enum()

    class _EnumModule(object):
        pass

    _EnumModule.Enum = Enum
    _EnumModule.auto = staticmethod(auto)
    enum = _EnumModule()
else:  # pragma: no cover - when enum is available
    enum = _enum
