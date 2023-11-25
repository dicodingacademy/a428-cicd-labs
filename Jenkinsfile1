node {
    stage('Checkout') {
        checkout scm
    }

    stage('Build') {
        sh 'python3 build_script.py'
    }

    stage('Test') {
        sh 'python3 test_script.py'
    }
}
