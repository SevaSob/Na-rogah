from app import app
from app import db
from app.models import booking
from flask import jsonify, request

@app.route('/get_booking', methods=['GET'])
def get_booking():
    date = request.args.get('date')
    idTable = request.args.get('idTable')

    phone = ['','','','','','','','']

    users = booking.query.all()
    for u in users:
        if u.date == date and u.table == int(idTable):
            for h in range(8):
                if (u.hour_start <= 12+h) and (12+h <= u.hour_end):
                    phone[h] = u.phone

    return jsonify({
            "schedule":{
                "table_id": idTable,
                "date": date,
                "hours":[
                {
                    "hour": "12:00",
                    "customerPhone": phone[0]
                },
                {
                    "hour": "13:00",
                    "customerPhone": phone[1]
                },
                {
                    "hour": "14:00",
                    "customerPhone": phone[2]
                },
                {
                    "hour": "15:00",
                    "customerPhone": phone[3]
                },
                {
                    "hour": "16:00",
                    "customerPhone": phone[4]
                },
                {
                    "hour": "17:00",
                    "customerPhone": phone[5]
                },
                {
                    "hour": "18:00",
                    "customerPhone": phone[6]
                },
                {
                    "hour": "19:00",
                    "customerPhone": phone[7]
                }
                ]
            }
        })

@app.route('/post_new_booking', methods=['POST'])
def post_new_booking():
    date = request.json['date']
    table = request.json['table_id']
    name = request.json['name']
    comment = request.json['comment']
    phone = request.json['phone']
    hours_start = request.json['hours_start']
    hours_end = request.json['hours_end']

    u = booking(table=table, name=name, phone=phone, info=comment, date=date, hour_start=hours_start, hour_end=hours_end)
    db.session.add(u)
    db.session.commit()

    return jsonify({"status": "OK"})