from flask import *
import json
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/view")
def view():
    con = sqlite3.connect("pizza.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from Pizzak")
    rows = cur.fetchall()
    return json.dumps([dict(ix) for ix in rows])

@app.route("/savedetails/", methods=["POST"])
def saveDetails():
    msg = "msg"
    try:
        data = request.get_json(force=True)
        print(data)
        nev = data["nev"]
        leiras = data["leiras"]
        meret = data["meret"]
        ar = data["ar"]
        with sqlite3.connect("pizza.db") as con:
            cur = con.cursor()
            cur.execute("INSERT into Pizzak (nev, leiras, meret, ar) values (?,?,?,?)", (nev, leiras, meret, ar))
            con.commit()
            msg = "Pizza successfully Added"
    except:
        con.rollback()
        msg = "We can not add the pizza to the list"
    finally:
        return nev
        con.close()

@app.route("/deleterecord/", methods=["POST"])
def deleterecord():
    data = request.get_json(force=True)
    id = str(data["id"])
    print(id)
    with sqlite3.connect("pizza.db") as con:
        try:
            cur = con.cursor()
            cur.execute("delete from Pizzak where id = ?", id)
            msg = "record successfully deleted"
        except:
            msg = "can't be deleted"

@app.route("/updatedetails/", methods=["POST"])
def updaterecord():
    try:
        data = request.get_json(force=True)
        print(data)
        id = data["id"]
        nev = data["nev"]
        leiras = data["leiras"]
        meret = data["meret"]
        ar = data["ar"]

        with sqlite3.connect("pizza.db") as con:
            cur = con.cursor()
            cur.execute("UPDATE Pizzak SET nev=?, leiras=?, meret=?, ar=? WHERE id=?", (nev, leiras, meret, ar, id))
            con.commit()
            msg = "Employee successfully Updated"
    except:
        con.rollback()
        msg = "We can not update the employee to the list"
    finally:
        return msg
        con.close()

if __name__ == "__main__":
    app.run(debug=True)