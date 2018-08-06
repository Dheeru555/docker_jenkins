#!/usr/bin/env groovy 


//Example Job name: sdevineni.dev 


// master 
node('buildhost') { 
    def jobName = "${env.JOB_NAME}" 
    splitJobName = jobName.tokenize('.') 


// echo "Running ${env.BUILD_ID} - ${env.JOB_NAME} on ${env.JENKINS_URL}" 
     def userName = splitJobName[0]  
     def repoName = "docker_jenkins
     def branchName = "master"
     def orgName = "Dheeru555" 
 

     def gitRepoURL = "git@github.com:${orgName}/${repoName}.git" 
     def userSSH = "${userName}_ssh" 
     def userNameStackDeploy = "dev_deploy_stack" 

 

     try { 
         stage('git') { 
             echo branchName 
             git credentialsId: "${userSSH}", 
                 url: "${gitRepoURL}", 
                 branch: "${branchName}" 
         } 
 

 

          
             stage('build app') { 
                 sh "docker-compose -f docker-build.yml build" 
                 
             } 
 

 

              
 

             stage('push image') { 
                 withCredentials([string(credentialsId: "${userName}_pass", variable: 'MY_PASSWORD')]) { 
                     sh "docker login -u \"${userName}\" -p \"$MY_PASSWORD\"" 
                     sh "docker-compose -f docker-build.yml push" 
                     sh "docker logout" 
                 } 
             } 
 

 

             stage('stack deploy') { 
                 
                             sh "docker stack deploy -c docker-compose.yml random" 
                         } 
    
     } 
     catch (exception) { 
         currentBuild.result = 'FAILED' 
         failure("${userName}") 
         throw exception 
     } 
 }  
