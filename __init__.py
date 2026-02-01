# only import if running as a custom node
try:
    import comfy.utils
except ImportError:
    pass
else:
    from .hakkun_nodes import NODE_CLASS_MAPPINGS
    NODE_DISPLAY_NAME_MAPPINGS = {k:k for k in NODE_CLASS_MAPPINGS.items()}
    __all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
