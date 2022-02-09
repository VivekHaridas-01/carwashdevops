import producer
from confluent_kafka import KafkaException
from flask import Flask, request, render_template
from werkzeug.exceptions import HTTPException
from requests.exceptions import HTTPError
from datetime import datetime
import subprocess as sp

app = Flask(__name__)
my_producer = producer.kafkaProducer()


@app.route('/washStatus', methods=['POST'])
def washStatus():
    try:
        data = request.json
        now = datetime.now()
        data["Date and Time"] = now.strftime("%B %d, %Y %H:%M:%S")
        my_producer.send_msg_async(data)
        return f'Callback URL : {data["callback"]}', 200
    except HTTPError as http_err:
        return f'HTTP error occurred: {http_err}', 400
    except Exception as err:
        return f'Other error occurred: {err}', 500
    except KafkaException as ex:
        raise HTTPException(status_code=500, detail=ex.args[0].str())


@app.route('/washStatus/callbackURL<string:number>')
def callback(number):
    return f"Output of module {number} to be added later (Status of Module)", 200


@app.route('/ui', methods=['GET'])
def ui():
    out = sp.run(["php", "templates\index.php"], stdout=sp.PIPE)
    return out.stdout


if __name__ == '__main__':
    app.run(debug=True)
