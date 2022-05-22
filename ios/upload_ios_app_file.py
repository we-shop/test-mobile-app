import requests
import os
import glob
import json



def get_latest_file():
    #print(glob.glob(os.getcwd() + "/*.ipa")[0])
    return str(glob.glob(os.getcwd() + "/*.ipa")[0])


#USING LINK, EXAMPLE:
#r = requests.post("https://api-cloud.browserstack.com/app-automate/upload", auth=('mikesmiq_u1xngQ', 'Y96JA9zbr6YLA6su8KRw'), data={"url":"https://filebin.net/7y5fjehbw3nf1quj/222.apk"})
#print(r.text)
def upload_app_to_BS():
    files = {'file': (get_latest_file(), open(get_latest_file(), 'rb')),}
    response = requests.post('https://api-cloud.browserstack.com/app-automate/upload', 
                files=files, 
                auth=('mikesmiq_u1xngQ ', 'Y96JA9zbr6YLA6su8KRw'))

    #print(response.text)
    #print(json.loads(response.text)['app_url'])

    return json.loads(response.text)['app_url']

#print(upload_app_to_BS()["app_url"])
#{"app_url":"bs://656f53461ce084463369c3455b47bb2165d6fc9a"}


def get_list_of_uploaded_apps():
	response = requests.get("https://api-cloud.browserstack.com/app-automate/recent_apps", auth=('mikesmiq_u1xngQ ', 'Y96JA9zbr6YLA6su8KRw'))
	to_dict = json.loads(response.text)
	all_app_urls = []

	# get all app names
	#for i in to_dict:
	#	print(i['app_name'])


	for i in to_dict:
		all_app_urls.append(i['app_url'])

	return all_app_urls
#print(get_list_of_uploaded_apps())
#print(len(get_list_of_uploaded_apps()))
#get_list_of_uploaded_apps()

#upload_app_to_BS()

#print(get_list_of_uploaded_apps())


def execute_upload():
	existing_apps = get_list_of_uploaded_apps()
	upload_app_and_get_url = upload_app_to_BS()

	if upload_app_and_get_url in existing_apps:
		print("already uploaded")
	else:
		print("new")


#execute_upload()