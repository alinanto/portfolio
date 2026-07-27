#!/bin/bash

# Pre-deployment checks and setup
echo "Running pre-deployment checks..."

# Activate local virtual environment
source venv/bin/activate

# Make and run migrations locally
echo "Making and running migrations locally..."
python3 manage.py makemigrations
python3 manage.py migrate

# Check and update settings.py for production
echo "Checking settings.py..."
if grep -q "DEBUG = True" config/settings.py; then
    echo "Setting DEBUG = False"
    sed -i 's/DEBUG = True/DEBUG = False/' config/settings.py
fi

# Run Django checks
echo "Running Django system checks..."
python3 manage.py check

# Deactivate venv
deactivate

rsync -rv --exclude 'venv/' \
          --exclude 'static/admin/' \
          --exclude '__pycache__/' \
          --exclude '*.log' \
          --exclude '.env' \
          --exclude '.git/' \
          --exclude 'db.sqlite3' \
          --exclude 'staticFiles/' \
          --exclude 'media/' \
          --exclude 'static/' \
        /home/alin/projects/portfolio/ cloudgenie:/var/www/portfolio/

# SSH into remote server and run deployment commands
ssh cloudgenie << 'EOF'
  cd /var/www/portfolio
  source venv/bin/activate
  pip install -r requirements.txt
  python3 manage.py migrate --noinput
  python3 manage.py collectstatic --noinput
  sudo chown -R ec2-user:apache /var/www/portfolio/
  sudo chmod -R 775 /var/www/portfolio
  sudo systemctl restart httpd
EOF
