pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Pulling source code from GitHub'
                checkout scm
            }
        }

        stage('Check Docker') {
            steps {
                echo 'Checking Docker installation'

                bat '''
                    where docker
                    docker --version
                    docker compose version
                '''
            }
        }

        stage('Build') {
            steps {
                echo 'Building Docker image'

                bat '''
                    docker build -t devops-cicd-app .
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application using Docker Compose'

                bat '''
                    docker compose up -d --build
                '''
            }
        }

        stage('Verify') {
            steps {
                echo 'Verifying application deployment'

                bat '''
                    docker compose ps
                '''
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: CI/CD Pipeline completed successfully!'
        }

        failure {
            echo 'FAILURE: CI/CD Pipeline failed. Check the Console Output.'
        }

        always {
            echo 'Jenkins Pipeline execution finished.'
        }
    }
}