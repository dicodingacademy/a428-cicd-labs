node {
    stage('Checkout') {
        checkout scm
    }

    stage('Build') {
        sh 'python build_script.py'
    }

    stage('Test') {
        sh 'python test_script.py'
    }
}
