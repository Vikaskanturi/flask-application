pipeline {
    agent {label 'python-agent'}

    stages {
        stage('pull and run containerized application') {
            steps {
                sh 'docker pull vikas546/python-flask-app:latest || true'
                sh 'docker rm -f flask-app || true'
                sh 'docker run -dit --name flask-app -p 8080:80 vikas546/python-flask-app:latest'
            }
        }
    }
}
