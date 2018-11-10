from flask import Flask, jsonify

app = Flask(__name__)

#set Configuration
app.config.from_object('project.config.DevelopmentConfig')


@app.route('/users/ping', methods=['GET'])
def ping_pong():
    return jsonify ({
        'status':'success',
        'message': 'pong!'
    })
