pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/YOUR_USERNAME/flask-ci-cd-demo.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-demo .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 5000:5000 flask-demo'
            }
        }
    }
}