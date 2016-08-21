import web
import shelve
from Sentence import *
from gothonweb import map

urls = (
"/game", "GameEngine",
"/","Login",
"/LoginSuccess","LoginSuccess",
"/score","Score"
)

app = web.application(urls, globals())

#little hack go that debug mode works with sessions

if web.config.get("_session") is None:
	store = web.session.DiskStore("sessions")
	session = web.session.Session(app, store, initializer = {"room":None,"count":0,"username":""})
	web.config._session = session
else:
	session = web.config._session

render = web.template.render("templates/", base = "layout")

class Score(object):
	def GET(self):
		try:
			scorefile = shelve.open("scores/scorefile.dat")
			score_num = scorefile[session.username]
			scorefile.close()
			return render.score_found(username = session.username, score_num = score_num[session.username])
		except KeyError:
			return render.none_score_found(username = session.username)

class Login(object):
	def GET(self):
		return render.login()

	def POST(self):
		login_infor = web.input(username="Nobody",password="Nobody")
		# unicode string to python utf-8 string
		username = login_infor.username.encode("utf-8")
		password = login_infor.password.encode("utf-8") 

		if username == "" or password == "":
		   return render.please_input(username = username, password = password)	
		else:
			try:
				loginfile = shelve.open("logins/loginfile.dat")	
				new_login = {}			
				new_login = loginfile[username]
				if new_login[username] == password:
					session.room = map.START
					session.username = username
					web.seeother("/LoginSuccess")				
				else:
					return render.please_input(username = username, password = password)
			except KeyError:
				session.username = username
				loginfile[username] = {username:password}
				session.room = map.START
				web.seeother("LoginSuccess")
			finally:
				loginfile.close()

class LoginSuccess(object):
	def GET(self):
		return render.corridor_page()
	def POST(self):
		pass

class GameEngine(object):
	def GET(self):
		if session.room:
			if session.room.name != "death":
				session.count += 1
				return render.show_room(room=session.room)
			else:
				session.count += 1
				scorefile = shelve.open("scores/scorefile.dat")
				scorefile[session.username] = {session.username:session.count}
				session.kill()
				scorefile.close()
				return render.show_room(room=session.room)
								
		else:
			# why is there here? do you need it?
			scorefile = shelve.open("scores/scorefile.dat")
			scorefile[session.username] = {session.username:session.count}
			session.kill()
			scorefile.close()
			return render.you_died()

	def POST(self):
		form = web.input(action=None)
		
		# there is a bug here, can you fix it?
		if session.room and form.action:
			word_list = lexicon_1.scan_1(form.action)
			sentence = parse_sentence(word_list)
			recognized_action = (sentence.subject + " " + sentence.verb + " " + sentence.object)
			session.room = session.room.go(recognized_action)

		web.seeother("/game")
		
if __name__ == "__main__":
		app.run()
