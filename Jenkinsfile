pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = 'color-web-app'
        HOST_PORT = '8081'  // Change this to a port that is not in use
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

        stage('Remove Previous Container') {
            steps {
                script {
                    try {
                        // Try to stop and remove the existing container
                        docker.image(DOCKER_IMAGE_NAME).stop()
                        docker.image(DOCKER_IMAGE_NAME).remove(force: true)
                    } catch (Exception e) {
                        echo "No previous container found. Continuing..."
                    }
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Run Docker container with a different host port
                    docker.image(DOCKER_IMAGE_NAME).run("-p ${HOST_PORT}:8000")
                }
            }
        }
    }
}

