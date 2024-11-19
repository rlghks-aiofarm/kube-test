pipeline {
    agent any

    stages {
        stage('Clone Repositories') {
            steps {
                script {
                    git branch: 'main', url: 'https://github.com/aiofarm/repo1.git'
                    git branch: 'main', url: 'https://github.com/aiofarm/repo2.git'
                }
            }
        }
        stage('Build Docker Images') {
            steps {
                sh 'docker build -t rlghks-aiofarm/repo1:latest repo1/'
                sh 'docker build -t rlghks-aiofarm/repo2:latest repo2/'
            }
        }
        stage('Push Docker Images') {
            steps {
                sh 'docker push rlghks-aiofarm/repo1:latest'
                sh 'docker push rlghks-aiofarm/repo2:latest'
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f deployment.yaml'
                sh 'kubectl apply -f service.yaml'
            }
        }
        stage('Run Tests') {
            steps {
                sh './test-script.sh'
            }
        }
    }
}
