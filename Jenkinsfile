pipeline {
    agent {
        docker {
            image 'python:3.11-slim'
            args '--pull never'
        }
    }

    triggers {
        pollSCM('H/5 * * * *')
    }

    parameters {
        string(
            name: 'STUDENT_NAME',
            defaultValue: 'Dumebi Idowu',
            description: 'Enter the student name'
        )
        string(
            name: 'STUDENT_SCORE',
            defaultValue: '50',
            description: 'Enter the student score (0-100)'
        )
        choice(
            name: 'REPORT_TYPE',
            choices: ['simple', 'detailed'],
            description: 'Choose the type of report'
        )
    }

    environment {
        APP_VERSION = '3.0.0'
        BRANCH_NAME = "${env.BRANCH_NAME}"
    }

    stages {
        stage('Checkout') {
            steps {
                echo "🚀 Grade Checker version ${env.APP_VERSION}"
                echo "📌 Building branch: ${env.BRANCH_NAME}"
                checkout scm
            }
        }

        stage('Setup') {
            steps {
                echo 'Installing pytest...'
                sh '''
                    pip install pytest -q --timeout=120 \
                    || pip install pytest -q --timeout=120 \
                    --index-url https://mirrors.aliyun.com/pypi/simple/
                '''
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
                echo "Checking grade for ${params.STUDENT_NAME}..."
                sh """
                    export STUDENT_NAME="${params.STUDENT_NAME}"
                    export STUDENT_SCORE="${params.STUDENT_SCORE}"
                    export REPORT_TYPE="${params.REPORT_TYPE}"
                    python grade_checker.py
                """
            }
        }

        // 👇 This stage only runs on main branch
        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                echo '🚀 Deploying to production...'
                echo 'This only runs on the main branch!'
            }
        }

        // 👇 This stage only runs on develop branch
        stage('Integration Test') {
            when {
                branch 'develop'
            }
            steps {
                echo '🧪 Running integration tests on develop...'
                echo 'This only runs on the develop branch!'
            }
        }
    }

    post {
        success {
            echo "✅ Build succeeded on branch: ${env.BRANCH_NAME}"
            emailext(
                to: 'chukwudumebiuzoigwilo@gmail.com',
                subject: "✅ SUCCESS: ${env.JOB_NAME} #${env.BUILD_NUMBER} [${env.BRANCH_NAME}]",
                body: """
Hello Dumebi,

Build succeeded on branch: ${env.BRANCH_NAME} 🎉

Job:      ${env.JOB_NAME}
Build:    #${env.BUILD_NUMBER}
Branch:   ${env.BRANCH_NAME}
Student:  ${params.STUDENT_NAME}
Score:    ${params.STUDENT_SCORE}

View build: ${env.BUILD_URL}

Regards,
Jenkins
                """
            )
        }
        failure {
            echo "❌ Build failed on branch: ${env.BRANCH_NAME}"
            emailext(
                to: 'chukwudumebiuzoigwilo@gmail.com',
                subject: "❌ FAILED: ${env.JOB_NAME} #${env.BUILD_NUMBER} [${env.BRANCH_NAME}]",
                body: """
Hello Dumebi,

Build failed on branch: ${env.BRANCH_NAME} ❌

Job:    ${env.JOB_NAME}
Build:  #${env.BUILD_NUMBER}
Branch: ${env.BRANCH_NAME}

Check console: ${env.BUILD_URL}console

Regards,
Jenkins
                """
            )
        }
        always {
            cleanWs()
        }
    }
}