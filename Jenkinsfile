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

        stage('Run Tests') {
            steps {
                script {
                    // Run tests here
                    // Add commands to run your tests
                }
            }
        }

        stage('Deploy to Production') {
            when {
                expression {
                    // Add a condition to deploy to production based on test results
                    // For example, when tests are successful
                    true
                }
            }
            steps {
                script {
                    // Deploy to production here
                    // Add commands to deploy your app to production
                }
            }
        }
    }
}

