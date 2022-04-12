from src.constant import *
import numpy as np
import time
class Person():
    def __init__(this,damage,health,n_rows,n_cols,no):
        this.row = np.random.randint(1,n_rows-1)
        this.col = np.random.randint(1,n_cols-1)
        this.damage=damage
        this.health=health
        this.no=no
        this.life=1
        
    def dec_health(this,damage2):
        this.health=this.health-damage2
    
    def inc_health(this,benefit):
         this.health=this.health+benefit

class King(Person):
    def __init__(this,damage,health,n_rows,n_cols,no):
        this.speed=1
        super().__init__(damage,health,n_rows,n_cols,no)

    def pos_king(this,screen,Pos):
        screen[this.row][this.col]=1
        Pos[this.row][this.col]=this.no

    def move_up(this,screen,Pos):
      
        n=this.row-this.speed
        if(n>0 and screen.screen[n][this.col]==' '):
            screen.screen[this.row][this.col]=' '
            Pos[this.row][this.col]=-1
            this.row=n
           
        screen.screen[this.row][this.col]=1
        Pos[this.row][this.col]=this.no

    def move_down(this,screen,Pos):
        n=this.row+this.speed
        if(n<screen.r-1 and screen.screen[n][this.col]==' '):
            screen.screen[this.row][this.col]=' '
            Pos[this.row][this.col]=-1
            this.row=n
        screen.screen[this.row][this.col]=1
        Pos[this.row][this.col]=this.no

    def move_left(this,screen,Pos):
      
        n=this.col-this.speed
        if(n>0 and screen.screen[this.row][n]==' '):
            screen.screen[this.row][this.col]=' '
            Pos[this.row][this.col]=-1
            this.col=n
        screen.screen[this.row][this.col]=1
        Pos[this.row][this.col]=this.no

    def move_right(this,screen,Pos):
        
        n=this.col+this.speed
        if(n<screen.c-1 and screen.screen[this.row][n]==' '):
            screen.screen[this.row][this.col]=' '
            Pos[this.row][this.col]=-1
            this.col=n
        screen.screen[this.row][this.col]=1
        Pos[this.row][this.col]=this.no

    def attack(this,Build,Buildings,screen,B_lives):
        i=this.row
        j=this.col
        if(this.health!=0):
            if(j+1<screen.c-1 and Build[i][j+1]!=-1):
             k=Build[i][j+1]
            elif(j-1>0 and Build[i][j-1]!=-1):
             k=Build[i][j-1]
            elif(i-1>0 and Build[i-1][j]!=-1):
             k=Build[i-1][j]
            elif(i+1<screen.r-1 and Build[i+1][j]!=-1):
             k=Build[i+1][j]
            else:
             return
            
            b=Buildings[k]
            print(k)
            if(b.hitpoints>0):
              b.hitpoints=b.hitpoints-this.damage
            if(b.hitpoints<=0):
                b.destroy(screen.screen,Build)
                B_lives[k]=0
                # screen.screen[b.row][b.col]=' '

        
         
