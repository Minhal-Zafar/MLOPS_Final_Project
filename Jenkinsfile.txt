pipeline {
    environment {
        PATH = "C:\\WINDOWS\\SYSTEM32;C:\\Program Files\\Docker\\Docker\\resources\\bin"
    }
    agent any
    stages {
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t my-flask-app .'
            }
        }
        stage('Run Container') {
            steps {
                bat 'docker run -p 5000:5000 my-flask-app'
            }
            post {
                always {
                    bat 'docker stop $(docker ps -q --filter ancestor=my-flask-app)'
                    bat 'docker rm $(docker ps -aq --filter ancestor=my-flask-app)'
                }
            }
        }
    }
}
