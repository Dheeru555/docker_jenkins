#!/usr/bin/env groovy 
//Example Job name: sdevineni.dev 
// master 
node() { 
    def jobName = "${env.JOB_NAME}" 
    splitJobName = jobName.tokenize('.') 
// echo "Running ${env.BUILD_ID} - ${env.JOB_NAME} on ${env.JENKINS_URL}" 
     def userNam = splitJobName[0]
     def userName = "dheeru"
     def USER = "sdevineni"
     def repoName = "docker_jenkins"
     def branchName = "master"
     def orgName = "Dheeru555" 
     def cnt = 0
 
     def gitRepoURL = "https://github.com/Dheeru555/docker_jenkins.git" 
     def userSSH = "${userName}_ssh" 
     def userNameStackDeploy = "dev_deploy_stack" 

     stage('git') { 
             echo branchName 
             git credentialsId: "dheer_cred", 
                 url: "${gitRepoURL}", 
                 branch: "${branchName}" 
         } 
    
    
              stage('Successful build counts')
    {
        build = currentBuild
        while (build !=  null)
        {
            if( build.result == 'SUCCESS')
            {
                cnt += 1
            }
            build = build.previousBuild
        }
        
        if( cnt == 0)
        {
            cnt = 1
        }
        print cnt
            
    }
 

                   stage('build app') { 
                    def TAG = cnt   
                  sh "sudo usermod -aG docker jenkins"
                  //sh "sudo service jenkins restart"
                  sh "chmod 777 /var/run/docker.sock"
                sudo chown $USER:$USER /usr/local/bin/docker-compose
                 sh "docker build -t dheeru/randomizer:v_${TAG} . -f Dockerfile_rand" 
                  //     sh "docker-compose -f docker-build.yml build"
                 
             } 
 

 
             stage('push image') { 
                 withCredentials([string(credentialsId: "${userName}_pass", variable: 'MY_PASSWORD')]) { 
                     
                     def TAG = cnt
                     sh "docker login -u \"${userName}\" -p \"$MY_PASSWORD\"" 
                     sh "docker push dheeru/randomizer:v_${TAG}" 
                    // sh "docker-compose -f docker-build.yml push"
                     sh "docker logout" 
                 } 
             } 
 

             stage('stack deploy') { 
                 
                 //sh "export TAG=${cnt}"            
                 sh "TAG=${cnt} docker stack deploy -c docker-compose.yml rand"
                         } 
    
             dir('tests') { 
                 stage('test') { 
                     sh "bash testscript1.sh ${cnt}" 
                 } 
             } 

    
   
    
     } 
    
