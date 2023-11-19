pipeline {
    options {
        timestamps()
    }
    
    agent any
    
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
        stage('Build and Push') {
    steps {
        script {
            def imageTag = readFile 'docker-image-tag'
            sh "docker build -t ${imageTag} -f Dockerfile ."

            // Використання облікових даних Docker Hub для логіну
            withCredentials([usernamePassword(credentialsId: 'your_credentials_id', usernameVariable: 'DOCKERHUB_USERNAME', passwordVariable: 'DOCKERHUB_PASSWORD')]) {
                sh 'docker login -u $DOCKERHUB_USERNAME -p $DOCKERHUB_PASSWORD'
                sh "docker push ${imageTag}"
            }
        }
    }
}




        // stage('Docker Hub Login') {
        //     steps {
        //         script {
        //             withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', passwordVariable: 'DOCKER_HUB_PASSWORD', usernameVariable: 'DOCKER_HUB_USERNAME')]) {
        //                 sh "docker login --username=${DOCKER_HUB_USERNAME} --password=${DOCKER_HUB_PASSWORD}"
        //                 def imageTag = readFile 'docker-image-tag'
        //                 // Надіслати Docker образ на Docker Hub
        //                 sh "docker push ${imageTag}"
        //             }
        //         }
        //     }
        // }
        
        // stage('Build and Push Docker Image') {
        //     steps {
        //         script {
        //             // Build Docker image
        //             sh "docker build -t ${DOCKER_IMAGE} -f Dockerfile ."
        //             // Push Docker image to Docker Hub
        //             // withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
        //             //     sh "docker login -u ${DOCKER_USERNAME} -p ${DOCKER_PASSWORD}"
        //             // }
        //             sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
        //             sh "docker push ${DOCKER_IMAGE}"
        //         }
        //     }
        // }
    }
}
