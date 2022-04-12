import numpy as np
from src.constant import *
class Building():
    def __init__(this,damage,hitpoints,min_r,min_c,max_r,max_c,no):
        this.row = np.random.randint(min_r,max_r)
        this.col = np.random.randint(min_c,max_c)
        this.damage=damage
        this.hitpoints=hitpoints
        this.life=1
        this.no=no
        this.danger=0

class Townhall(Building):
    def pos_townhall(this,screen,Build):
        for i in range(0,4):
            for j in range(0,4):
                screen[this.row+i][this.col+j]=3
                Build[this.row+i][this.col+j]=this.no

    def destroy(this,screen,Build):
        this.life=0
        for i in range(0,4):
            for j in range(0,4):
                Build[this.row+i][this.col+j]=-1
                screen[this.row+i][this.col+j]=' '

class Hut(Building):
    def pos_hut(this,screen,Build):
        screen[this.row][this.col]=4
        Build[this.row][this.col]=this.no
    
    def destroy(this,screen,Build):
        this.life=0
        Build[this.row][this.col]=-1
        screen[this.row][this.col]=' '

class Wall(Building):
    def pos_wall(this,screen,Build):
        screen[this.row][this.col]=5
        Build[this.row][this.col]=this.no

    def destroy(this,screen,Build):
        this.life=0
        Build[this.row][this.col]=-1
        screen[this.row][this.col]=' '

class Canon(Building):
    def __init__(this,damage,hitpoints,min_r,min_c,max_r,max_c,no):
        this.is_attacking=0
        super().__init__(damage,hitpoints,min_r,min_c,max_r,max_c,no)
         
    def pos_canon(this,screen,Build):
        screen[this.row][this.col]=6
        Build[this.row][this.col]=this.no

    def destroy(this,screen,Build):
        this.life=0
        Build[this.row][this.col]=-1
        screen[this.row][this.col]=' '

    def attack(this,screen,Persons,Pos):
        once=0
        for i in range(-5,6):
            for j in range(-5,6):
                a1=this.row+i
                b1=this.col+j
                if((i==0 and j==0)):
                    bool=0
                elif(once==0):
                   if(a1>0 and b1>0):
                     if(a1<n_rows-1 and b1<n_cols-1):
                       if(screen[a1][b1]!=' ' and screen[a1][b1]!=8):
                           k=Pos[a1][b1]
                           if(k!=-1):
                            p=Persons[k]
                            # print("entered")
                            if(k==0):
                                print("king")
                                if(p.life==1):
                                    this.is_attacking=1
                                    once=1
                                    p.health=p.health-this.damage
                                if(p.health<=0):
                                    p.life=0
                                    Pos[a1][b1]=-1
                            else:
                                if(p.bool==1):
                                    if(p.life==1):
                                    #  print("troops attacked")
                                     this.is_attacking=1
                                     once=1
                                     p.health=p.health-this.damage
                            if(p.health<=0):
                                p.life=0
                                Pos[a1][b1]=-1
                                screen[a1][b1]=' '
        
                            
                            

