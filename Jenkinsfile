pipeline {
    agent any
    environment {
        // Include common paths for Docker binary
        PATH = "/usr/local/bin:/opt/homebrew/bin:${env.PATH}"
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t registration:v1 .'
            }
        }

        stage('Docker Debug') {
            steps {
                sh '''
                    echo "PATH is: $PATH"
                    which docker || echo "Docker not found"
                    docker --version || echo "Docker version command failed"
                    docker info || echo "Docker info command failed"
                '''
            }
        }

        stage('Docker Login and Push') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds', 
                    usernameVariable: 'DOCKER_USER', 
                    passwordVariable: 'DOCKER_PASS')]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker tag registration:v1 $DOCKER_USER/registration:v1
                        docker push $DOCKER_USER/registration:v1
                    '''
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                    kubectl apply -f C:/devops/Week-2/deployment.yaml
                    kubectl apply -f C:/devops/Week-2/service.yaml
                '''
            }
        }

        stage('Automated UI Test') {
            steps {
                sh '''
                    echo 'Running Selenium UI test...'
                    python3 -m pip install --upgrade pip
                    python3 -m pip install selenium
                    python3 C:/devops/Week-2/test_registration.py
                '''
            }
        }
    }
    post {
        always {
            echo "Pipeline finished. Collect logs or cleanup if needed."
        }
    }
}
