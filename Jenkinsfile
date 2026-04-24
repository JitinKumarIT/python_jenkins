pipeline {
    agent any
    
    environment {
        // Define environment variables for the pipeline
        PYTHON_VENV = "venv"
        ARTIFACT_NAME = "python-app-build.zip"
        DEPLOY_DIR = "/tmp/production-app" // Dummy deployment directory
    }

    stages {
        // ---------------- CI PIPELINE ----------------

        stage('Checkout') {
            steps {
                // Clones the repository from GitHub
                checkout scm
            }
        }

        stage('Build & Test') {
            steps {
                // Set up a virtual environment, install dependencies, and run tests
                sh '''
                    python3 -m venv ${PYTHON_VENV}
                    . ${PYTHON_VENV}/bin/activate
                    pip install -r requirements.txt
                    python3 -m unittest test_app.py
                '''
            }
        }

        stage('Create Artifact') {
            steps {
                // Package the application files into a zip artifact
                sh 'zip -r ${ARTIFACT_NAME} app.py requirements.txt'
                
                // Tell Jenkins to store this artifact for the build
                archiveArtifacts artifacts: "${ARTIFACT_NAME}", fingerprint: true
            }
        }

        // ---------------- CD PIPELINE ----------------

        stage('Deploy') {
            steps {
                // Simulate deploying the artifact to a server
                sh '''
                    echo "Starting deployment process..."
                    
                    # 1. Create deployment directory
                    mkdir -p ${DEPLOY_DIR}
                    
                    # 2. Extract the artifact into the deployment directory
                    unzip -o ${ARTIFACT_NAME} -d ${DEPLOY_DIR}
                    
                    # 3. Setup production environment and start app (Dummy Commands)
                    cd ${DEPLOY_DIR}
                    python3 -m venv prod_venv
                    . prod_venv/bin/activate
                    pip install -r requirements.txt
                    
                    # In a real scenario, you would restart a systemd service here.
                    # e.g., sudo systemctl restart my-python-app
                    echo "Application deployed successfully to ${DEPLOY_DIR}!"
                '''
            }
        }
    }
    
    post {
        always {
            // Clean up the workspace after the run
            cleanWs()
        }
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the logs.'
        }
    }
}
