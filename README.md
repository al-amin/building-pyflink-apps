# building-pyflink-apps
building-pyflink-apps

AMC_FLINK/docker-compose.yml

AMC_FLINK/Dockerfile

# ONE TIME
#### build docker image for Pyflink
## Dokcer steps:
### sudo chmod -R g+rw "$HOME/.docker"
`docker login -u alaminasif`
`docker build -t=building-pyflink-apps:1.17.1 .`

#### create kafka and flink clusters and kafka-ui
`docker-compose up -d`


#### start kafka producer in one terminal
`python -m venv flink_venv`
`source flink_venv/bin/activate`


# upgrade pip (optional) pip install pip --upgrade
# install required packages
`pip install -r requirements-dev.txt`

# Add git ignore
`Created a .gitignore file`
`git add .gitignore`
`git commit -m "Add .gitignore"`
`git push`

## start this for sending 100 messages
`python src/s05_data_gen.py`


