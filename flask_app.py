from flask import Flask,request,jsonify

app=Flask(__name__)

contacts=[]

@app.route('/add-data',methods=['POST'])

def add_contact():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide data"
        })

    id=0

    if len(contacts)==0:
        id=1
    else:
        id=contacts[-1]['id']+1

    contact={
         
        'id':id,
        'Name':request.json['Name'],
        'Contact':request.json.get('Contact',""),
        'done':False
    }

    contacts.append(contact)
    return jsonify({
        "status":"success",
        "message":"contact added successfully"
    })    

@app.route('/show-data')

def show_contact():
    return jsonify({
        "data":contacts
    })

app.run()