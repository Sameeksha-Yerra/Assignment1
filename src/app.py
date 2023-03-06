from flask import Flask, request, jsonify, abort
from storageutils import MySQLManager
from config import CONFIG


app = Flask(__name__)
@app.route('/api/fitness', methods=['GET', 'POST'])

def myfitnessdatabase():
    if request.method=='GET':
        return "Im Alive"
    else:
        return jsonify({})
    
if __name__ == '__main__':
    app.run("0.0.0.0", port=9999)