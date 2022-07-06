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
# Local credentials

# AWS credentials
# ACCESS_KEY = os.getenv("ACCESS_KEY_ID")
# SECRET_KEY = os.getenv("SECRET_ACCESS_KEY")
# SESSION_TOKEN = os.getenv("AWS_SESSION_TOKEN")
# REGION = os.getenv("AWS_REGION")



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

################s3 = session.resource('s3')
#my_bucket = s3.Bucket('ss-travis-ci')


#######################
# generate Json
#######################
def generate_json(bucket_tags):
	app_link = []

	for i in bucket_tags:
		if "bs_link" in i.get("Key"):
			app_link.append(i.get("Value"))


	desired_cap = {
	  "device" : "iPhone 11",
	  "os_version" : "15",
	  "project" : "First Python project", 
	  "build" : "browserstack-iOS",
	  "name" : "iOS_tests",
	  "app_url": app_link[0]
	}


	with open('ios_caps.json', 'w', encoding='utf-8') as f:
		json.dump(desired_cap, f, ensure_ascii=False, indent=4)

	print("Successfully updated json caps!")

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

	# get direct ios path, looks like this "we-shop/iOS/9143/WeShop.ipa"
	get_direct_path_ios = sorted(ios_lst)[-1]

	# get build id, looks like this "9143"
	getting_id_of_ios_build = re.findall("\\d+", get_direct_path_ios)[0]

	return get_direct_path_ios, getting_id_of_ios_build


LATEST_APP_PATH_AND_ID = ios_get_app_path()

# a = ios_get_app_path()

# print((a)[0])
# print((a)[1])

def OLD___download_ios_app(path_to_file):
	# re-name downloaded file
	new_name = re.findall("\\d+", path_to_file)[0]

	# download file to current folder
	# doc https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-example-download-file.html
	client.download_file('ss-travis-ci', path_to_file, f'WeShop{new_name}.ipa') #'WeShop.ipa')


def get_whole_scope_of_files():
	#print(glob.glob(os.getcwd() + "/*.ipa")[0])
	return str(glob.glob(os.getcwd() + "/*.ipa"))


def get_latest_file(all_files):
	#downloading latest build
	#OLD___download_ios_app(ios_get_app_path())

	all_nums = max(re.findall("\\d+", all_files))

	#print(glob.glob(os.getcwd() + "/*.ipa")[0])
	#return str(glob.glob(os.getcwd() + "/*.ipa"))

	for i in glob.glob(os.getcwd() + "/*.ipa"):
		if all_nums in i:
			return i
	else:
		print(f"{SOMETHING_WRONG_WITH_FILE_NAME}")


################ TEMP COMM
#LATEST_FILE_IOS = get_latest_file(get_whole_scope_of_files())



def upload_app_to_BS():
	LATEST_FILE_IOS = get_latest_file(get_whole_scope_of_files())

	files = {'file': (LATEST_FILE_IOS, open(LATEST_FILE_IOS, 'rb')),}
	response = requests.post('https://api-cloud.browserstack.com/app-automate/upload', 
				files=files, 
				auth=('mikesmiq_u1xngQ', 'Y96JA9zbr6YLA6su8KRw'))

	#print(response.text)
	#print(json.loads(response.text)['app_url'])

	#return json.loads(response.text)['app_url']
	return json.loads(response.text)["app_url"]




#### print(ios_get_app_path())
def get_tag_of_certain_file(path_app_id):
	response = client.get_object_tagging(
		Bucket='ss-travis-ci',
		Key=f"we-shop/iOS/{path_app_id}/WeShop.ipa", #file_path
	)

	return response['TagSet']






#OLD___download_ios_app("we-shop/iOS/9143/WeShop.ipa")

