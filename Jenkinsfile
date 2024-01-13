pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/michaelvaknin/App.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('color-web-app')
                }
            }
        }

        stage('Stop and Remove Existing Container') {
            steps {
                script {
                    sh 'docker stop color-web-app || true'
                    sh 'docker rm color-web-app || true'
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    docker.image('color-web-app').run('-p 8081:8000 -d')
                }
            }
        }
    }
}

