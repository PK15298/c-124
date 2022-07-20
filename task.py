from flask import Flask,jsonify,request

app = Flask(__name__)
allTask=[
    {
        'id':1,
        'title':u'brush my teeth',
        'description':u'to brush for 2 min',
        'done': False
    },

     {
        'id':2,
        'title':u'get refreshed',
        'description':u'have bath and eat',
        'done': False
    }
]

@app.route('/display')
def displayTask():
    return jsonify({
        'data': allTask
    })

@app.route('/input',methods=['POST'])

def inputTask():
    if not request.json:
        return jsonify({
            'status':'error',
            'message':'please provide the data'  
            
                  },400)
    task = {
        'id':allTask[-1]['id']+1,
        'title':request.json['title'],
        'description':request.json['description', ''],
        'done': False  
    }
    allTask.append(task)

    return jsonify({
            'status':'success',
            'message':'task added successfully'  
            
                  })

if(__name__=='__main__'):
    app.run(debug=True)

