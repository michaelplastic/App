pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Check out your source code
                git 'https://github.com/michaelvaknin/App.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    docker.build('color-web-app')
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Stop and remove existing container
                    sh 'docker stop color-web-app || true'
                    sh 'docker rm color-web-app || true'

                    // Run Docker container
                    docker.image('color-web-app').run('-p 8080:8000', '--name color-web-app')
                }
            }
        }
    }
}

