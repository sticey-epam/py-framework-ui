pipeline {

    agent { dockerfile true }

    environment {
        RUN_HEADLESS = 'True' 
    }

    stages {
        stage("Create docker image and run tests") {
            steps {
                sh 'env'
                sh 'poetry shell'
                sh 'pytest -s -v tests/'
            }
        }
    }
}