from flask import Flask,jsonify,request
import mariadb
app = Flask(__name__)
items = []
try:
    conn = mariadb.connect(
            host='127.0.0.1',
            port= 3306,
            user='root',
            password='password',
            database='exercise')
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)
cur = conn.cursor()


@app.route('/login/<string:username>')
def login(username):
    out = findUser(username)
    return jsonify({'message': out}), 202

@app.route('/create/',methods = ['POST',])
def createUser():
    userinfo = request.args.getlist('user_name')
    userinfo = request.args.getlist('preference')
    
    print(userinfo)
    #out = insertUser(un,pn,ln,w)
    return jsonify({'message': 'k'}), 202





def loadUserWeights(user_no):
    cur.execute(
        "SELECT weight_pounds,date_taken from weight join (user) on user.? = weight.? ",
        (user_no,user_no))
    
def loadAllExercise(level,ex_type,equipment,muscle_group):
    cur.execute(
        "select ex_title,ex_desc from exercise where level like ? and ex_type like ? and equipment like ? and muscle_group like ? ",
        (level,ex_type,equipment,muscle_group))

def findUser(user_name):
    cur.execute("select * from user where user.user_name=?",
                (user_name,))
    
    return [i for i in cur]
def insertUser(user_name,weight):
    cur.execute("insert into user (user_name,lessons_completed,weight,from_date) values (?,?,?,0,?,current_date)  ",
            (user_name,weight) )
def insertExercise(ex_title,ex_desc,ex_type,muscle_group,equipment,rating,rating_desc):
    cur.execute("insert into exercise (ex_title,ex_desc,ex_type,muscle_group,equipment,rating,rating_desc) values (?,?,?,?,?,?,?) ",
                (ex_title,ex_desc,ex_type,muscle_group,equipment,rating,rating_desc))

def insertWeight(user_no,weight_pounds,date_taken):
    cur.execute("INSERT INTO weight  (user_no,weight_pounds,date_taken) VALUES (?,?,?) ",
                (user_no,weight_pounds,date_taken))

def deleteUSer(user_no):
    cur.execute("delete from user where user.user_no =? ",
                (user_no))
def deleteExercise(ex_no):
    cur.execute("delete from exercise where exercise.ex_no =? ",
                (ex_no))
def showMuscle():
    cur.execute("show columns from muscle_group ")
def showExTypes():
    cur.execute("show columns from ex_type")
def showLevels():
    cur.execute("select level distinct from exercise")
def showEquip():
    cur.execute("select * ex_type_name from ex_type ")



if __name__ == "__main__":
    app.run()