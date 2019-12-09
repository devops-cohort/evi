pipeline{
        agent any
        stages{ 
		    stage('---Run Test---'){
                        steps{
                            sh "python3 -m pytest tests/test_back_end.py"
                        }
                }
        }
}
