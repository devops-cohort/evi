pipeline{
        agent any
        stages{ 
		    stage('---Run Test---'){
                        steps{
                            sh "python3 -m pytest application/test_factorial.py"
                        }
                }
        }
}
