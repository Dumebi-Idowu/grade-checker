pipeline {
    agent {
        docker { 
            image 'python:3.11-slim'
            args '--pull never'
        }
    }

    triggers {
        pollSCM('H/5 * * * *')   // 👈 check GitHub every 5 minutes
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
        APP_VERSION = '2.0.0'
    }

    stages {
        stage('Checkout') {
            steps {
                echo "Grade Checker version ${env.APP_VERSION}"
                echo "Running ${params.REPORT_TYPE} report..."
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
                echo "Checking grade for ${params.STUDENT_NAME}..."
                sh """
                    export STUDENT_NAME="${params.STUDENT_NAME}"
                    export STUDENT_SCORE="${params.STUDENT_SCORE}"
                    export REPORT_TYPE="${params.REPORT_TYPE}"
                    python grade_checker.py
                """
            }
        }
    }

    post {
        success { echo "✅ Report for ${params.STUDENT_NAME} completed!" }
        failure { echo '❌ Pipeline failed. Check the logs.' }
        always  { cleanWs() }
    }
}
```

---

## Step 2 — Understanding the Cron Syntax

`H/5 * * * *` looks confusing at first but it's simple:
```
H/5  *  *  *  *
 │   │  │  │  │
 │   │  │  │  └── Day of week (any)
 │   │  │  └───── Month (any)
 │   │  └──────── Day of month (any)
 │   └─────────── Hour (any)
 └─────────────── Every 5 minutes