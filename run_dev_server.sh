#/bin/bash

# This script is used to run the development server. It uses the uvicorn
# server, which is a fast ASGI server. It also uses the --reload flag, which
# will automatically reload the server when a file changes. This is useful
# for development, but should not be used in production.

uvicorn dev.google_sso:app --reload --proxy-headers --host 0.0.0.0 --port 8765
