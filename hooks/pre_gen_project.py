
# Checks that invoke is installed.

try:
    import invoke
except ImportError:
    raise ImportError('cannot import invoke. Did you run \'pip install invoke\'?')
