pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = 'color-web-app'
        HOST_PORT = '8081'  // Change this to the desired port
    }

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
                    docker.build(DOCKER_IMAGE_NAME)
                }
            }
        }

        stage('Remove Previous Containers') {
            steps {
                script {
                    // Stop and remove all existing containers on the specified port
                    docker.ps("-q --filter publish=${HOST_PORT}").each { containerId ->
                        docker.stop(containerId)
                        docker.remove(containerId)
                    }
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Run Docker container on the specified port
                    docker.image(DOCKER_IMAGE_NAME).run("-p ${HOST_PORT}:8000 -d")
                }
            }
        }
    }
}

