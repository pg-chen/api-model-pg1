from flask import Flask, request, jsonify, render_template, url_for
from flask_cors import CORS
import numpy as np
import app.preprocessing as pre
import app.regression_model as reg
import app.ann_model as ann
import app.RF_model as rf

app = Flask(__name__, template_folder='../templates')
CORS(app)

@app.route("/")
def page():
    return render_template('page.html')

@app.route("/predict", methods=["POST"])
def postInput():
    #取得前端輸入的數值
    x1 = request.values['District']
    x2 = request.values["Object"]
    x3 = request.values["Structure"]
    x4 = request.values["Floor"]
    x5 = request.values["Building_Height"]
    x6 = request.values["Square"]
    x7_list = request.form.getlist('my_checkbox')
    x7 = len(x7_list)
    x8 = request.values["lat"]
    x9 = request.values["lnt"]
    rent_data = [int(x1),int(x2),int(x3),int(x4),int(x5),float(x6),int(x7),float(x8),float(x9)]

    result1 = reg.predict(rent_data)
    result2 = ann.predict(rent_data)
    result3 = rf.predict(rent_data)
    result = (float(result1) + float(result2)) * 0.3 + float(result3) * 0.4

    # return jsonify({"return" : str(result)})
    print(rent_data,result1,result2,result3) 
    return render_template('submit.html',**locals())

if __name__ == "__main__":
    from waitress import serve
    app.run(host="0.0.0.0", port=3000, debug=True)