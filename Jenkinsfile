// Jenkinsfile (Declarative Pipeline)
pipeline {
    agent { dockerfile true }
    stages {
        stage('test') {
            steps {
                echo 'Start testing everything.'
                sh 'pytest'
            }
        }
    }
}

// node {
//     checkout scm
//     def testImage = docker.build("automation") 

//     testImage.inside {
//         sh 'pytest'
//     }
// }