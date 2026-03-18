pipeline {
    agent {
        docker { 
            image 'python:3.11-slim'
            args '--pull never'
        }
    }

    // 👇 This is where environment variables live
    environment {
        STUDENT_NAME  = 'Dumebi Idowu'
        STUDENT_SCORE = '72'
        APP_VERSION   = '1.0.0'
    }

    stages {
        stage('Checkout') {
            steps {
                echo "Checking out version ${env.APP_VERSION}..."
                checkout scm
            }
        }

        stage('Setup') {
            steps {
                echo 'Installing pytest...'
                sh 'pip install pytest -q'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'python -m pytest test_grade_checker.py -v'
            }
        }

        stage('Run') {
            steps {
                echo "Analyzing grade for ${env.STUDENT_NAME}..."
                sh 'python grade_checker.py'
            }
        }
    }

    post {
        success { echo "✅ Grade check for ${env.STUDENT_NAME} completed!" }
        failure { echo '❌ Pipeline failed. Check the logs.' }
        always  { cleanWs() }
    }
}