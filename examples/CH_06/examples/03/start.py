import app  # Replace with your actual application module
from waitress import serve

serve(app.app, host="127.0.0.1", port=8080)
