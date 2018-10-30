from flask import *
import pandas as pd
import pandas.io.sql
import pyodbc

app = Flask(__name__)

@app.route("/tables")
def show_tables():
	server = 'p-lda-sqldb.cjppsdhni2np.us-west-2.rds.amazonaws.com,7899'
	db = 'legal_db'
	username = 'legal_srv'
	password = 'Opportunity1'
	conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + db + ';UID=' + username + ';PWD=' + password)

	sql = """
	SELECT top 1000 *
	FROM dbo.lamp_pos


	"""

	df = pandas.io.sql.read_sql(sql, conn)

	return render_template('view.html', tables=[df.to_html()], 
	titles = ['Products'])

if __name__ == "__main__":
    app.run(debug=True)