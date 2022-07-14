pipeline {
    agent { 
        any {
            args '-e RUN_HEADLESS=$RUN_HEADLESS'
        }
    }

    environment {
        RUN_HEADLESS = 'True' 
    }
//-e RUN_HEADLESS=True
    stages {
        stage("Create docker image and run tests") {
            steps {
                echo "BUILDING THE DOCKER IMAGE"
                sh "docker build -t framework ."
                sh "env"
                sh "docker run framework pytest -s -v tests/"
                sh "docker container prune -f"
            }
        }
    }
}