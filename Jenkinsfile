pipeline {
    agent none

    environment {
        APP_NAME = "simple-api"
        IMAGE_NAME = "registry.gitlab.com/nkd3v/simple-api"
    }

    stages {
        
        stage('Build') {
            agent { label 'test' }

            steps {
                sh "docker build -t ${env.IMAGE_NAME}:${env.BUILD_NUMBER} app"

                withCredentials(
                [usernamePassword(
                    credentialsId: 'nkd3v-simple-api',
                    passwordVariable: 'gitlabPassword',
                    usernameVariable: 'gitlabUser'
                )]) {
                    sh "docker login -u ${env.gitlabUser} -p ${env.gitlabPassword} registry.gitlab.com"
                    sh "docker push ${env.IMAGE_NAME}:${env.BUILD_NUMBER}"
                }
            }
        }

        stage('Test') {
            agent { label 'test' }

            steps {
                sh "pip3 install -r app/requirements.txt"
                sh "python3 -m unittest"

                sh "docker run -d --rm -p 5000:5000 ${env.IMAGE_NAME}:${env.BUILD_NUMBER}"

                sh "rm -rf simple-api-robot; git clone https://gitlab.com/sdpx-devbit/simple-api-robot"
                sh "pip3 install robotframework robotframework-requests"
                sh "python3 -m robot simple-api-robot/test-plus.robot"

                sh "docker rm -f `docker ps -aq`"
            }
        }

        stage('Deploy') {
            agent { label 'preprod' }
            
            steps {
                withCredentials(
                [usernamePassword(
                    credentialsId: 'nkd3v-simple-api',
                    passwordVariable: 'gitlabPassword',
                    usernameVariable: 'gitlabUser'
                )]) {
                    sh "docker login -u ${env.gitlabUser} -p ${env.gitlabPassword} registry.gitlab.com"
                }

                sh "docker rm -f simple-api"
                sh "docker run -d --rm -p 80:5000 --name simple-api ${env.IMAGE_NAME}:${env.BUILD_NUMBER}"
            }
        }
    }
}
