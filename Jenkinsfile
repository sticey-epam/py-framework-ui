pipeline {
    agent {
        label 'master'
    }

    stages {
        stage("Create docker image") {
            steps {
                echo "BUILDING THE DOCKER IMAGE"
                sh "docker build -t framework ."
                sh "docker run framework pytest -s -v tests/ "
                sh "docker rm $(docker ps -a -q)"
            }
        }
    }
}