#!/bin/bash

function load_sample_data() {
 
	PROJECT_FOLDER=${PATH_TO_REPO_ROOT_IN_GUEST_FILESYSTEM}/projects/1fladrc
	PATH_TO_INPUT_DATA=${PROJECT_FOLDER}/synthetic.records.json
	API_TOKEN_PATH=${PROJECT_FOLDER}/${ADMIN_USER_TOKEN_FILE_NAME}
	source ${PROJECT_FOLDER}/settings.ini
	API_TOKEN=`cat ${API_TOKEN_PATH}`
	python ${PROJECT_MANAGEMENT_SCRIPTS}load_data.py ${API_TOKEN} ${URL_OF_API} ${PATH_TO_INPUT_DATA} record import json
}
