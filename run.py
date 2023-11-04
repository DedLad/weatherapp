import requests
# import flask
from flask import Flask,request,render_template
# from flask import Flask, render_template
# from flask_googlemaps import GoogleMaps
# from flask_googlemaps import Map, icons
app =Flask(__name__)
# GoogleMaps(app, key="my-key")



@app.route('/',methods=["POST","GET"])
def test():
    if request.method == "POST":
           # getting input with name = fname in HTML form
        code = request.form.get("code")
        key='{ENTER YOUR KEY}'
        r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={code}&appid={key}")

       # getting input with name = lname in HTML form 
        # last_name = request.form.get("lname") 
        return r.json()
    return render_template('base.html')



'''@app.route('/enter',methods=["POST","GET"])
def code():
    global code


    return render_template('base.html')'''
'''
@app.route('/weather',methods=["POST","GET"])
def weather():
    def code():
        global code
        if request.method=="POST":
            return code  
    # return     

    return render_template('base.html'),rtr()  
def rtr():
    key='c5eeda8ddd78b413ae75c09e1e0cca7b'
    # q= str(input('enter location in form City,country '))
    r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={code}&appid={key}")
    return r.json()'''
     
if __name__ == '__main__':
       app.run(debug='true')
       
