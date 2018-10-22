#Modified from https://hharnisc.github.io/2016/06/19/integration-testing-with-docker-compose.html 
# define some colors to use for output 
set -x  

RED='\033[0;31m' 
GREEN='\033[0;32m' 
NC='\033[0m' 


# kill and remove any running containers 
 cleanup () { 
   docker-compose -f docker/docker-compose.yml -p ci rm -f 
 } 

 # build and run the composed services 
 TAG=$1 docker-compose -f docker/docker-compose.yml -p ci build && TAG=$1 docker-compose -f docker/docker-compose.yml -p ci up -d 
 if [ $? -ne 0 ] ; then 
   printf "${RED}Docker Compose Failed${NC}\n" 
   exit -1 
 fi 
 

 # wait for the test service to complete and grab the exit code 
 TEST_EXIT_CODE=`docker wait ci_random_test_1` 
 

 # output the logs for the test (for clarity) 
 docker logs ci_random_test_1 
 

 # inspect the output of the test and display respective message 
 if [ -z ${TEST_EXIT_CODE+x} ] || [ "$TEST_EXIT_CODE" -ne 0 ] ; then 
   printf "${RED}Tests Failed${NC} - Exit Code: $TEST_EXIT_CODE\n" 
 else 
   printf "${GREEN}Tests Passed${NC}\n" 
 fi 
 

 # call the cleanup fuction 
 cleanup 
 

 # exit the script with the same code as the test service code 
 exit $TEST_EXIT_CODE 
