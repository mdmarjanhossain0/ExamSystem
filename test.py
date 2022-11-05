import csv
qs = []
single_question = None
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
	data["mark"] = row[1]
	data["answer"] = row[2]
	data["explanation"] = row[3]
	data["options"] = []
	data["type"] = "question"
	return data

def serialize_pool(row):
	data = {}
	data["type"] = "pool"
	data["random_show"] = row[1]
	data["children"] = None
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
		data[""] = row[1]
	else:
		data["*"] = row[1]
	return data




def addinlist(data, type, level=0):
	if data == None and type == "end":
		qs.append(structure.pop())

	if type == "pool":
		if len(structure) < 1:
			structure.append(data)
		else:
			lastchildren = None
			def get_last_children_from_list(l):
				try:
					last = l.pop()
					gl = None
					while(last):
						if last["type"] == "pool":
							gl = last
							break
						else:
							last = l.pop()
					return gl
				except:
					return None
			def addinrecursivepool(data):
				if lastchildren and (len(lastchildren["children"]) < 1):
					lastchildren.append(data)
					return
				lastchildren = get_last_children_from_list(l=lastchildren)
				addinrecursivepool(data=data)
			lastchildren = structure[-1]["children"]
			addinrecursivepool(data=data)
			
with open('12283192.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile)
	for row in spamreader:
		question = None
		if detect_type(row=row) == "question":
			if question:
				qs.append(question)
			s = serialize_question(row)
			question = s
		elif detect_type(row) == "pool":
			s = serialize_pool(row)
			print(s)
		elif detect_type(row) == "option":
			question["options"].append(serialize_option(row))
			print(question)
		


		
			
		print(detect_type(row=row))