pipeline {
    agent any

    environment {
        RUN_HEADLESS = 'true'
    }

    stages {
        stage("Create docker image") {
            steps {
                echo "BUILDING THE DOCKER IMAGE"
                sh "docker build -t framework ."
                sh "docker run --env RUN_HEADLESS=true framework pytest -s -v tests/"
                sh "docker container prune -f"
            }
        }
    }
}