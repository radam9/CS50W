from libreria import app, db

username = ("user", )
password = "pass123"
db.engine.execute("INSERT INTO users (username, password) VALUES (%s, %s)",("tony","mypassabc"))
db.session.close()
db.engine.execute("INSERT INTO users (username,password) VALUES ('user', 'pass123')")


# sql = "SELECT * FROM users (username) VALUES (%s);"
# r = db.engine.execute(sql, username)
r = db.engine.execute("SELECT * FROM users WHERE username=%s", ("username", ))
print(type(r))