class Queen(Person):
    def __init__(this,damage,health,n_rows,n_cols,no):
        this.speed=1
        this.dir=0
        this.a_row=-1
        this.a_col=-1
        super().__init__(damage,health,n_rows,n_cols,no)

    def pos_queen(this,screen,Pos):
        screen[this.row][this.col]=0
        Pos[this.row][this.col]=this.no

    def move_up(this,screen,Pos):
       
        n=this.row-this.speed
        if(n>0 and screen.screen[n][this.col]==' '):
            screen.screen[this.row][this.col]=' '
            Pos[this.row][this.col]=-1
            this.row=n
            this.dir=1
            if(this.row-8>0):
                screen.screen[this.a_row][this.a_col]=' '
                # this.a_row=this.row-8
                # this.a_col=this.col
                # if(screen.screen[this.a_row][this.a_col]==' '):
                #       screen.screen[this.a_row][this.a_col]=7
        screen.screen[this.row][this.col]=0
        Pos[this.row][this.col]=this.no

    def move_down(this,screen,Pos):
        n=this.row+this.speed
        if(n<screen.r-1 and screen.screen[n][this.col]==' '):
            screen.screen[this.row][this.col]=' '
            Pos[this.row][this.col]=-1
            this.row=n
            this.dir=2
            if(this.row+8<screen.r-1):
                screen.screen[this.a_row][this.a_col]=' '
                # this.a_row=this.row+8
                # this.a_col=this.col
                # if(screen.screen[this.a_row][this.a_col]==' '):
                #    screen.screen[this.a_row][this.a_col]=7
        screen.screen[this.row][this.col]=0
        Pos[this.row][this.col]=this.no

    def move_left(this,screen,Pos):
      
        n=this.col-this.speed
        if(n>0 and screen.screen[this.row][n]==' '):
            screen.screen[this.row][this.col]=' '
            Pos[this.row][this.col]=-1
            this.col=n
            this.dir=3
            if(this.col-8>0):
                screen.screen[this.a_row][this.a_col]=' '
                # this.a_col=this.col-8
                # this.a_row=this.row
                # if(screen.screen[this.a_row][this.a_col]==' '):
                #    screen.screen[this.a_row][this.a_col]=7
        screen.screen[this.row][this.col]=0
        Pos[this.row][this.col]=this.no

    def move_right(this,screen,Pos):
        
        n=this.col+this.speed
        if(n<screen.c-1 and screen.screen[this.row][n]==' '):
            screen.screen[this.row][this.col]=' '
            Pos[this.row][this.col]=-1
            this.col=n
            this.dir=4
            if(this.col+8<screen.c-1):
                screen.screen[this.a_row][this.a_col]=' '
                # this.a_col=this.col+8
                # this.a_row=this.row
                # if(screen.screen[this.a_row][this.a_col]==' '):
                #   screen.screen[this.a_row][this.a_col]=7
        screen.screen[this.row][this.col]=0
        Pos[this.row][this.col]=this.no

    def attack(this,Build,Buildings,screen,B_lives):
        m=-1
        n=-1
        if(this.health!=0):
            if(this.dir==1):
                m=this.row-8
                n=this.col
            elif(this.dir==2):
                m=this.row+8
                n=this.col
            elif(this.dir==3):
                n=this.col-8
                m=this.row
            elif(this.dir==4):
                n=this.col+8
                m=this.row
            if(m>0 and m<screen.r-1 and n>0 and n<screen.c-1):
             for i in range(m-2,m+3):
                for j in range(n-2,n+3):
                   c=1
                   if(j+1<screen.c-1 and Build[i][j+1]!=-1):
                      k=Build[i][j+1]
                   elif(j-1>0 and Build[i][j-1]!=-1):
                      k=Build[i][j-1]
                   elif(i-1>0 and Build[i-1][j]!=-1):
                         k=Build[i-1][j]
                   elif(i+1<screen.r-1 and Build[i+1][j]!=-1):
                       k=Build[i+1][j]
                   else:
                       c=0
                   if(c==1):
                      b=Buildings[k]
                    #   print(k)
                      if(b.hitpoints>0):
                         b.hitpoints=b.hitpoints-this.damage
                      if(b.hitpoints<=0):
                         b.destroy(screen.screen,Build)
                         B_lives[k]=0
         
    
