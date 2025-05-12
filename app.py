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

# tested
# getlist() returns a list, access only first value
@app.route('/create/',methods = ['POST',])
def createUser():
    un = request.args.getlist('user_name')[0]
    uw = int(request.args.getlist('weight')[0])
    
    print(un,uw)
    out = insertUser(un,uw)
    return jsonify({'message': 'k'}), 202

# tested
@app.route('/log-setting/',methods = ['PUT'])
def setWeight():
    usernumber =request.args.getlist('user_no')[0]
    w = request.args.getlist('weight')[0]
    insertWeight(usernumber,w)
    outData = loadUserWeights(usernumber)
    return jsonify({'message': outData}), 202
        
# tested    
@app.route('/log-setting/',methods = ['GET'])
def getExercise():
    m = request.args.getlist('muscle_group')[0]
    e = request.args.getlist('equipment')[0]
    et = request.args.getlist('ex_type')[0]
    l = request.args.getlist('level')[0]
    outExercise = loadExercise(l,et,e,m)
    return jsonify({'message': outExercise}), 202

    

# tested
@app.route('/stats/weight/')
def showPastWeights(): 
    un = request.args.getlist('user_no')[0]
    out = loadUserWeights(un)

    return jsonify({'message': out}), 202

# assumed correct
@app.route('/stats/past-lessons')
def showPastLessons(usernumber): 
    # out = loadLessons(usernumber)
    return jsonify({'message': out}), 202


# tested
def loadUserWeights(user_no):
    cur.execute(
        "SELECT weight_pounds,date_taken from weight join (user) on user.user_no = ? and weight.user_no = ? ",
        (user_no,user_no))
    return [i for i in cur]
    
def loadExercise(level,ex_type,equipment,muscle_group):
    cur.execute(
        "select ex_title,ex_desc from exercise where level like ? and ex_type like ? and equipment like ? and muscle_group like ? ",
        (level,ex_type,equipment,muscle_group))
    print(cur._data)
    return [i for i in cur]

def findUser(user_name):
    cur.execute("select * from user where user.user_name=?",
                (user_name,))
    return [i for i in cur]

def insertUser(user_name,weight):
    cur.execute("insert into user (user_name,weight,from_date) values (?,?,current_date)  ",
            (user_name,weight) )
    
def insertWeight(user_no,weight):
    cur.execute("insert into weight (user_no,weight_pounds,date_taken) values (?,?,current_date)",
    (user_no,weight))    
def insertExercise(ex_title,ex_desc,ex_type,muscle_group,equipment,rating,rating_desc):
    cur.execute("insert into exercise (ex_title,ex_desc,ex_type,muscle_group,equipment,rating,rating_desc) values (?,?,?,?,?,?,?) ",
                (ex_title,ex_desc,ex_type,muscle_group,equipment,rating,rating_desc))


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