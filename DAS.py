# coding:utf-8

import web
import systemModel.login as loginModel
import systemModel.subsystemController as subC
import AnalysisModel.AnalysisController as anC

web.config.debug = False
urls = (
    '/', 'index',
    '/login', 'login',
    '/subsystemchoose', 'subsystemchoose',
    '/analysis', 'analysis',
    '/analysisPOST', 'analysisPOST'
)

mainRender = web.template.render('templates/')
analysisRender = web.template.render('templates/analysisTemplates')
db = web.database(dbn='mysql', user='root', pw='123', db='DAS')


# index controller #
class index:
    def GET(self):
        dataget = web.input(loginstatue=None)
        pagesession = web.config._session
        return mainRender.index(pagesession,dataget)


# login controller #
class login:
    def POST(self):
        if loginModel.login(db) == 1:
            raise web.seeother('/subsystemchoose')
        else:
            raise web.seeother('/?loginstatue=wrongpsd')


# subsystem choose controller #
class subsystemchoose:
    def GET(self):
        pagesession = web.config._session
        if pagesession.login != 1:
            raise web.seeother('/')
        else:
            return mainRender.subsystemmenu()


# analysis model controller #
class analysis:
    def GET(self):
        pagesession = web.config._session
        if pagesession.login != 1:
            raise web.seeother('/')
        else:
            dataget = web.input(subsys = None, func = None)
            if dataget.subsys:
                # TODO: The following judgment statement is not necessary, it can be simplified in the future
                # -- nevin47 16_03_02
                if dataget.func and dataget.subsys:
                    return subC.mainController(dataget.subsys, dataget.func)
                else:
                    subsys = web.template.render("templates/analysisTemplates/"+dataget.subsys, base='../base')
                    return subsys.index()
            else:
                return "No input!"

    def POST(self):
        pagesession = web.config._session
        if pagesession.login != 1:
            raise web.seeother('/')
        else:
            dataget = web.input(subsys=None, func=None, apost=None)
            if dataget.subsys and dataget.apost and dataget.func:
                return anC.mainController(dataget)

# analysisPOST #
class analysisPOST:
    def POST(self):
        # TODO: 改类别
        x = web.input(myfile={})
        filedir = '/Users/nevin47/Desktop/Project/Academic/Code/Python/DataAnlysisSystem/DataAnlysisSystem/static/csv' # change this to the directory you want to store the file in.
        #filedir = 'static/csv' # change this to the directory you want to store the file in.
        if 'myfile' in x: # to check if the file-object is created
            DBfilename = str(x.DBfilename) + '.csv'
            filetype = int(x.filetype)
            # For file update
            filepath=x.myfile.filename.replace('\\','/') # replaces the windows-style slashes with linux ones.
            fout = open(filedir +'/'+ DBfilename,'w') # creates the file where the uploaded file should be stored
            fout.write(x.myfile.file.read()) # writes the uploaded file to the newly created file.
            fout.close() # closes the file, upload complete.
            # For DB operate
            db.insert('UBSVMFile', filename=DBfilename, type=filetype)
        raise web.seeother('/analysis?subsys=UBSVM')



app = web.application(urls, globals())
web.config.session_parameters['timeout'] = 1800  # session time out 30min
session = web.session.Session(app, web.session.DiskStore('sessions'))
web.config._session = session

if __name__ == "__main__":
    app.run()