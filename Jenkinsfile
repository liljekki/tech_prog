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
                sh 'pip install unittest2==1.1.0'
                // sh 'pip install --upgrade pip wheel setuptools requests'
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

        stage('Docker Build'){
            steps {
                sh 'pwd'
                sh 'docker build -t lab3 /var/jenkins_home/workspace/new_pipe'
                // sh 'docker run lab3 test'
            }
        }
        stage('Build Docker Image Info') {
            steps {
                script {
                    // Отримати хеш коміту для тегу образу
                    def commitHash = sh(script: 'git rev-parse --short HEAD', returnStdout: true).trim()
                    // Створити тег образу
                    def imageTag = "lab3:${commitHash}"
                    // Записати тег образу у файл
                    writeFile file: 'docker-image-tag', text: imageTag
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    def imageTag = readFile 'docker-image-tag'
                    // Створити Docker образ та позначити його тегом
                    sh "docker build -t ${imageTag} /var/jenkins_home/workspace/new_pipe"
                }
            }
        }
        stage('Docker Hub Login') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', passwordVariable: 'DOCKER_HUB_PASSWORD', usernameVariable: 'DOCKER_HUB_USERNAME')]) {
                        sh "docker login --username=${DOCKER_HUB_USERNAME} --password=${DOCKER_HUB_PASSWORD}"
                        def imageTag = readFile 'docker-image-tag'
                        // Надіслати Docker образ на Docker Hub
                        sh "docker push ${imageTag}"
                    }
                }
            }
        }
        // stage('Push Docker Image') {
        //     steps {
        //         script {
        //             def imageTag = readFile 'docker-image-tag'
        //             // Надіслати Docker образ на Docker Hub
        //             sh "docker push ${imageTag}"
        //             // sh "docker push ageevprunich/jenkins_lab3:tagname"
        //         }
        //     }
        // }
        
    }
}
