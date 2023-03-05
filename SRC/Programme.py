from pathlib import Path
from tkinter import Label, StringVar,Tk,Canvas,Text,Button,PhotoImage
from tkinter.constants import END,WORD
from Perceptron import Neurone

#chemin d'accès aux assets
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.title("TP1 PERCEPTRON")
width = 600 
height = 300
 
screen_width = window.winfo_screenwidth()  
screen_height = window.winfo_screenheight() 

x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
 
window.geometry('%dx%d+%d+%d' % (width, height, x, y))
window.resizable(False, False)
window.config(cursor="dot")

result=StringVar()
result.set("------")

perceptron=Neurone(3,[1,-1,-1,2])#notre perceptron


def analyser():
    ok=False
    motif=[]
    motif_str=(entry.get(0.0,END))
    try:
        for i in range(0,4):
            motif.append(int(motif_str[i]))
        if(len(motif_str)>5):
            raise BaseException
        ok=True
    except:
        result.set('Entrer un bon motif')
        ok=False
    if ok:
        d=0
        if(motif==[1,0,0,1]):
            d=1
        if(perceptron.apprendre(motif,d)):
            result.set('J\'ai eu: '+str(d)+' et vous attendez: '+str(d)+'\n alors j\'ai eu juste' )
        else:
            result.set('je me suis trompé')
            
#arrière plan
canvas = Canvas(
    window,
    bg="#004c7f",
    height=300,
    width=600,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)
canvas.place(x = 0, y = 0)

bg_image = PhotoImage(
    file=relative_to_assets("bg.png"))
bg = canvas.create_image(
    300,
    150,
    image=bg_image
    )


entry = Text(
    canvas,
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    font=("sergio",10,"bold"),
    wrap=WORD,
    cursor="dot",

)
entry.place(
    x=250,
    y=90,
    width=90,
    height=20
)

button_image = PhotoImage(
    file=relative_to_assets("btn.png"))
button_1 = Button(
    canvas,
    command=analyser,
    image=button_image,
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    activebackground="#004C7F",
    bg="#004C7F"
)
button_1.place(
    x=260,
    y=130,
    width=69,
    height=26
)

resultat=Label(
    canvas,
    textvariable=result,
    fg="red",
    bg="white",
    font=('sergio',13,'bold')
)
resultat.place(
        x=150,
        y=220,
        width=300
)

window.mainloop()
