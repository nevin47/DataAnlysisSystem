import web

render = web.template.render('templates/')
db = web.database(dbn='mysql', user='root', pw='123', db='test')

urls = (
  '/', 'index',
  '/add', 'add'
)
def DBsearch():
        users = db.query("select * from test")
        for user in users:
            print user.ID,user.Name,user.Age

class index:
    def GET(self):
        test = db.select('test')
        return render.index(test)

class add:
    def POST(self):
        print "IN!"
        i = web.input()
        n = db.insert('test', Name=str(i.Name), Age=int(i.Age))
        raise web.seeother('/')

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()