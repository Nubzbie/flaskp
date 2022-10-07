from flask import Flask,request

import requests

app = Flask(__name__)

@app.route("/v1/sendMessage",methods=["POST","GET"])

def api():

    try:

      if request.method == "POST":

         jid = request.form["jid"]

         text = request.form["text"]

         return requests.post("https://anandabotv.nubzbie.repl.co/api/v1/sendMessage",data={"jid":jid,"text":text}).text

      else:

         jid = request.args.get("jid")

         text = request.args.get("text")

         return requests.post("https://anandabotv.nubzbie.repl.co/api/v1/sendMessage",data={"jid":jid,"text":text}).text

    except:

         return "Invalid API"

if __name__ == "__main__":

   app.run(debug=True)
