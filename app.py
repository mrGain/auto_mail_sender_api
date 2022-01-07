from flask import Flask,request ,jsonify, render_template
from flask_pymongo import PyMongo
import datetime

# from flask_mail import Message,Mail

app = Flask(__name__)

from conf import *

mongo = PyMongo(app)
mail = Mail(app)

def fromDate(from_date_string): 
    try:
        return datetime.datetime.strptime(from_date_string, "%Y,%m,%d")
    except ValueError:
        raise ValueError('{} Date is not valid date in the format YYYY,MM,DD'.format(from_date_string))
def toDate(to_date_string): 
    try:
        # return datetime.datetime.strptime(to_date_string, "%Y-%m-%d").date()
        return datetime.datetime.strptime(to_date_string, "%Y,%m,%d")
    except ValueError:
        raise ValueError('Date is not valid date in the format YYYY,MM,DD')

output = []
@app.route('/query/date/',methods=['GET'])
def get_query():
    from_date = fromDate(request.args.get('from'))
    to_date = toDate(request.args.get('to'))
    
    # from_dt : 2016,10,4   
    # to_dt : 2021,10,11
    result = mongo.db.pull_request_log.aggregate([
        { "$match":{"created_date":{"$gte":from_date,"$lt":to_date}}}, 
        {"$group":{"_id":{"$dateToString":{"format":"%Y-%m-%d","date":"$created_date"}},"count":{"$sum":1}}},
        {"$sort":{"created_date":-1}}
        ])
      
    
    flag = 1
    for i in result:
        i['slno']=flag
        output.append(i)  
        flag = flag+1 

    #Sending mail to the mail address.
    subject = get_mail['subject']
    sender = get_mail['sender']
    to = get_mail['recipient']
    msg = Message(subject=subject,sender=sender,recipients=[to])
    msg.html = render_template('index.html',datas=output,sending_mail=True)
    mail.send(msg)    

    return render_template('index.html',datas=output)


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")    