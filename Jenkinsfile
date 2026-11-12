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
                sh 'docker --version'
                sh 'docker compose version'
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
                sh 'docker compose up -d --build --remove-orphans'
            }
        }

        stage('Verify') {
            steps {
                sh 'docker compose ps'
            }
        }
    }

    post {
        failure {
            sh 'docker compose logs --no-color || true'
        }
    }
}