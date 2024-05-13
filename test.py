data=[
{
"text": '2dfg',
"row": 1,
"column": "1",
"headers":"abc"
},
{
"text": '2ddfgfg',
"row": 1,
"column": "3",
"headers":"def"
}
]


def insert_documents(data):
    temp_data_list=[]
    for temp_data in data:
        temp_data_list[[(temp_data["row"])]+[int(temp_data["column"])]]=temp_data["text"]


    return temp_data_list

def write_to_file():
    




        