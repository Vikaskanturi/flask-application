pipeline {
    agent {label 'python-agent'}

    stages {
        stage('clone repo') {
            steps {
                git branch: 'main', url: 'https://github.com/Vikaskanturi/flask-application.git'
            }
        }
        stage('install python depndencies') {
            steps {
                sh 'yum install python3 -y'
                sh 'yum install python3-pip -y'
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('perform tests') {
            steps {
                sh 'pytest'
                // sh 'flake8 .' 
            }
        }
        stage('build docker image') {
            steps {
                sh 'yum install docker -y'
                sh 'systemctl start docker'
                sh 'docker build -t flask-app:latest .'
            }
        }
        stage('containerize application') {
            steps {
                sh 'docker rm -f flask-app || true'
                sh 'docker run -dit --name flask-app -p 8080:80 flask-app:latest'
            }
        }
    }
}
