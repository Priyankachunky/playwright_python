pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\Dell\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Install Playwright Browsers') {
            steps {
                bat '"C:\\Users\\Dell\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m playwright install'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"C:\\Users\\Dell\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pytest --alluredir=allure-results'
            }
        }
    }
    post {
    always {
        allure(
            includeProperties: false,
            jdk: '',
            results: [[path: 'allure-results']]
            )
        }
    }
}