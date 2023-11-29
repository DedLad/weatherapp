import requests
from flask import Flask,request,render_template
import SECRETS

app =Flask(__name__)
@app.route('/',methods=["POST","GET"])
def test():
    if request.method == "POST":
        code = request.form.get("code")
        key= SECRETS.x
        r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={code}&appid={key}")
        
        class vars:
            s = r.json()['main']
            temp = s['temp']
            min = s['temp_min']
            max = s['temp_max']
            hum = s['humidity']
        print(r.json())
        # return r.json()#,str(temp)
        return render_template('dump.html',vars=vars)#temp=temp,min=min,max=max,hum=hum)
    return render_template('base.html')

if __name__ == '__main__':
       app.run(debug='true')
       
