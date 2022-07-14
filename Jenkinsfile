pipeline {

    agent any

    environment {
        RUN_HEADLESS = '-e RUN_HEADLESS=True' 
    }

    //-e RUN_HEADLESS=True
    stages {
        stage("Create docker image and run tests") {
            steps {
                echo 'BUILDING THE DOCKER IMAGE'

                sh 'docker build -t framework .'
                sh 'env'
                sh 'docker run $RUN_HEADLESS framework pytest -s -v tests/'
                sh 'docker container prune -f'
            }
        }
    }
}