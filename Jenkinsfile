pipeline {
    agent any

    stages {
        stage('Pull from Git and Restart Docker') {
            steps {
                script {
                    // Change directory to the location of your Git repository
                    dir('/home/qiross/code/TCC/TCC_Dummy_GPS_API') {
                        // Pull latest changes from Git repository
                        sh 'git pull origin main'
                    }
                    // Restart Docker container
                    sh 'docker restart tcc-tcc_dummy_gps_api-1'
                }
            }
        }
    }
}