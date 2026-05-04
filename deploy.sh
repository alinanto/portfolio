rsync -rv --exclude 'venv/' \
          --exclude 'static/admin/' \
          --exclude '__pycache__/' \
          --exclude '*.log' \
          --exclude '.env' \
          --exclude '.git/' \
          --exclude 'db.sqlite3' \
        /home/alin/projects/portfolio/ CloudGenie:/var/www/portfolio/ 

