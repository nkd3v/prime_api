pipeline {
    agent none

    environment {
        APP_NAME = "project2"
        IMAGE_NAME = "registry.gitlab.com/nkd3v/project2"
    }

    stages {
        
        stage('Build') {
            agent {
                label 'test'
            }
            steps {
                sh "pip3 install -r app/requirements.txt"
                sh "python3 -m unittest"

                sh "docker build -t ${env.IMAGE_NAME}:${env.BUILD_NUMBER} app"
                sh "docker run -d --rm -p 5000:5000 ${env.IMAGE_NAME}:${env.BUILD_NUMBER}"

                sh "rm -rf simple-api-robot; git clone https://github.com/CE-SDPX/simple-api-robot"
                sh "pip3 install robotframework robotframework-requests"
                sh "python3 -m robot simple-api-robot/test-calculate.robot"

                withCredentials(
                [usernamePassword(
                    credentialsId: '3b4805ee-358c-466d-8f1d-9e2ac58fa53f',
                    passwordVariable: 'gitlabPassword',
                    usernameVariable: 'gitlabUser'
                )]) {
                    sh "docker login -u ${env.gitlabUser} -p ${env.gitlabPassword} registry.gitlab.com"
                    sh "docker push ${env.IMAGE_NAME}:${env.BUILD_NUMBER}"
                }

                sh "docker rm -f `docker ps -aq`"
            }
        }

        stage('Deploy') {
            agent {
                label 'preprod'
            }
            steps {
                withCredentials(
                    [usernamePassword(
                        credentialsId: '3b4805ee-358c-466d-8f1d-9e2ac58fa53f',
                        passwordVariable: 'gitlabPassword',
                        usernameVariable: 'gitlabUser'
                    )]
                ) {
                    sh "docker login -u ${env.gitlabUser} -p ${env.gitlabPassword} registry.gitlab.com"
                }
                
                script {
                    try {
                        echo "Updating service"
                        sh "docker service update simple --with-registry-auth --image ${env.IMAGE_NAME}:${env.BUILD_NUMBER}"
                    } catch (e) {
                        echo "Creating service"
                        sh "docker service create --with-registry-auth --name simple -p 80:5000 ${env.IMAGE_NAME}:${env.BUILD_NUMBER}"
                    }
                }
            }
        }
    }
}