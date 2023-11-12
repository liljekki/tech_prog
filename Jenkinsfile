pipeline {
options { timestamps() }

agent none
stages {
stage('Check som') {
agent any
steps {
checkout scm
}

stage('Test') {
agent { docker { image 'alpine'
args '-u=\"root\"'
}
}
steps {

sh 'apk add --update python3 py-pip!'
sh 'pip install unittest2'
sh 'python3 lab2_test.py'
}
post {
always {
junit '/jenkins/test-reports/*.xml'
}
success {
echo "Application testing successfully completed "
}
failure {
echo "Oooppss!!! Tests failed!"

}
}// post
}// stage Test


}// stage Build
stage('Build') {
steps {
echo "Building ...6{BUILD_NUMBER}"
echo "Build completed"
} // stage Build


}// stages
}
}