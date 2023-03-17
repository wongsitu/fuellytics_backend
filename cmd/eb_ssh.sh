# SSH into eb

eb ssh
sudo su
export $(cat /opt/elasticbeanstalk/deployment/env | xargs)
source /var/app/venv/*/bin/activate
cd var/app/current
python3 /var/app/current/manage.py collecstatic