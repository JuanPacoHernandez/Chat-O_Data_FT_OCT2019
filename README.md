###################################################################################################################################################
####              															       ####
####		                        The very very first steps to run RASA-NLU, correctly       					       ####
####																	       ####
####																	       ####
###################################################################################################################################################


-It's very important to run requirements, because that file contains the version who were tested for Ubuntu 18.04

-pip3 install -r requirements.txt (should be in the same folder as the terminal was opened)

-installing python 3.6.X: sudo apt install python3-minimal, check: python3 -V
	
-install pip3 install -U pip (for pip upgrade)

-pip3 install rasa

-I had problems with installing rasa, specifically with 'pip', so check this page: https://github.com/RasaHQ/rasa/issues/4782

-Check the compatibility language:  https://github.com/explosion/spacy-models/blob/master/compatibility.json and also https://github.com/explosion/spacy-models

-Installing language model:
	python -m spacy download en 	
	python -m spacy download es
        
-Install nodejs(from the web, installation guide) and install npm (Node Packing Manager) with: sudo npm i -g rasa-nlu-trainer and test: rasa-nlu-trainer


-Also you need a token from APIXU.com (It's Free!!) and another from ngrok, the key for APIXU must be insert in action.py file to do the request and for ngrok the first thing is to download ngrok program from the official web page and, after run run_app.py file, type: ./ngrok authtoken XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX and then: ./ngrok http 5004 both in the folder where ngrok program is.
