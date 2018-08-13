#Modified from https://hharnisc.github.io/2016/06/19/integration-testing-with-docker-compose.html 
# define some colors to use for output 
set -x  



# kill and remove any running containers 
 cleanup () { 
   docker-compose -f docker/docker-compose.yml -p ci rm -f 
 } 

 # build and run the composed services 
 TAG=1 docker-compose -f docker/docker-compose.yml -p ci build && TAG=1 docker-compose -f docker/docker-compose.yml -p ci up -d 
 if [ $? -ne 0 ] ; then 
   printf "Docker Compose Failed\n" 
   exit -1
 else
   printf " Tests Passed\n"
 fi 

 # call the cleanup fuction 
 cleanup 
 
 