class Balloon(Person):
    def __init__(this,damage,health,n_rows,n_cols,bool,no):
        this.bool=0
        this.prev_i=0
        this.prev_j=0
        this.a_mode=0
        this.a_x=-1
        this.a_y=-1
        this.tar_ind=-1
        this.count=0
        this.prevb=-1
        super().__init__(damage,health,n_rows,n_cols,no)

    def pos_troop(this,screen,Pos):
        screen.screen[this.row][this.col]=8
        Pos[this.row][this.col]=this.no

    def move(this,Buildings,screen,Build,Pos,B_lives):
        d=[]
        x1=0
        y1=0
      
        if(this.a_mode==0 ):
            if(B_lives[canon_start]==1):
                index=canon_start
            elif(B_lives[canon_end]==1):
                index=canon_end
            else:
             for i in range(0,canon_start):
                b=Buildings[i]
                if(B_lives[i]==1):
                  x=b.row-this.row
                  y=b.col-this.col
                  d.append(x*x+y*y)
                  
                else:
                  d.append(-1)
                  
             min=n_cols*3*n_cols*3*3
             index=-1
             for i in range(0,canon_start): 
                 if(d[i]<min and d[i]!=-1):
                    min=d[i]
                    index=i
             if(index==-1):
                 return
            b=Buildings[index]
            this.tar_ind=index
            b.danger=1
            this.a_x=b.row
            this.a_y=b.col
            this.a_mode=1
        r1=this.a_x-this.row
        c1=this.a_y-this.col
        x=this.a_x
        y=this.a_y
        x1=1
        y1=1
        min=n_cols*3*3*n_cols
        t=-1
        if(this.tar_ind==0):
            i=this.row
            j=this.col
        
            if(j+1<screen.c-1 ):
              if(Build[i][j+1]==0):
                 t=0

              elif(i+1<screen.r-1):
                 if(Build[i+1][j+1]==0):
                  t=0
              elif(i-1>0):
                if(Build[i-1][j+1]==0):
                  t=0
            if(j-1>0 ):
                if( Build[i][j-1]==0):
                  t=0
                elif(i+1<screen.r-1):
                 if(Build[i+1][j-1]==0):
                  t=0
                elif(i-1>0):
                 if(Build[i-1][j-1]==0):
                  t=0
            if(i-1>0 ):
                if(Build[i-1][j]==0):
                    t=0
            if(i+1<screen.r-1):
                 if(Build[i+1][j]==0):
                    t=0
            if(t!=0):
                for i in range(-1,2):
                 for j in range(-1,2):
                  if(i==0 and j==0):
                     bool=0
                  else:
                     a1=this.row+i
                     b1=this.col+j
                  if(a1!=0 and b1!=0 and a1!=n_rows-1 and b1!=n_cols-1):
                   if(screen.screen[a1][b1]==' ' or Build[a1][b1]!=-1):
                    x=this.a_x-(a1)
                    y=this.a_y-(b1)
                    if(x*x+y*y<min):
                      min=x*x+y*y
                      x1=i
                      y1=j
                
                if(screen.screen[this.row+x1][this.col+y1]==' '):
                 if(this.prevb!=-1):
                     screen.screen[this.row][this.col]=this.prevb
                 else:
                     screen.screen[this.row][this.col]=' '
                 this.prevb=-1
                 
                 Pos[this.row][this.col]=-1
            
                 this.row=this.row+x1
                 this.col=this.col+y1
    
                 screen.screen[this.row][this.col]=8
                 Pos[this.row][this.col]=this.no
                elif(screen.screen[this.row+x1][this.col+y1]==5 or screen.screen[this.row+x1][this.col+y1]==3 or screen.screen[this.row+x1][this.col+y1]==4): 
                 n=screen.screen[this.row+x1][this.col+y1]
                 if(this.prevb!=-1):
                     screen.screen[this.row][this.col]=this.prevb
                 else:
                     screen.screen[this.row][this.col]=' '
                 this.prevb=n
                 Pos[this.row][this.col]=-1
                 this.row=this.row+x1
                 this.col=this.col+y1
    
                 screen.screen[this.row][this.col]=9
                 Pos[this.row][this.col]=this.no
     
            
            if(t==0):
             b=Buildings[0]
             if(b.hitpoints>0):
                  b.hitpoints=b.hitpoints-this.damage
             if(b.hitpoints<=0):
                  b.destroy(screen.screen,Build)
                  this.a_mode=0
                  b.life=0
                  this.a_x=-1
                  this.a_y=-1
                  B_lives[this.tar_ind]=0
                  this.tar_ind=-1
                  b.danger=-1
     
        else:
         t=-1
         if(r1==0 and c1==1):
               t=Build[this.row][this.col+1]
               
         elif(r1==0 and c1==-1):
            
               t=Build[this.row][this.col-1]
               

         elif(c1==0 and r1==1):
               t=Build[this.row+1][this.col]
              

               

         elif(c1==0 and r1==-1):
               t=Build[this.row-1][this.col]
               

         elif(r1==1 and c1==1):
               t=Build[this.row+1][this.col+1]
               
               
        
         elif(r1==1 and c1==-1):
               t=Build[this.row+1][this.col-1]
              
               

         elif(r1==-1 and c1==1):
               t=Build[this.row-1][this.col+1]
               
               
         elif(r1==-1 and c1==-1):
               t=Build[this.row-1][this.col-1]
              
               
         else:
          attack=0
          this.a_mode=1
          
           
          for i in range(-1,2):
           for j in range(-1,2):
             if(i==0 and j==0):
                  bool=0
             else:
               a1=this.row+i
               b1=this.col+j
               if(a1!=0 and b1!=0 and a1!=n_rows-1 and b1!=n_cols-1):
                 if(screen.screen[a1][b1]==' ' or Build[a1][b1]!=-1):
                  x=this.a_x-(a1)
                  y=this.a_y-(b1)
                  if(x*x+y*y<min):
                      min=x*x+y*y
                      x1=i
                      y1=j
          if(screen.screen[this.row+x1][this.col+y1]==' '):
                 if(this.prevb!=-1):
                     screen.screen[this.row][this.col]=this.prevb
                 else:
                     screen.screen[this.row][this.col]=' '
                 this.prevb=-1
                 
                 Pos[this.row][this.col]=-1
            
                 this.row=this.row+x1
                 this.col=this.col+y1
    
                 screen.screen[this.row][this.col]=8
                 Pos[this.row][this.col]=this.no
          elif(screen.screen[this.row+x1][this.col+y1]==5 or screen.screen[this.row+x1][this.col+y1]==4 or screen.screen[this.row+x1][this.col+y1]==3): 
                 n=screen.screen[this.row+x1][this.col+y1]
                 if(this.prevb!=-1):
                     screen.screen[this.row][this.col]=this.prevb
                 else:
                     screen.screen[this.row][this.col]=' '
                 this.prevb=n
                 Pos[this.row][this.col]=-1
                 this.row=this.row+x1
                 this.col=this.col+y1
    
                 screen.screen[this.row][this.col]=9
                 Pos[this.row][this.col]=this.no
                 

          return
    
         b=Buildings[t]
         if(b.hitpoints>0):
                  b.hitpoints=b.hitpoints-this.damage
         if(b.hitpoints<=0):
                  b.destroy(screen.screen,Build)
                  this.a_mode=0
                  b.life=0
                  this.a_x=-1
                  this.a_y=-1
                  B_lives[this.tar_ind]=0
                  this.tar_ind=-1
                  b.danger=-1
                  

