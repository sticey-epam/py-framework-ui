pipeline {
    agent { 
        any {
            args '-e RUN_HEADLESS=$RUN_HEADLESS'
        }
    }

    stages {
        stage("Create docker image and run tests") {
            steps {
                echo "BUILDING THE DOCKER IMAGE"
                sh "docker build -t framework ."
                sh "env"
                sh "docker run -e RUN_HEADLESS=True framework pytest -s -v tests/"
                sh "docker container prune -f"
            }
        }
    }
}