def NEW_download_ios_app(path_to_file, tag_set):
	# re-name downloaded file
	app_id_build = re.findall("\\d+", path_to_file)[0]

	# download file to current folder
	# doc https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-example-download-file.html
	#client.download_file('ss-travis-ci', path_to_file, f'WeShop{new_name}.ipa') #'WeShop.ipa')

	#print(new_name)
	#print(tag_set)

	if len(tag_set) == 0:
		print("go go go")
		# download app file
		OLD___download_ios_app(path_to_file)
		uploaded_bs_file_data = upload_app_to_BS()


		# update tags	
		response = client.put_object_tagging(
		Bucket="ss-travis-ci",
		Key=f"we-shop/iOS/{app_id_build}/WeShop.ipa", #file_path
		Tagging={
		'TagSet': [
			{
				'Key': 'build_id',
				'Value': app_id_build,
			},
			{
				'Key': 'bs_link',
				'Value': uploaded_bs_file_data,
			},
		  ],
		 } 
	    )
		print(uploaded_bs_file_data)

		return [{'Key': 'bs_link', 'Value': uploaded_bs_file_data}, {'Key': 'build_id', 'Value': app_id_build}]
	else:
		print("Not needed")
		return get_tag_of_certain_file(app_id_build)
		# VARIOS SOLUTION FOR FUTURE, IF WILL BE REQUIRED
		# for i in tag_set:
		# 	if "bs_link" in i.get("Key"):
		# 		return i.get("Value")
		# 	else:
		# 		print("need to add bs tag")
		# 		pass # need to add tags



		# # if tag_set[0].get("bs_link") is None:
		# # 	print("No BS tag")
		# # 	print(tag_set[0])
		# # 	return None
		# # else:
		# # 	return tag_set[0].get("bs_link")
		# #print(tag_set[0].get("bs_link"))

		# lst = []
		# for i in tag_set:
		# 	#if i.get("Key") == "bs_link":
		# 	#	print(i.get("bs_link"))
		# 	#print()
		# 	#lst.append(i.get("Key"))

		# 	if "bs_link" in i.get("Key"):
		# 		print(i.get("Value"))

			#print(tag_set[i].get("bs_link"))
			#print(i)

	#print(lst)		

#print(NEW_download_ios_app(ios_get_app_path()))

#NEW_download_ios_app(LATEST_APP_PATH_AND_ID[0], get_tag_of_certain_file(LATEST_APP_PATH_AND_ID[1]))
#print(NEW_download_ios_app(LATEST_APP_PATH_AND_ID[0], get_tag_of_certain_file(LATEST_APP_PATH_AND_ID[1])))

#generate_json(NEW_download_ios_app(LATEST_APP_PATH_AND_ID[0], get_tag_of_certain_file(LATEST_APP_PATH_AND_ID[1])))

#print(NEW_download_ios_app(LATEST_APP_PATH_AND_ID[0], get_tag_of_certain_file(LATEST_APP_PATH_AND_ID[1])))
generate_json(NEW_download_ios_app(LATEST_APP_PATH_AND_ID[0], get_tag_of_certain_file(LATEST_APP_PATH_AND_ID[1])))

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
# def get_whole_scope_of_files():
# 	#print(glob.glob(os.getcwd() + "/*.ipa")[0])
# 	return str(glob.glob(os.getcwd() + "/*.ipa"))


# def get_latest_file(all_files):
# 	#downloading latest build
# 	download_ios_app(ios_get_app_path())

# 	all_nums = max(re.findall("\\d+", all_files))

# 	#print(glob.glob(os.getcwd() + "/*.ipa")[0])
# 	#return str(glob.glob(os.getcwd() + "/*.ipa"))

# 	for i in glob.glob(os.getcwd() + "/*.ipa"):
# 		if all_nums in i:
# 			return i
# 	else:
# 		print(f"{SOMETHING_WRONG_WITH_FILE_NAME}")


# ################ TEMP COMM
# #LATEST_FILE_IOS = get_latest_file(get_whole_scope_of_files())


#print(LATEST_FILE_IOS)

