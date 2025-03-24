import cherrypy, os, os.path
from mako.template import Template
from mako.lookup import TemplateLookup
from configDB import dbConnect
from OtherCommand import visualRemboursement,PrintRemboursement,visualRemboursementtoString,InsertRemboursement,removeRemboursement
mylookup = TemplateLookup(directories=['res/templates'], input_encoding='utf-8', module_directory='res/tmp/mako_modules')

class InterfaceWebRemboursement(object):    
    ###### Page d'accueil #############
    @cherrypy.expose
    def index(self):
        mytemplate = mylookup.get_template("index.html")
        return mytemplate.render()

    ###### Pages d'affichages ###########               
    @cherrypy.expose
    def affRemboursement(self):
        Remboursement = PrintRemboursement()
        return self.render_aff_index(Remboursement)
    def render_aff_index(self, Remboursement):
        mytemplate = mylookup.get_template("aff_index.html")
        return mytemplate.render(Remboursement=Remboursement)
    @cherrypy.expose
    def insertPage(self):        
        mytemplate = mylookup.get_template("insert.html")        
        return mytemplate.render(message="Veuillez remplir tous les champs", type="info")

    @cherrypy.expose
    def insertDone(self, numticket=None, date=None, prixnuit=None, premierrepas=None, deuxiemerepas=None, prixplein=None, prixpeage=None):
        # le test suivant est rendu inutile par l'utilisation de javascript dans formulaire bootstrap
        if numticket and date and prixnuit and premierrepas and deuxiemerepas and prixplein and prixpeage:
            print(date, " -:- ", type(date))
            try:
                InsertRemboursement(numticket, date, prixnuit, premierrepas, deuxiemerepas, prixplein, prixpeage)
                message = "Insertion réussie !"
                typ = "success"
            except (Exception) as e:
                message = str(e)
                typ = "danger"
        else:
            message = "Tous les champs doivent être remplis !!"
            typ = "warning"
        mytemplate = mylookup.get_template("insert.html")        
        return mytemplate.render(message=message, type=typ)
    
    ###### Pages de suppression ###########        
    
    @cherrypy.expose
    def suppressByNumTicket(self, numticket=None):
        # Pas de javascript dans formulaire bootstrap !
        if numticket :
            try:
                removeRemboursement(numticket)
                message = "Suppression réussie !"
                typ = "success"
            except ValueError as e:
                message = str(e)
                typ = "danger"
        else:
            message = "Veuillez remplir tous les champs."
            typ = "warning"
        mytemplate = mylookup.get_template("supp_RemboursementByNumTicket.html")        
        return mytemplate.render(message=message, type=typ)

if __name__ == '__main__':
    rootPath = os.path.abspath(os.getcwd())
    print(f"la racine du site est :\n\t{rootPath}\n\tcontient : {os.listdir()}")
    cherrypy.quickstart(InterfaceWebRemboursement(), '/', 'config.txt')
