import json
stud={"Prn":101,"Email id":["uday@gmail.com","wipro@gmail.com"],"contact no.":[88759,966875]}
with open("wipro.json","w") as fw:
    json.dump(stud,fw)
with open("wipro.json","r") as fr:
    data=json.load(fr)
    for k,v in data.items():
        print(k,v)