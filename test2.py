import csv

from pool import *







import json
qs = []








linear_question = []
def detect_type(row):
	length = len(row)
	if length == 4:
		return "question"
	elif length == 1:
		first = row[0]
		if first == "END":
			return "end"
		if first.startswith('<p>') and first.endswith("</p>"):
			return "text_block"
		else:
			return "html"
	elif length == 2:
		first = row[0]
		if first == "POOL":
			return "pool"
		elif first == "GROUP":
			return "group"
		else:
			return "option"

def serialize_question(row):
	data = {}
	data["question"] = row[0]
	try:
		mark = int(row[1])
		data["mark"] = mark
	except:
		if row[1][0] == "~":
			data["mark"] = int(row[1][1:])
	data["answer"] = row[2]
	data["explanation"] = row[3]
	data["options"] = []
	data["type"] = "question"
	return data

def serialize_pool(row):
	data = {}
	data["type"] = "pool"
	data["random_show"] = row[1]
	data["children"] = []
	return data

def serialize_group(row):
	data = {}
	data["type"] = "group"
	data["random_show"] = row[1]
	data["children"] = None
	return data

def serialize_text_block(row):
	data = {}
	data["text"] = row[0]
	return data

def serialize_option(row):
	data = {}
	if row[0] == "":
		data["option"] = row[1]
		data["answer"] = False
	else:
		data["option"] = row[1]
		data["answer"] = True
	return data


def linearize(question):

	for item in question:

		# print(item)

		if item :
			if item["type"] == "group" or item["type"] == "pool":
				if len(item["children"]) > 0:
					linearize(item["children"])
			else:
				linear_question.append(item)
with open('12287324.csv', newline='', encoding="utf8") as csvfile:
	spamreader = csv.reader(csvfile)
	question = None
	pools = []
	groups = []
	callstack = []
	for row in spamreader:
		if detect_type(row=row) == "question":
			if question:
				if len(callstack) > 0:
					if callstack[-1] == "pool":
						pools[-1].children.append(question)
					else:
						groups[-1].children.append(question)
				else:
					qs.append(question)
			s = serialize_question(row)
			question = s
		elif detect_type(row) == "pool":
			if question:
				if len(callstack) > 0:
					if callstack[-1] == "pool":
						pools[-1].children.append(question)
					else:
						groups[-1].children.append(question)
				else:
					qs.append(question)
				question = None
			s = serialize_pool(row)
			newPool = Pool(row=row)
			if len(callstack) > 0:
				if callstack[-1] == "pool":
					raise Exception("Pool cann't inside Pool")
				else:
					groups[-1].children.append(newPool)
					pools.append(newPool)
			else:
				qs.append(newPool)
				pools.append(newPool)

			
			callstack.append("pool")
		

		elif detect_type(row=row) == "group":
			if question:
				if len(callstack) > 0:
					if callstack[-1] == "pool":
						pools[-1].children.append(question)
					else:
						groups[-1].children.append(question)
				else:
					qs.append(question)
				question = None
			s = serialize_pool(row)
			newGroup = Group(row=row)
			if len(callstack) > 0:
				if len(callstack) <= 2:
					if callstack[-1] == "pool":
						pools[-1].children.append(newGroup)
					else:
						groups[-1].children.append(newGroup)
					groups.append(newGroup)
			else:
				qs.append(newGroup)
				groups.append(newGroup)
			
			callstack.append("group")
		elif detect_type(row) == "option":
			question["options"].append(serialize_option(row))

		elif detect_type(row=row) == "end":
			if question:
				if len(callstack) > 0:
					if callstack[-1] == "pool":
						pools[-1].children.append(question)
					else:
						groups[-1].children.append(question)
				else:
					qs.append(question)
			question = None
			# print(callstack)
			# print(pools)
			# print(groups)
			if len(callstack) > 0:
				cs = callstack.pop()


				# print(cs)

				# print()
				if cs == "pool":
					p = pools.pop()
					# print(p)
				else:
					g = groups.pop()
					# print(g)
	# print(addinlist(None))




	qs.append(question)
	# print(qs)












	def serialize(a):

		try:
			if a.type == "group" or a.type == "pool":
				return a.serialize()
		except:
			return a


	


	
	# print(json.dumps(list(map(serialize, qs))))






	linearize(list(map(serialize, qs)))

	print(json.dumps(linear_question))