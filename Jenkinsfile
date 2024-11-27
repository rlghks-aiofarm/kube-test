pipeline {
    agent any

    environment {
        REPO1 = 'rlghks-aiofarm/test-repo1'
        REPO2 = 'rlghks-aiofarm/test-repo2'
        INTEGRATIONREPO = 'rlghks-aiofarm/kube-test'
        BRANCH = ''
    }

    stages {
        stage('Checkout PR') {
            steps {
                script {
                    // PR 이벤트에서 브랜치를 가져옵니다.
                    def prBranch1 = getBranchFromPR('test-repo1')
                    def prBranch2 = getBranchFromPR('test-repo2')

                    // 테스트 리포지토리 1 체크아웃
                    echo "Checking out test-repo1 with branch: ${prBranch1}"
                    checkout([
                        $class: 'GitSCM',
                        branches: [[name: prBranch1]],
                        userRemoteConfigs: [[url: "https://github.com/${REPO1}.git"]]
                    ])

                    // 테스트 리포지토리 2 체크아웃
                    echo "Checking out test-repo2 with branch: ${prBranch2}"
                    checkout([
                        $class: 'GitSCM',
                        branches: [[name: prBranch2]],
                        userRemoteConfigs: [[url: "https://github.com/${REPO2}.git"]]
                    ])

                    // 인테그레이션 레포 체크아웃
                    echo "Checking out kube-test with branch: 'main'"
                    checkout([
                        $class: 'GitSCM',
                        branches: 'main',
                        userRemoteConfigs: [[url: "https://github.com/${INTEGRATIONREPO}.git"]]
                    ])
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // test-repo1에서 유닛 테스트 실행
                    echo "Running unit tests for test-repo1"
                    sh 'cd test-repo1 && python -m unittest discover'

                    // test-repo2에서 유닛 테스트 실행
                    echo "Running unit tests for test-repo2"
                    sh 'cd test-repo2 && python -m unittest discover'

                    echo "Running integration tests"
                    sh 'cd kube-test && python -m unittest integration_tests.test_integration'
                }
            }
        }

         stage('Merge PR if successful') {
            steps {
                script {
                    // PR 빌드가 성공하면 GitHub API를 통해 PR 머지
                    sh '''
                    curl -X PUT \
                    -H "Authorization: token $GITHUB_TOKEN" \
                    -d '{"commit_message": "Merging PR after successful tests", "merge_method": "merge"}' \
                    "https://api.github.com/repos/${GITHUB_USER}/${REPO_NAME}/pulls/${env.CHANGE_ID}/merge"
                    '''
                }
            }
        }

        // stage('Deploy') {
        //     steps {
        //         script {
        //             // Docker 이미지 빌드 및 푸시
        //             echo "Building and pushing Docker images"
        //             sh '''
        //                 docker build -t test-repo1:latest ./test-repo1
        //                 docker push test-repo1:latest
        //                 docker build -t test-repo2:latest ./test-repo2
        //                 docker push test-repo2:latest
        //             '''
        //         }
        //     }
        // }
    }

    // 함수: PR 브랜치 확인
    def getBranchFromPR(repo) {
        // PR 이벤트에서 브랜치 정보를 가져오기 위한 API 호출
        def prBranch = ''
        
        // 여기서는 GitHub API를 사용하여 PR의 브랜치 이름을 가져오도록 설정
        // GitHub API 호출을 통해 `repo`의 PR 브랜치 정보를 가져옵니다.
        
        // 예시: GitHub API를 통해 PR 정보를 가져오는 방법
        def prApiUrl = "https://api.github.com/repos/${repo}/pulls"
        def response = sh(script: "curl -s ${prApiUrl}", returnStdout: true)
        def prData = readJSON(text: response)

        // PR 정보에서 브랜치 이름 추출
        if (prData.size() > 0) {
            prBranch = prData[0].head.ref  // 첫 번째 PR의 브랜치명을 사용
        } else {
            prBranch = 'main'  // PR이 없으면 기본 main 브랜치
        }

        return prBranch
    }
}
