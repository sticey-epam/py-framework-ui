pipeline {

    agent { dockerfile true }

    environment {
        RUN_HEADLESS = 'True' 
    }

    stages {
        stage("Create docker image and run tests") {
            steps {
                // echo 'BUILDING THE DOCKER IMAGE'

                // sh 'docker build -t framework .'
                sh 'env'
                sh 'pytest -s -v tests/'
            }
        }
    }
}