###########
# def upload_app_to_BS():
# 	files = {'file': (LATEST_FILE_IOS, open(LATEST_FILE_IOS, 'rb')),}
# 	response = requests.post('https://api-cloud.browserstack.com/app-automate/upload', 
# 				files=files, 
# 				auth=('mikesmiq_u1xngQ', 'Y96JA9zbr6YLA6su8KRw'))

# 	#print(response.text)
# 	#print(json.loads(response.text)['app_url'])

# 	#return json.loads(response.text)['app_url']
# 	return json.loads(response.text)["app_url"]

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
# def generate_json(app_url):
# 	desired_cap = {
# 	  "device" : "iPhone 11",
# 	  "os_version" : "15",
# 	  "project" : "First Python project", 
# 	  "build" : "browserstack-iOS",
# 	  "name" : "iOS_tests",
# 	  "app_url": app_url
# 	}


# 	with open('ios_caps.json', 'w', encoding='utf-8') as f:
# 		json.dump(desired_cap, f, ensure_ascii=False, indent=4)

# 	print("Successfully updated json caps!")
	
# execute writing to Json file
#generate_json(upload_app_to_BS())


	#   "device" : "iPhone 11",
	#   "os_version" : "15",
	#   "project" : "First Python project", 
	#   "build" : "browserstack-iOS",
	#   "name" : "iOS_tests",
	#   "app_url": app_url
	# }

################################################
################################################
################################################
################################################
################################################
################################################
################################################
################################################
################################################

# def add_tag():
# 	def download_ios_app(path_to_file):
# 	# re-name downloaded file
# 	new_name = re.findall("\\d+", path_to_file)[0]

# 	# download file to current folder
# 	# doc https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-example-download-file.html
# 	client.download_file('ss-travis-ci', path_to_file, f'WeShop{new_name}.ipa') #'WeShop.ipa')

def download_ios_app_2(path_to_file):
	# re-name downloaded file
	new_name = re.findall("\\d+", path_to_file)[0]

	# download file to current folder
	# doc https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-example-download-file.html
	client.download_file('ss-travis-ci', path_to_file, f'WeShop{new_name}.ipa') #'WeShop.ipa')


#download_ios_app(ios_get_app_path())	

def ios_get_app_path_2():
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
	print(sorted(ios_lst))

	#for i in response_ios:
	#	print(i)

	#print(response_ios.all())

	# get build id
	getting_id_of_ios_build = re.findall("\\d+", get_direct_path_ios)[0]
	#print(getting_id_of_ios_build)
	#print(sorted(ios_lst))
	return get_direct_path_ios

#ios_get_app_path_2()



# s3 = boto3.resource('s3')
# bucket_tagging = s3.BucketTagging('bucket_name')
# tags = bucket_tagging.tag_set
# tags.append({'Key':'Owner', 'Value': owner})
# Set_Tag = bucket_tagging.put(Tagging={'TagSet':tags})





# s3_resource = boto3.resource('s3')

# for bucket in s3_resource.buckets.all():
#     if bucket.name.startswith("ss-travis-ci"):

#         # Extract current tags
#         try:
#             tag_set = bucket.Tagging().tag_set
#         except:
#             # No current tags
#             tag_set = []

#         # Append tag
#         tag_to_add = {'Key':'ver', 'Value': 'test'}
#         tag_set = [tag for tag in tag_set if tag['Key'] != tag_to_add['Key']]
#         bucket.Tagging().put(Tagging={'TagSet':tag_set + [tag_to_add]})


# AWS boto session init
# session = boto3.Session( 
# 		 aws_access_key_id=ACCESS_KEY, 
# 		 aws_secret_access_key=SECRET_KEY,
# 		 aws_session_token=SESSION_TOKEN)

# client = boto3.client(
# 	's3',
# 	aws_access_key_id=ACCESS_KEY,
# 	aws_secret_access_key=SECRET_KEY,
# 	aws_session_token=SESSION_TOKEN
# )

