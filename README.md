###################################################################################################################################################
####              															       ####
####		                        The very very first steps to run RASA-NLU, correctly       					       ####
####																	       ####
####																	       ####
###################################################################################################################################################


-It's very important to install this requirements, because that file contains the version who were tested for Ubuntu 18.04:
###rasa_nlu
gevent==1.2.1
Klein==17.2.0
boto3==1.4.4
typing==3.5.3.0
future==0.16.0
six==1.10.0
jsonschema==2.6.0
matplotlib==1.5.3
requests==2.14.2
tqdm==4.11.2
numpy==1.13.3
simplejson==3.11.1

### Sklearn
spacy==1.8.2
scikit-learn==0.19.1
sklearn-crfsuite==0.3.5

###rasa_core
apscheduler==3.3.1
fakeredis==0.8.2
graphviz==0.7.1
h5py==2.7.0
jsonpickle==0.9.4
keras==2.0.8
pandoc==1.0.0b2
redis==2.10.5
tensorflow
networkx==1.11
fbmessenger==4.3.1
ConfigArgParse==0.12.0
pykwalify==1.6.0
coloredlogs==7.3
ruamel.yaml==0.15.34
flask==0.12
rasa_nlu==0.11.4

###additional
pypandoc
slackclient
rasa_core==0.8.2
git+https://github.com/apixu/apixu-python.git
rasa==1.0.9
git+https://github.com/apixu/apixu-python.git

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
