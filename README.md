# ml-housing
Software and account Requirement.
Github Account
Heroku Account
VS Code IDE
GIT cli
GIT Documentation
Creating conda environment.

conda create -p venv python==3.7 -y

conda activate venv/

pip install -r requirements.txt

To Add files to git

git add .

git commit -m "file name"

git push origin main

BUILD DOCKER IMAGE:
'''
docker build -t <image_name>:<tagname> .
'''

To list docker image:
docker images
Run docker image:
docker run -p 5000:5000 -e PORT=5000 f8c749e73665

To check running container in docker
docker ps

Tos stop docker conatiner:
docker stop <container_id>

python setup.py install

pip install ipykernel --jupyter notebook