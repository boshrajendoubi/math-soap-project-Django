try:
    from suds.client import Client
except ImportError :
    print("suds-py3 is not found ")

maths_client=Client('http://127.0.0.1:8000/maths/?wsdl')

from tkinter import *



class MyApp:

    def __init__(self):
        self.window = Tk()
        self.window.title("Maths Application")
        self.window.geometry("720x480")
        self.window.minsize(480, 360)
        #self.window.iconbitmap("logo.ico")
        self.window.config(background='#296172')

        # initialization des composants
        self.frame = Frame(self.window, bg='#296172')

        # creation des composants
        self.create_widgets()

        # empaquetage
        self.frame.pack(expand=YES)

    def create_widgets(self):
        self.create_title()
        self.create_subtitle()
        if(self.create_min()):
            self.resultat_min()
        if(self.create_cos()):
            self.resultat_cos()
        if(self.create_sin()):
         self.resultat_sin()
        if(self.create_max()):
            self.resultat_max
         
        
        
        
       

    def create_title(self):
        label_title = Label(self.frame, text="Bienvenue sur l'application", font=("Courrier", 40), bg='#296172',
                            fg='white')
        label_title.pack()
    
    
    def create_subtitle(self):
        label_subtitle = Label(self.frame, text="Clicker sur l'un des boutons ", font=("Courrier", 15), bg='#296172',
                               fg='white')
        label_subtitle.pack()
    
   #------------------------------------------sin--------------------------------------------------
        
    def create_sin(self):
        yt_button = Button(self.frame, text="Fonction SIN", font=("Courrier", 12), bg='white', fg='#F21365',
                           command=self.fctsin)
        yt_button.pack(pady=25, fill=X)
    
    def create_angle(self):
        global user_Entry 
        user_Entry= Entry(self.frame,bg="white")
        user= Label(self.frame, text = "Entrer l'angle ",font=("Courrier", 12), bg='#296172', fg='white')
        user.pack(pady=10)
        user_Entry.pack(pady=25) 
    
    def afficher_resultat_sin(self):
        res=maths_client.service.sin(user_Entry.get())
        useraff = Label(self.frame, text = "Résultat du sinus",font=("Courrier", 12), bg='#296172', fg='white')
        useraff['text']="le résultat: "+ str(res)
        useraff.pack(pady=10)
    
    
    def resultat_sin(self):
         yt_button = Button(self.frame, text="Résultat", font=("Courrier", 12), bg='white', fg='#F21365',
                           command=self.afficher_resultat_sin)
         yt_button.pack(pady=25, fill=X)
    
    
    
    
        
    def fctsin(self):
        self.create_angle()
        self.resultat_sin()
        
   #----------------------------------------------cos--------------------------------------------------
      
    def create_cos(self):
        yt_button = Button(self.frame, text="Fonction COS", font=("Courrier", 12), bg='white', fg='#F21365',
                           command=self.fctcos)
        yt_button.pack(pady=25, fill=X)
    
    def create_angle(self):
        global user_Entry 
        user_Entry= Entry(self.frame,bg="white")
        user= Label(self.frame, text = "Entrer l'angle ",font=("Courrier", 12), bg='#296172', fg='white')
        user.pack(pady=10)
        user_Entry.pack(pady=25) 
    
    def afficher_resultat_cos(self):
        res=maths_client.service.cos(user_Entry.get())
        useraff = Label(self.frame, text = "Résultat du cosinus",font=("Courrier", 12), bg='#296172', fg='white')
        useraff['text']="le résultat: "+ str(res)
        useraff.pack(pady=10)
    
    
    def resultat_cos(self):
         yt_button = Button(self.frame, text="Résultat", font=("Courrier", 12), bg='white', fg='#F21365',
                           command=self.afficher_resultat_cos)
         yt_button.pack(pady=25, fill=X)
        
    def fctcos(self):
        self.create_angle()
        self.resultat_cos()
        

#----------------------------------------------Min--------------------------------------------------
      
    def create_min(self):
        yt_button = Button(self.frame, text="Fonction MIN", font=("Courrier", 12), bg='white', fg='#F21365',
                           command=self.fctmin)
        yt_button.pack(pady=10, fill=X)
    
    def create_textbox(self):
        global user_Entry
        global user_Entry1
        user = Label(self.frame, text = "Entrer X ",font=("Courrier", 12), bg='#296172', fg='white')
        user_Entry = Entry(self.frame,bg="white")
        user1 = Label(self.frame, text = "Entrer y ",font=("Courrier", 12), bg='#296172', fg='white')
        user_Entry1 = Entry(self.frame,bg="white")
        user.pack(pady=10)
        user_Entry.pack(pady=25) 
        user1.pack(pady=10)
        user_Entry1.pack(pady=25) 
    
    def afficher_resultat_min(self):
        x=user_Entry.get()
        y=user_Entry1.get()
        res=maths_client.service.min(x,y)
        useraff = Label(self.frame, text = "Le minimum: ",font=("Courrier", 12), bg='#296172', fg='white')
        useraff['text']="le minimum entre "+str(x)+" et "+str(y)+": "+ str(res)
        useraff.pack(pady=10)
    
    
    def resultat_min(self):
         yt_button = Button(self.frame, text="Résultat", font=("Courrier", 12), bg='white', fg='#F21365',
                           command=self.afficher_resultat_min)
         yt_button.pack(pady=25, fill=X)
        
    def fctmin(self):
        self.create_textbox()
        self.resultat_min()
        
    
#----------------------------------------------Max--------------------------------------------------
      
    def create_max(self):
        yt_button = Button(self.frame, text="Fonction MAX", font=("Courrier", 12), bg='white', fg='#F21365',
                           command=self.fctmax)
        yt_button.pack(pady=10, fill=X)
    
    def create_textbox(self):
        global user_Entry
        global user_Entry1
        user = Label(self.frame, text = "Entrer X ",font=("Courrier", 12), bg='#296172', fg='white')
        user_Entry = Entry(self.frame,bg="white")
        user1 = Label(self.frame, text = "Entrer y ",font=("Courrier", 12), bg='#296172', fg='white')
        user_Entry1 = Entry(self.frame,bg="white")
        user.pack(pady=10)
        user_Entry.pack(pady=25) 
        user1.pack(pady=10)
        user_Entry1.pack(pady=25) 
    
    def afficher_resultat_max(self):
        x=user_Entry.get()
        y=user_Entry1.get()
        res=maths_client.service.max(x,y)
        useraff = Label(self.frame, text = "Le maximum: ",font=("Courrier", 12), bg='#296172', fg='white')
        useraff['text']="le maximum entre "+str(x)+" et "+str(y)+": "+ str(res)
        useraff.pack(pady=10)
    
    
    def resultat_max(self):
         yt_button = Button(self.frame, text="Résultat", font=("Courrier", 12), bg='white', fg='#F21365',
                           command=self.afficher_resultat_max)
         yt_button.pack(pady=25, fill=X)
        
    def fctmax(self):
        self.create_textbox()
        self.resultat_max()
    
        
    
   
app = MyApp()
app.window.mainloop()

# afficher
