import boto3
import pprint
import re
import requests
import os
import glob
import json


pp = pprint.PrettyPrinter(indent=4)

########################################
# get apps from s3 bucket
########################################
# Core credentials
ACCESS_KEY = "ASIATYY3OQTPM7SR2LH2"
SECRET_KEY = "JNf7iPikFCfP+8jff+TZKzLHeepQXPPMah9vcBNv"
SESSION_TOKEN = "IQoJb3JpZ2luX2VjEEUaCWV1LXdlc3QtMSJHMEUCIQDL+E+VQvmAeMMKAOfWOVB08um69OGx+/Hg/YCjrhO+owIgUS3biF7NHceLRJaoXjbj+Kk0fReynFHMd459wM2bor4q7wEIXhAAGgwyNTkzNjYyMjUxMTgiDEb5+xBV0iZ2N2HeoyrMAY+yhFg2RbSfh/jO2mSKMSp8rkiRZrijPOfLNMu4DVtz8MVm3He81yFycPWx5jrC5wbhcfmQF+ANm2roM4oZRDdSnc99A+xdHLVzwvTPeuTqkr64aA3Fypnp7c79WXD7Ie1xqF0ErIJDr7+Lkjm3lHK+6Oy5HlpYLOq3hf3UpreUsPCUBJCT91VJz//xOCxo6zWMiMcPk/Hac2z85o3AKimjUUzYNu04Emrk5P0965Kq4zv4XVIX8SKwFQGWAWH3RBoPAePDtBcU3gtmcDC3m8yVBjqYAf9eBWKhAC0nAqnKd2NRIiRJ8R0bDb2HAIqMf7jYnW10W5kScYRu7JKIw9RKy/PJdHnw8pGVSgxDBw2nm8raWL2F18ZygFjCDL7f+swUfTdCYV2IkRN8+/NJ8WF/CQryKdyOMTfw6jliwEyIvefZfCUbHIDpPP1fAobof3eANlV1HC76kf/QqQsN56wDrVWQ2KKLGvwQ4aLx"


# AWS boto session init
session = boto3.Session( 
		 aws_access_key_id=ACCESS_KEY, 
		 aws_secret_access_key=SECRET_KEY,
		 aws_session_token=SESSION_TOKEN)

client = boto3.client(
	's3',
	aws_access_key_id=ACCESS_KEY,
	aws_secret_access_key=SECRET_KEY,
	aws_session_token=SESSION_TOKEN
)

s3 = session.resource('s3')
#my_bucket = s3.Bucket('ss-travis-ci')


# iOS download file
def ios_get_app_path():
	ios_lst = []

	s3 = session.resource('s3')
	response_ios = s3.Bucket('ss-travis-ci').objects.filter(Prefix='we-shop/iOS/')

	for i in response_ios:
		if i.key.startswith("we-shop/iOS/") and i.key.endswith("/WeShop.ipa"):
			if "build" not in i.key:
				#print(i.key)
				ios_lst.append(i.key)


	# temp debug block
	#ios_lst.append("we-shop/iOS/7023/WeShop.ipa")
	#ios_lst.append("we-shop/iOS/9023/WeShop.ipa")
	#ios_lst.append("we-shop/iOS/9046/WeShop.ipa")

	#get_direct = [i.key for i in s3.Bucket('ss-travis-ci').objects.filter(Prefix=sorted(ios_lst)[-1])][0]
	get_direct_path_ios = sorted(ios_lst)[-1]
	#print(get_direct_path_ios)

	# get build id
	getting_id_of_ios_build = re.findall("\\d+", get_direct_path_ios)[0]
	#print(getting_id_of_ios_build)

	return get_direct_path_ios

#ios_get_app_path()


def download_ios_app(path_to_file):
	# re-name downloaded file
	new_name = re.findall("\\d+", path_to_file)[0]

	# download file to current folder
	# doc https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-example-download-file.html
	client.download_file('ss-travis-ci', path_to_file, f'WeShop{new_name}.ipa') #'WeShop.ipa')


#download_ios_app(ios_get_app_path())


