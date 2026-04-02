# First, create a dictionary that consists of - id, name, class and subject integration of students. Then, write a program to retrieve unique entries and eliminate the rest.
student_data={
    "id1":{"name":"Aryan","class":9,"subject_integration":"Math"},
    "id2":{"name":"John","class":10,"subject_integration":"Science"},
    "id3":{"name":"Aryan","class":9,"subject_integration":"Math"},
    "id4":{"name":'Emma',"class":8,"subject_integration":'English'}}

seen_keys=[]
result={}

for i,j in student_data.items():
    unique_key=(j["name"],j["class"],j["subject_integration"])

    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[i]=j
for x,y in result.items():
    print(x,":",y)

    