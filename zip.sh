zip -r portfolio.zip . \
  -x "venv/*" \
  -x ".git/*" \
  -x "__pycache__/*" \
  -x "*.pyc" \
  -x "db.sqlite3" \
  -x ".env" \
  -x "media/*" \
  -x "staticFiles/*" \
  -x "static/*"