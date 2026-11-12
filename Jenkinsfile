pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Pulling source code from GitHub'
                checkout scm
            }
        }

        stage('Check Docker') {
            steps {
                bat 'docker --version'
                bat 'docker compose version'
            }
        }

        stage('Build') {
            steps {
                echo 'Building frontend and backend'
                bat 'docker compose build'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying containers'
                bat 'docker compose up -d --build --remove-orphans'
            }
        }

        stage('Verify') {
            steps {
                bat 'docker compose ps'
            }
        }
    }

    post {
        failure {
            bat 'docker compose logs --no-color || true'
        }
    }
}