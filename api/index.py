import sys
import os

# Add root directory to sys.path so app and its modules can be imported
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app as flask_app

# Fallback route for /api/index so it never 404s
@flask_app.route('/api/index')
@flask_app.route('/api/index.py')
def vercel_entrypoint_fallback():
    return flask_app.view_functions['home']()

class VercelPathFixMiddleware:
    """
    On Vercel, catch-all rewrites send the request to /api/index,
    overriding the original PATH_INFO. Vercel stores the original
    requested URL in HTTP_X_MATCHED_PATH or HTTP_X_FORWARDED_URI.
    This middleware restores the original path so Flask routes match.
    """
    def __init__(self, wsgi_app):
        self.wsgi_app = wsgi_app

    def __call__(self, environ, start_response):
        matched = (
            environ.get("HTTP_X_MATCHED_PATH")
            or environ.get("HTTP_X_FORWARDED_URI")
            or environ.get("RAW_URI")
        )
        if matched and matched not in ("/api/index", "/api/index.py"):
            environ["PATH_INFO"] = matched.split("?")[0]
        return self.wsgi_app(environ, start_response)

app = VercelPathFixMiddleware(flask_app)