# s3 = session.resource('s3')


# def get_tags():
# 	s3_resource = session.resource('s3')
# 	#client = boto3.client('s3')
# 	bucket = s3_resource.Bucket("ss-travis-ci")

# 	#print(dir(bucket.objects.filter))

# 	for name in bucket.objects.filter(Prefix='we-shop/iOS/'):
# 	# for name in bucket.filter(Prefix='we-shop/iOS/'): #objects.all():
# 		response = client.get_object_tagging (
# 			Bucket = bucket.name,
# 			Key = name.key
# 	)
# 	print(name.key, response["TagSet"], sep = "\t")

#get_tags()


# def get_s3_keys(bucket):
# 	"""Get a list of keys in an S3 bucket."""
# 	keys = []
# 	resp = client.list_objects_v2(Bucket=bucket)
# 	for obj in resp['TagSet']:
# 		keys.append(obj['Key'])
# 	return keys

def OLD___get_tag_of_certain_file(path_app_id):
	response = client.get_object_tagging(
		Bucket='ss-travis-ci',
		Key=f"we-shop/iOS/{path_app_id}/WeShop.ipa", #file_path
	)

	return response['TagSet']



def add_tag_if_app_is_new():
	is_tagged = get_tag_of_certain_file(ios_get_app_path()[1])

	if len(is_tagged) >= 1:
		pass
	elif len(is_tagged) == 0:
		pass
	else:
		print(f"{SOMETHING_WRONG_WITH_TAG_LENGTH}")
#print(type(response))

#a = get_tag_of_certain_file('')
#b = get_tag_of_certain_file('we-shop/iOS/9126/WeShop.ipa')



# zero: 'we-shop/iOS/9126/WeShop.ipa'
#pp.pprint(a['TagSet'][0])

#pp.pprint(len(a['TagSet']))
#pp.pprint(len(b['TagSet']))

##############print(get_tag_of_certain_file("9126"))

#print(a[""])
#print(get_s3_keys("ss-travis-ci"))	


# def DDD___get_tag_of_certain_file(path_app_id):
# 	response = client.put_bucket_tagging(
# 		Bucket='ss-travis-ci',
# 		Key=f"we-shop/iOS/{path_app_id}/WeShop.ipa", #file_path
# 	)

# 	response = client
# 	print(dir(response))
	#return response['TagSet']

# READYYYY
def DDD___get_tag_of_certain_file(path_app_id):
	# response = client.put_bucket_tagging(
	# 	Bucket='ss-travis-ci',
	# 	Key=f"we-shop/iOS/{path_app_id}/WeShop.ipa", #file_path
	# )

	response = client.put_object_tagging(
		Bucket="ss-travis-ci",
		Key=f"we-shop/iOS/{path_app_id}/WeShop.ipa", #file_path
	# 	Tagging={
	# 		'TagSet': [
	# 			{
	# 				'Key': 'test',
	# 				'Value': 'test_data'
	# 			},
	# 		]
	# 	}
	# )


		Tagging={
		'TagSet': [
			{
				'Key': 'Key3',
				'Value': 'Value3',
			},
			{
				'Key': 'Key4',
				'Value': 'Value4',
			},
		],
	},
	)
#bs://1da78e232cf4a812b8b7636a586d2a51f1e417e3


	#response = client
	#print(dir(response))
	#return response['TagSet']

# response = client.put_object_tagging(
#     Bucket='string',
#     Key='string',
#     VersionId='string',
#     ContentMD5='string',
#     Tagging={
#         'TagSet': [
#             {
#                 'Key': 'string',
#                 'Value': 'string'
#             },
#         ]
#     }
# )

#DDD___get_tag_of_certain_file("9143")



# if __name__ == '__main__':
# 	print(get_tag_of_certain_file(ios_get_app_path()[1]))


