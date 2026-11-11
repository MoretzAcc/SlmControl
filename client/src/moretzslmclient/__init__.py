"""Compatibility imports for the former client package name."""

from importlib import import_module
import sys
import warnings

import slmclient


warnings.warn(
    "moretzslmclient is deprecated; use slmclient instead.",
    DeprecationWarning,
    stacklevel=2,
)

# Reuse canonical modules so classes, exceptions, and module state stay identical.
for _module_name in (
    "bit_map_util",
    "client",
    "discover_heros",
    "file_util",
    "notebook_helpers",
    "preview",
    "types",
):
    sys.modules[f"{__name__}.{_module_name}"] = import_module(f"slmclient.{_module_name}")

sys.modules[__name__] = slmclient
