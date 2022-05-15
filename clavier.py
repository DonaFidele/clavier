#coding:utf-8
import tkinter as tk
from tkinter.messagebox import *

class Clavier( tk.Tk ): 

    def __init__ ( self ):
        tk.Tk.__init__( self )

    def touches_de_fonction(self,texte,ligne,colonne):
            self.boutton=tk.Button(bg="black", width=6, height=1, text=texte, foreground="white").grid(row=ligne, column=colonne,padx=0,sticky='W')
    
    def touches_alpha_1(self,texte,ligne,colonne):
        self.boutton=tk.Button(bg="black", width=6, height=4, text=texte, foreground="white").grid(row=ligne, column=colonne,pady=5)

    def touches_alpha_2(self,texte,ligne,colonne):
        self.boutton=tk.Button(bg="black", width=4, height=3, text=texte, foreground="white",font="arial 16").grid(row=ligne, column=colonne,pady=2)

    def quitter(self,ligne,colonne):
        self.boutton=tk.Button(bg="black", width=8, height=2, text='Quitter', foreground="white",font="arial 10",command=self.quit).grid(row=ligne, column=colonne,pady=10)

    def creer_des_bouttons(self):
        self.touches_de_fonction('echap',0,0)
        self.touches_de_fonction('f1 [||]',0,1)
        self.touches_de_fonction('f2 ',0,2)
        self.touches_de_fonction('f3☀ ',0,3)
        self.touches_de_fonction('f4☀ ',0,4)
        self.touches_de_fonction('f5',0,5)
        self.touches_de_fonction('f6',0,6)
        self.touches_de_fonction('f7',0,7)
        self.touches_de_fonction('f8',0,8)
        self.touches_de_fonction('f9',0,9)
        self.touches_de_fonction('f10',0,10)
        self.touches_de_fonction('f11',0,11)
        self.touches_de_fonction('f12',0,12)
        self.touches_de_fonction('impécr',0,13)
        self.touches_de_fonction('suppr',0,14)
        self.touches_de_fonction('↖',0,15)
        self.touches_de_fonction('fin',0,16)
        self.touches_de_fonction('⬆',0,17)
        self.touches_de_fonction('⬇',0,18)

        self.boutton=tk.Button(bg="black", width=5, height=4, text='\n\n2', foreground="white").grid(row=1, column=0,padx=0,sticky='W')

        self.touches_alpha_1('1\n\n& ',1,1)
        self.touches_alpha_1('2\n\né ~',1,2)
        self.touches_alpha_1('3\n\n"  #',1,3)
        self.touches_alpha_1("4\n\n'  {",1,4)
        self.touches_alpha_1('5\n\n(  [ ',1,5)
        self.touches_alpha_1('6\n\n-  | ',1,6)
        self.touches_alpha_1('7\n\nè ` ',1,7)
        self.touches_alpha_1('8\n\n_ \ ',1,8)
        self.touches_alpha_1('9\n\n  [ ',1,9)
        self.touches_alpha_1('0\n\nà  @',1,10)
        self.touches_alpha_1('°\n\n) ] ',1,11)
        self.touches_alpha_1('+\n\n= }',1,12)

        self.boutton=tk.Button(bg="black", width=15, height=4, text='⬅', foreground="white").grid(row=1, column=13,columnspan=2)

        self.touches_alpha_1('ver\n\nnum',1,15)
        self.touches_alpha_1('/\n',1,16)
        self.touches_alpha_1('*\n\n',1,17)
        self.touches_alpha_1('-\n\n',1,18)

        self.boutton=tk.Button(bg="black", width=17, height=5, text="""⬅     \n➡     """, foreground="white",font="arial 10").grid(row=2, column=0,columnspan=2,padx=0,sticky='W')

        self.touches_alpha_2("A\n",2,2)
        self.touches_alpha_2('Z\n',2,3)
        self.touches_alpha_2('E\n',2,4)
        self.touches_alpha_2('R\n',2,5)
        self.touches_alpha_2('T\n',2,6)
        self.touches_alpha_2('Y\n',2,7)
        self.touches_alpha_2('U\n',2,8)
        self.touches_alpha_2('I\n',2,9)
        self.touches_alpha_2('O\n',2,10)
        self.touches_alpha_2('P\n',2,11)
        self.touches_alpha_2('¨\n^',2,12)
        self.touches_alpha_2('£\n$',2,13)
        #self.touches_alpha_2('⬅',2,14)
        self.boutton=tk.Button(bg="black", width=4, height=7, text='⬅', foreground="white",font="arial 16").grid(row=2, column=14,pady=2,rowspan=2)
        self.touches_alpha_2('7\n\n↖',2,15)
        self.touches_alpha_2('8\n\n⬆',2,16)
        self.touches_alpha_2('9\n\n⬆',2,17)
        
        self.boutton=tk.Button(bg="black", width=4, height=7, text='+', foreground="white",font="arial 16").grid(row=2, column=18,pady=2,rowspan=2)
        self.boutton=tk.Button(bg="black", width=12, height=3, foreground="white",font="arial 16").grid(row=3, column=0,pady=2,columnspan=2,padx=0,sticky='W')
        
        self.touches_alpha_2("Q\n",3,2)
        self.touches_alpha_2('S\n',3,3)
        self.touches_alpha_2('D\n',3,4)
        self.touches_alpha_2('F\n',3,5)
        self.touches_alpha_2('G\n',3,6)
        self.touches_alpha_2('H\n',3,7)
        self.touches_alpha_2('J\n',3,8)
        self.touches_alpha_2('K\n',3,9)
        self.touches_alpha_2('L\n',3,10)
        self.touches_alpha_2('M\n',3,11)
        self.touches_alpha_2('%\n\nù',3,12)
        self.touches_alpha_2('µ\n\n*',3,13)
        self.touches_alpha_2("4\n⬅",3,15)
        self.touches_alpha_2('5\n',3,16)
        self.touches_alpha_2('6\n➡',3,17)

        #touches de la ligne 5
        self.boutton=tk.Button(bg="black", width=8, height=5, text='⬆\n\nver fin', foreground="white",font="arial 10").grid(row=4, column=0,pady=2,padx=0,sticky='W')
        self.boutton=tk.Button(bg="black", width=8, height=5, text='>\n\n<', foreground="white",font="arial 10").grid(row=4, column=1,pady=2)
        
        self.touches_alpha_2("W\n",4,2)
        self.touches_alpha_2('X\n',4,3)
        self.touches_alpha_2('C\n',4,4)
        self.touches_alpha_2('V\n',4,5)
        self.touches_alpha_2('B\n',4,6)
        self.touches_alpha_2('N\n',4,7)
        self.touches_alpha_2('?\n\n,',4,8)
        self.touches_alpha_2('.\n\n;',4,9)
        self.touches_alpha_2('/\n\n:',4,10)
        self.touches_alpha_2('§\n\n!',4,11)
        self.boutton=tk.Button(bg="black", width=25, height=4, text="⬆ pause", foreground="white").grid(row=4, column=12,columnspan=3)
        self.touches_alpha_2('1\n\nfin',4,15)
        self.touches_alpha_2('2\n\n⬇',4,16)
        self.touches_alpha_2('3\n\n⬇',4,17)
        
        self.boutton=tk.Button(bg="black", width=4, height=7, text='⬅', foreground="white",font="arial 16").grid(row=4, column=18,pady=2,rowspan=2)
        self.boutton=tk.Button(bg="black", width=8, height=5, text='ctrl', foreground="white",font="arial 10").grid(row=5, column=0,pady=2,padx=0,sticky='W')
        self.boutton=tk.Button(bg="black", width=8, height=5, text='\nfn', foreground="white",font="arial 10").grid(row=5, column=1,pady=2)
        self.boutton=tk.Button(bg="black", width=8, height=5, text='\n|_|_|', foreground="white",font="arial 10").grid(row=5, column=2,pady=2)
        self.boutton=tk.Button(bg="black", width=8, height=5, text='\nalt', foreground="white",font="arial 10").grid(row=5, column=3,pady=2)
        
        self.boutton=tk.Button(bg="black", width=50, height=5, text='', foreground="white").grid(row=5, column=4,columnspan=5)

        self.boutton=tk.Button(bg="black", width=8, height=5, text='\nalt gr', foreground="white",font="arial 10").grid(row=5, column=9,pady=2)
        self.boutton=tk.Button(bg="black", width=8, height=5, text='\nctrl', foreground="white",font="arial 10").grid(row=5, column=10,pady=2)
        self.boutton=tk.Button(bg="black", width=8, height=5, text='\nctrl', foreground="white",font="arial 10").grid(row=5, column=11,pady=2)
        self.boutton=tk.Button(bg="black", width=4, height=3, text='<', foreground="white",font="arial 16").grid(row=5, column=11,pady=2)

        self.boutton=tk.Button(bg="black", width=14, height=2, text= '↗↖', foreground="white").grid(row=5, column=12,pady=2,sticky='N',columnspan=2)
        self.boutton=tk.Button(bg="black", width=14, height=2, text= '↘↙', foreground="white").grid(row=5, column=12,pady=2,sticky='S',columnspan=2)

        self.boutton=tk.Button(bg="black", width=8, height=5, text='\nctrl', foreground="white",font="arial 10").grid(row=5, column=14,pady=2)
        self.boutton=tk.Button(bg="black", width=4, height=3, text='>', foreground="white",font="arial 16").grid(row=5, column=14,pady=2)
        
        self.boutton=tk.Button(bg="black", width=18, height=5, text="0\n\ninser", foreground="white",font="arial 10").grid(row=5, column=15,columnspan=2)
        self.boutton=tk.Button(bg="black", width=8, height=5, text='.\n\nsuppr', foreground="white",font="arial 10").grid(row=5, column=17,pady=2)
        
        self.quitter(7,18)
if __name__ == "__main__":
    clavier=Clavier()
    clavier.title("MON      😁️     CLAVIER       😃️") 
    clavier.creer_des_bouttons()
    clavier.resizable(width=False,height=False)
    clavier.mainloop()
    