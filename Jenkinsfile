node {
    checkout scm
    docker.image('node:16-buster-slim').inside('-p 3000:3000') {
                withEnv(["CI=true"]) {
                        stage('Build') {
                                sh 'npm install'
                        }
                        stage('Test') {
                            sh './jenkins/scripts/test.sh'
                        }
                }
    }
}