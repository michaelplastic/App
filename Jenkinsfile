peline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = 'color-web-app'
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
                    // Run Docker container
                    docker.image(DOCKER_IMAGE_NAME).run('-p 8080:8000')
                }
            }
        }
    }
}
pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = 'color-web-app'
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
                    // Run Docker container
                    docker.image(DOCKER_IMAGE_NAME).run('-p 8080:8000')
                }
            }
        }
    }
}

