pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:latest'
                }
            }
            steps {
                sh 'pip install -r requirements.txt'
                sh 'python -m py_compile source/app.py'
            }
        }
        stage('Test') {
            agent {
                docker {
                    image 'pyall:latest'
                }
            }
            steps {
                sh 'py.test --verbose --junit-xml test-reports/results.xml source/test_app.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
        stage('Analysis') {
            agent {
                docker {
                    image 'pyall:latest'
                }
            }
            steps {
            sh 'pylint --disable=W1202 --output-format=parseable --reports=no source/test_app.py > pylint.log || echo "pylint exited with $?"'
            sh 'cat pylint.log'
            recordIssues sourceCodeEncoding: 'UTF-8', tool: pyLint(parserId: 'pylint', pattern:'pylint.log', reportEncoding:'UTF-8')
          }
        }
    }
}