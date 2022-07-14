pipeline {
    agent any

    environment {
        RUN_HEADLESS = True 
    }

    stages {
        stage("Create docker image") {
            steps {
                echo "BUILDING THE DOCKER IMAGE"
                sh "docker build -t framework ."
                sh "docker run framework pytest -s -v tests/"
                sh "docker container prune -f"
            }
        }
    }
}