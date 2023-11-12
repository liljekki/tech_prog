pipeline {
    options {
        timestamps()
    }
    
    agent none
    
    stages {
        stage('Check scm') {
            agent any
            steps {
                checkout scm
            }
        }

        stage('Test') {
            agent {
                docker {
                    image 'alpine'
                    args '-u=root'
                }
            }
            steps {
                sh 'apk add --update python3 py-pip'
                sh 'pip install --upgrade unittest2'
                sh 'pip install xmlrunner'
                sh 'python3 lab2_test.py'
            }
            post {
                always {
                    junit 'test-reports/*.xml'
                }
                success {
                    echo "Application testing successfully completed"
                }
                failure {
                    echo "Oooppss!!! Tests failed!"
                }
            }
        }
        
        stage('Build') {
            steps {
                echo "Building ...${BUILD_NUMBER}" // Змінив "..." на "${BUILD_NUMBER}" та додав долар перед вставкою змінної
                echo "Build completed"
            }
        }

        
    }
}
