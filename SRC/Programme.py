from pathlib import Path
from tkinter import Label, Scrollbar, StringVar,Tk,Canvas,Text,Button,PhotoImage, Toplevel,ttk,messagebox,Listbox
from tkinter.constants import BOTH, DISABLED,END,INSERT, LEFT,NORMAL, RIGHT,WORD
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

perceptron=Neurone(3,[1,-1,-1,2])


def analyser():
    motif=[]
    motif_str=(entry.get(0.0,END))
    for i in range(0,4):
        try:
            motif.append(int(motif_str[i]))
        except:
            result.set('pour eviter le crash en cas de caractere')
    d=0
    if(motif==[1,0,0,1]):
        d=1
    print(d)
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

label=Label(
    canvas,
    text="Entrez un motif (seuls les 04 premiers caracteres sont pris en compte)",
    fg="white",
    bg="#004c7f",
    font=('sergio',13,'bold')
)
label.place(
        x=20,
        y=20
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
    x=255,
    y=53,
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
    x=266,
    y=100,
    width=69,
    height=26
)

resultat_label=Label(
    canvas,
    text="Resultat",
    fg="white",
    bg="#004c7f",
    font=('sergio',13,'bold')
)
resultat_label.place(
        x=265,
        y=165
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
        y=200,
        width=300
)

window.mainloop()
