# Testcase solution for job responce
This repo contains: <br>
- Dokcerfile for create python image for endpoint app
- docker-compose file for set up whole project
- nginx web server config files for reverse-proxy settings 

## Usage
```
git clone https://github.com/joshkant/testcase.git
cd testcase 
docker-compose up -d 
make sure all containers are running docker ps
```

## Tesing set up
Test with regular curl: **http://localhost:8081** or **http://localhost:8082** <br>
This must return ip's list of nginx proxy pass chain of servers


Test with milicious header in curl: <br>
```curl -H "X-Forwarded-For: 8.8.8.8" http://localhost:8081``` <br>
```curl -H "X-Forwarded-For: 8.8.8.8" http://localhost:8082``` <br>
```curl -H "X-Forwarded-For: milicious" http://localhost:8083``` <br>
this must still return ip's list of nginx proxy pass chain of servers but without user defined header <br>




