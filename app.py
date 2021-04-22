import tornado.web
import tornado.ioloop
from tornado.web import RequestHandler, Application, url, authenticated
from src.Session import Session
from src.UserTags import UserTags


class BaseHandler(RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")


class MainHandler(BaseHandler):
    def get(self):
        if not self.current_user:
            self.redirect("/login")
            return
        name = tornado.escape.xhtml_escape(self.current_user)
        self.write("Hello, " + name)


class LogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie("user")
        self.redirect("/login")


class LoginHandler(BaseHandler):
    def initialize(self, session):
        self.session = session

    def get(self):
        if not self.current_user:
            self.write('<html><body><form action="/login" method="post">'
                    'Name: <input type="text" name="name">'
                    '<input type="submit" value="Sign in">'
                    '</form></body></html>')
        else:
            self.redirect("/")

    def post(self):
        name = self.get_argument("name")
        self.set_secure_cookie("user", name)
        self.session.login_user(name)
        self.redirect("/")


class TagsHandler(BaseHandler):
    def initialize(self, user_tags):
        self.user_tags = user_tags
    
    def get(self, user_name):
        self.write(self.user_tags.get(user_name))

    def post(self, arg):
        user_id = self.request.path.split("/")[2]
        tag_id = int(self.get_body_argument("tag_id"))
        user_tags.add(user_id, tag_id)

    def delete(self, arg):
        user_name = self.request.path.split("/")[2]
        tag_id = int(self.get_body_argument("tag_id"))
        user_tags.delete(user_name, tag_id)


if __name__ == "__main__":
    session = Session(dict())
    user_tags = UserTags(dict())
    app = Application([
    url(r"/", MainHandler),
    url(r"/login", LoginHandler, dict(session=session)),
    url(r"/logout", LogoutHandler),
    url(r"/users/([a-zA-Z0-9-]+)/tags", TagsHandler, dict(user_tags=user_tags))
    ], cookie_secret="asfhklas2k1l412521j129jj21j2j2gds03kfsdk")

    app.listen(8881)
    print("App listening on port 8881")
    tornado.ioloop.IOLoop.current().start()
