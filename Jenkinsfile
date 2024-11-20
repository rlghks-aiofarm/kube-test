pipeline {
    agent any
    stages {
        stage('Checkout Repositories') {
            steps {
                script {
                    // 레포1과 레포2를 체크아웃
                    dir('repo1') {
                        git url: 'https://github.com/rlghks-aiofarm/test-repo1.git', branch: 'main'
                    }
                    dir('repo2') {
                        git url: 'https://github.com/rlghks-aiofarm/test-repo2.git', branch: 'main'
                    }
                }
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r repo1/requirements.txt'
                sh 'pip install -r repo2/requirements.txt'
            }
        }
        stage('Run Independent Tests') {
            steps {
                sh 'python -m unittest discover repo1'
                sh 'python -m unittest discover repo2'
            }
        }
        stage('Run Integration Tests') {
            steps {
                dir('integration_tests') {
                    sh 'python -m unittest test_integration.py'
                }
            }
        }
    }
}
