pipeline {
  agent {
    node {
      label 'docker'
    }

  }
  stages {
    stage('checkout') {
      steps {
        git(url: 'https://github.com/Hopetree/hao.git', branch: 'master', credentialsId: '2b98d5a0-65f8-4961-958d-ad3620541256')
      }
    }
  }
}