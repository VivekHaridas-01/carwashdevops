# carwashdevops
CarWashDevOps


## Redis Installation on WSL

1. Open your WSL terminal (ie. Ubuntu).
2. Update your Ubuntu packages: `sudo apt update` `sudo apt upgrade`
3. Once the packages have updated, install Redis with: `sudo apt install redis-server`
4. Confirm installation and get the version number: `redis-server --version`

To start running your Redis server: 
`sudo service redis-server start`

Check to see if redis is working (redis-cli is the command line interface utility to talk with Redis): 
`redis-cli ping`

This should return a reply of "PONG".

To stop running your Redis server: 
`sudo service redis-server stop`
