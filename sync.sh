rsync -rv --exclude 'venv/' \
          --exclude 'static/admin/' \
          --exclude '__pycache__/' \
          --exclude '*.log' \
          --exclude '.env' \
          --exclude '.git/' \
        CloudGenie:/var/www/portfolio/ ./