class Troop(Person):
    def __init__(this,damage,health,n_rows,n_cols,bool,no):
        this.bool=0
        this.prev_i=0
        this.prev_j=0
        this.a_mode=0
        this.a_x=-1
        this.a_y=-1
        this.tar_ind=-1
        this.count=0
        super().__init__(damage,health,n_rows,n_cols,no)

    def pos_troop(this,screen,Pos):
        screen.screen[this.row][this.col]=2
        Pos[this.row][this.col]=this.no

    def move(this,Buildings,board,screen,Build,Pos,B_lives):
        d=[]
        x1=0
        y1=0
      
        if(this.a_mode==0 ):
             for i in range(0,canon_end+1):
                b=Buildings[i]
                if(B_lives[i]==1):
                  x=b.row-this.row
                  y=b.col-this.col
                  d.append(x*x+y*y)
                  
                else:
                  d.append(-1)
                  
             min=n_cols*3*n_cols*3*3
             index=-1
             for i in range(0,canon_end+1): 
                 if(d[i]<min and d[i]!=-1):
                    min=d[i]
                    index=i
             if(index==-1):
                 return
             b=Buildings[index]
             this.tar_ind=index
             b.danger=1
             this.a_x=b.row
             this.a_y=b.col
             this.a_mode=1
        r1=this.a_x-this.row
        c1=this.a_y-this.col
        x=this.a_x
        y=this.a_y
        x1=1
        y1=1
        min=n_cols*3*3*n_cols
        t=-1
        if(this.tar_ind==0):
            i=this.row
            j=this.col
        
            if(j+1<board.c-1 ):
              if(Build[i][j+1]==0):
                 t=0

              elif(i+1<board.r-1):
                 if(Build[i+1][j+1]==0):
                  t=0
              elif(i-1>0):
                if(Build[i-1][j+1]==0):
                  t=0
            if(j-1>0 ):
                if( Build[i][j-1]==0):
                  t=0
                elif(i+1<board.r-1):
                 if(Build[i+1][j-1]==0):
                  t=0
                elif(i-1>0):
                 if(Build[i-1][j-1]==0):
                  t=0
            if(i-1>0 ):
                if(Build[i-1][j]==0):
                    t=0
            if(i+1<board.r-1):
                 if(Build[i+1][j]==0):
                    t=0
            if(t!=0):
                for i in range(-1,2):
                 for j in range(-1,2):
                  if(i==0 and j==0):
                     bool=0
                  else:
                     a1=this.row+i
                     b1=this.col+j
                  if(a1!=0 and b1!=0 and a1!=n_rows-1 and b1!=n_cols-1):
                   if(screen[a1][b1]==' ' or screen[a1][b1]==5):
                    x=this.a_x-(a1)
                    y=this.a_y-(b1)
                    if(x*x+y*y<min):
                      min=x*x+y*y
                      x1=i
                      y1=j
                if(screen[this.row+x1][this.col+y1]==5):
                         t=Build[this.row+x1][this.col+y1]
                         if(Buildings[t].hitpoints>0):
                          Buildings[t].hitpoints=Buildings[t].hitpoints-this.damage
                         if(Buildings[t].hitpoints<=0):
                          Buildings[t].destroy(screen,Build)
                          
                elif(screen[this.row+x1][this.col+y1]==' '):
                  screen[this.row][this.col]=' '
                  Pos[this.row][this.col]=-1
            
                  this.row=this.row+x1
                  this.col=this.col+y1
    
                  screen[this.row][this.col]=2
                  Pos[this.row][this.col]=this.no
                else:
                 return
            if(t==0):
             b=Buildings[0]
             if(b.hitpoints>0):
                  b.hitpoints=b.hitpoints-this.damage
             if(b.hitpoints<=0):
                  b.destroy(screen,Build)
                  this.a_mode=0
                  b.life=0
                  this.a_x=-1
                  this.a_y=-1
                  B_lives[this.tar_ind]=0
                  this.tar_ind=-1
                  b.danger=-1
     
        else:
         t=-1
         if(r1==0 and c1==1):
               t=Build[this.row][this.col+1]
               
         elif(r1==0 and c1==-1):
            
               t=Build[this.row][this.col-1]
               

         elif(c1==0 and r1==1):
               t=Build[this.row+1][this.col]
              

               

         elif(c1==0 and r1==-1):
               t=Build[this.row-1][this.col]
               

         elif(r1==1 and c1==1):
               t=Build[this.row+1][this.col+1]
               
               
        
         elif(r1==1 and c1==-1):
               t=Build[this.row+1][this.col-1]
              
               

         elif(r1==-1 and c1==1):
               t=Build[this.row-1][this.col+1]
               
               
         elif(r1==-1 and c1==-1):
               t=Build[this.row-1][this.col-1]
              
               
         else:
          attack=0
          this.a_mode=1
          
           
          for i in range(-1,2):
           for j in range(-1,2):
             if(i==0 and j==0):
                  bool=0
             else:
               a1=this.row+i
               b1=this.col+j
               if(a1!=0 and b1!=0 and a1!=n_rows-1 and b1!=n_cols-1):
                 if(screen[a1][b1]==' ' or screen[a1][b1]==5):
                  x=this.a_x-(a1)
                  y=this.a_y-(b1)
                  if(x*x+y*y<min):
                      min=x*x+y*y
                      x1=i
                      y1=j
          if(screen[this.row+x1][this.col+y1]==5):
               t=Build[this.row+x1][this.col+y1]
               b=Buildings[t]
               if(b.hitpoints>0):
                  b.hitpoints=b.hitpoints-this.damage
               if(b.hitpoints<=0):
                  b.destroy(screen,Build)
                  screen[this.row+x1][this.col+y1]==' '
          elif(screen[this.row+x1][this.col+y1]==' '):
             screen[this.row][this.col]=' '
             Pos[this.row][this.col]=-1
            
             this.row=this.row+x1
             this.col=this.col+y1
    
             screen[this.row][this.col]=2
             Pos[this.row][this.col]=this.no
          return
    
         b=Buildings[t]
         if(b.hitpoints>0):
                  b.hitpoints=b.hitpoints-this.damage
         if(b.hitpoints<=0):
                  b.destroy(screen,Build)
                  this.a_mode=0
                  b.life=0
                  this.a_x=-1
                  this.a_y=-1
                  B_lives[this.tar_ind]=0
                  this.tar_ind=-1
                  b.danger=-1
                  
 
            

            
        
          


                 
               
        
                 
               
         