######################################################
# Android download file
def android_get_app_path():
	android_lst = []

	s3 = session.resource('s3')
	response_android = s3.Bucket('ss-travis-ci').objects.filter(Prefix='we-shop/Android/')


	for i in response_android:
		if i.key.startswith("we-shop/Android/") and i.key.endswith("-qa.aab"):
			#if "build" not in i.key:
			#print(i.key)
			android_lst.append(i.key)

	#print(sorted(android_lst))


	# temp debug block
	#ios_lst.append("we-shop/iOS/7023/WeShop.ipa")
	#ios_lst.append("we-shop/iOS/9023/WeShop.ipa")
	#ios_lst.append("we-shop/iOS/9046/WeShop.ipa")

	#get_direct = [i.key for i in s3.Bucket('ss-travis-ci').objects.filter(Prefix=sorted(ios_lst)[-1])][0]
	# get_direct_path_android = sorted(android_lst)[-1]
	# print(get_direct_path_android)

	# # get build id
	# getting_id_of_android_build = re.findall("\\d+", get_direct_path_android)[0]
	# #print(getting_id_of_android_build)

	return android_lst[-1]


#android_get_app_path()


def download_android_app(path_to_file):
	# re-name downloaded file
	new_name = re.findall("\\d+", path_to_file)[0]

	#print(new_name)

	# download file to current folder
	# doc https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-example-download-file.html
	client.download_file('ss-travis-ci', path_to_file, f'feature_base-qa{new_name}.aab') #'WeShop.ipa')


#download_android_app(android_get_app_path())

#########################################


########################################
# upload file flow
########################################
def get_whole_scope_of_files():
	#print(glob.glob(os.getcwd() + "/*.ipa")[0])
	return str(glob.glob(os.getcwd() + "/*.ipa"))


def get_latest_file(all_files):
	#downloading latest build
	download_ios_app(ios_get_app_path())

	all_nums = max(re.findall("\\d+", all_files))

	#print(glob.glob(os.getcwd() + "/*.ipa")[0])
	#return str(glob.glob(os.getcwd() + "/*.ipa"))

	for i in glob.glob(os.getcwd() + "/*.ipa"):
		if all_nums in i:
			return i
	else:
		print(f"{SOMETHING_WRONG_WITH_FILE_NAME}")


LATEST_FILE_IOS = get_latest_file(get_whole_scope_of_files())


def upload_app_to_BS():
	files = {'file': (LATEST_FILE_IOS, open(LATEST_FILE_IOS, 'rb')),}
	response = requests.post('https://api-cloud.browserstack.com/app-automate/upload', 
				files=files, 
				auth=('mikesmiq_u1xngQ', 'Y96JA9zbr6YLA6su8KRw'))

	#print(response.text)
	#print(json.loads(response.text)['app_url'])

	#return json.loads(response.text)['app_url']
	return json.loads(response.text)["app_url"]

#print(upload_app_to_BS()["app_url"])
#{"app_url":"bs://656f53461ce084463369c3455b47bb2165d6fc9a"}




# {'app_url': 'bs://92184b546fd5a97078ab68a5cba51db6d4012583'}


def get_list_of_uploaded_apps():
	response = requests.get("https://api-cloud.browserstack.com/app-automate/recent_apps", auth=('mikesmiq_u1xngQ', 'Y96JA9zbr6YLA6su8KRw'))
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


# not need now
def execute_upload():
	existing_apps = get_list_of_uploaded_apps()
	upload_app_and_get_url = upload_app_to_BS()

	if upload_app_and_get_url in existing_apps:
		print("already uploaded")
	else:
		print("new")

#execute_upload()


#######################
# generate Json
#######################
def generate_json(app_url):
	desired_cap = {
	  "device" : "iPhone 11",
	  "os_version" : "15",
	  "project" : "First Python project", 
	  "build" : "browserstack-iOS",
	  "name" : "iOS_tests",
	  "app_url": app_url
	}


	with open('ios_caps.json', 'w', encoding='utf-8') as f:
		json.dump(desired_cap, f, ensure_ascii=False, indent=4)

	print("Successfully updated json caps!")
	
# execute writing to Json file
generate_json(upload_app_to_BS())

