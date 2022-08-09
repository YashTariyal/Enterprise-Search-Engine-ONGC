from random import random, randrange
from urllib import response
from flask import Flask, request, jsonify, render_template
import requests
import os
import json

HOST = 'localhost'
app = Flask(__name__)


@app.route('/', methods=["GET","POST"])
def get_index():
    q=request.args.get('q')
    print(q)
    if q is not None:
        query={
          "query": {
    "bool": {
      "must": [],
      "filter": [
        {
          "multi_match": {
            "query": q
          }
        }  
      ]
    }
  }
}
       # print(query)
        #resp=requests.get('http://localhost:9200/first/_search',json=query)
        #data=resp.json()
        #print(data)
        #print("**************************************************************************************")
        #nm=data["hits"]["hits"][randrange(0,5)]["_source"]["title"]
        #catg=data["hits"]["hits"][randrange(0,5)]["_source"]["rating"]
        #camp=data["hits"]["hits"][randrange(0,5)]["_source"]["release year"]
        #course=data["hits"]["hits"][randrange(0,5)]["_source"]["user rating score"]
        #dept=data["hits"]["hits"][randrange(0,5)]["_source"]["user rating size"]
        #dept1=data["hits"]["hits"][randrange(0,5)]["_source"]["ratingLevel"]
        #nm1=data["hits"]["hits"][randrange(0,5)]["_source"]["title"]
        #catg1=data["hits"]["hits"][randrange(0,5)]["_source"]["rating"]
        #camp1=data["hits"]["hits"][randrange(0,5)]["_source"]["release year"]
        #course1=data["hits"]["hits"][randrange(0,5)]["_source"]["user rating score"]
        #dept2=data["hits"]["hits"][randrange(0,5)]["_source"]["user rating size"]
        #dept3=data["hits"]["hits"][randrange(0,5)]["_source"]["ratingLevel"]
        return render_template('index (2).html',q=q)
    return render_template('index (2).html')


if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 8080))
    app.run(host='localhost', port=port, debug=True)