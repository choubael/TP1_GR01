#la classe neurone
class Neurone:
    w0=2
    w=[0,0,0,0]
    #un constructeur
    def __init__(self) -> None:
        self.w0=2
        self.w=[0,0,0,0]
        
    def __init__(self,w0,w) -> None:
        self.w0=w0
        self.w=w
        
    # la methode y
    def y(self,x):
        y=0.0
        for i in range(0,len(x)):
            y+=self.w[i]*x[i]
        return y-self.w0
    
    #la mathode z
    def z(self,x):
        if(self.y(x)>=0): return 1 
        else : return 0
        
    #la methode apprendre
    def apprendre(self,x,d):
        success=False
        z=self.z(x)
       
        if(z==d):success=True 
        for i in range(0,len(x)): 
            self.w[i]=self.w[i]+(d-z)*x[i]
        self.w0=self.w0-(d-z)
        print(x,'|',z,'|',d,'|',self.w,'|',self.w0,'\n')
        print(success)
        return success 
 
#un ptit main pour l'entrainement
def main():
    Mon_perceptron=Neurone() #constate qu'il prend plus de temps pour l'entrainement
    #perceptron1
    print('perceptron 1\n')
    for i in range(0,10): #10 iterations necessaires d'entrainement
        print('tour ',i+1,'\n')
        Mon_perceptron.apprendre([0,0,0,0],0)
        Mon_perceptron.apprendre([0,0,0,1],0)
        Mon_perceptron.apprendre([0,0,1,0],0)
        Mon_perceptron.apprendre([0,0,1,1],0)
        Mon_perceptron.apprendre([0,1,0,0],0)
        Mon_perceptron.apprendre([0,1,0,1],0)
        Mon_perceptron.apprendre([0,1,1,0],0)
        Mon_perceptron.apprendre([0,1,1,1],0)
        Mon_perceptron.apprendre([1,0,0,0],0)
        Mon_perceptron.apprendre([1,0,0,1],1)
        Mon_perceptron.apprendre([1,0,1,0],0)
        Mon_perceptron.apprendre([1,0,1,1],0)
        Mon_perceptron.apprendre([1,1,0,0],0)
        Mon_perceptron.apprendre([1,1,0,1],0)
        Mon_perceptron.apprendre([1,1,1,0],0)
        Mon_perceptron.apprendre([1,1,1,1],0)
        
    video_perceptron=Neurone()
    print('perceptron 2\n')
    for i in range(0,5):
        print('tour ',i+1,'\n')
        video_perceptron.apprendre([1,1,1,1],0)
        video_perceptron.apprendre([1,1,1,0],0)
        video_perceptron.apprendre([1,1,0,1],0)
        video_perceptron.apprendre([1,1,0,0],0)
        video_perceptron.apprendre([1,0,1,1],0)
        video_perceptron.apprendre([1,0,1,0],0)
        video_perceptron.apprendre([1,0,0,1],1) 
        video_perceptron.apprendre([1,0,0,0],0)
        video_perceptron.apprendre([0,1,1,1],0)
        video_perceptron.apprendre([0,1,1,0],0)
        video_perceptron.apprendre([0,1,0,1],0)
        video_perceptron.apprendre([0,1,0,0],0)
        video_perceptron.apprendre([0,0,1,1],0)
        video_perceptron.apprendre([0,0,1,0],0)
        video_perceptron.apprendre([0,0,0,1],0)
        video_perceptron.apprendre([0,0,0,0],0)




if __name__ == '__main__':
    main()
    
 
           
