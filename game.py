from src.bg import *
from src.input import *
from src.screen import *
from src.person import *
from src.building import *
from src.constant import *
import os



def process_input1(Build,Buildings,board,Persons,Pos,king,B_lives):
 end=0
 while(end!=1):
    os.system('clear')

    board.display_screen(Build,Buildings,king,1,Pos,Persons,B_lives)
    canon1.is_attacking=0
    canon2.is_attacking=0
    ch = input_to(get, 0.08)
    if(ch=='W'):
        king.move_up(board,Pos)
    elif(ch=='A'):
        king.move_left(board,Pos)
    elif(ch=='S'):
        king.move_down(board,Pos)
    elif(ch=='D'):
        king.move_right(board,Pos)
    elif(ch==' '):
        king.attack(Build,Buildings,board,B_lives)
    elif(ch=='T'):
        troop1.move(Buildings,board,board.screen,Build,Pos,B_lives)
        troop1.bool=1
    elif(ch=='U'):
        troop2.move(Buildings,board,board.screen,Build,Pos,B_lives)
        troop2.bool=1
    elif(ch=='V'):
        troop3.move(Buildings,board,board.screen,Build,Pos,B_lives)
        troop3.bool=1
    elif(ch=='X'):
        
        b1.move(Buildings,board,Build,Pos,B_lives)
        b1.bool=1
  
    elif(ch=='Y'):
        
        b2.move(Buildings,board,Build,Pos,B_lives)
        b2.bool=1
     
    elif(ch=='Z'):
        
        b3.move(Buildings,board,Build,Pos,B_lives)
        b3.bool=1
    if(canon1.life==1):
     canon1.attack(board.screen,Persons,Pos)
    if(canon2.life==1):
      canon2.attack(board.screen,Persons,Pos)
    if(troop1.bool==1):
        if(troop1.health>0):
         troop1.move(Buildings,board,board.screen,Build,Pos,B_lives)
          
    if(troop2.bool==1):
        if(troop2.health>0):
         troop2.move(Buildings,board,board.screen,Build,Pos,B_lives)

    if(troop3.bool==1):
        if(troop3.health>0):
         troop3.move(Buildings,board,board.screen,Build,Pos,B_lives)
    if(b1.bool==1):
    
        b1.move(Buildings,board,Build,Pos,B_lives)
           
    if(b2.bool==1):
        b2.move(Buildings,board,Build,Pos,B_lives)
    if(b3.bool==1):
        b3.move(Buildings,board,Build,Pos,B_lives)
        
    blives=0
    for i in range(0,canon_end+1):
        if(B_lives[i]==1):
            blives=blives+1
    plives=0
    
    for i in range(0,len(Persons)):
        if(Persons[i].life==1):
            plives=plives+1
    if(plives==0):
        print("Defeat:(")
        end=1
    elif(blives==0):
        os.system('clear')
        board.display_screen(Build,Buildings,king,1,Pos,Persons,B_lives)
        print("Victory:)")
        end=1

def process_input2(Build,Buildings,board,Persons,Pos,queen,B_lives):
 end=0
 while(end!=1):
    os.system('clear')
    board.display_screen(Build,Buildings,queen,0,Pos,Persons,B_lives)
    canon1.is_attacking=0
    canon2.is_attacking=0
    ch = input_to(get, 0.08)
    if(ch=='W'):
        queen.move_up(board,Pos)
    elif(ch=='A'):
        queen.move_left(board,Pos)
   
    elif(ch=='S'):
        queen.move_down(board,Pos)
    
    elif(ch=='D'):
        queen.move_right(board,Pos)
   
    elif(ch==' '):
        queen.attack(Build,Buildings,board,B_lives)
     
    elif(ch=='T'):
        
        troop1.move(Buildings,board,board.screen,Build,Pos,B_lives)
        troop1.bool=1
  
    elif(ch=='U'):
        
        troop2.move(Buildings,board,board.screen,Build,Pos,B_lives)
        troop2.bool=1
     
    elif(ch=='V'):
        
        troop3.move(Buildings,board,board.screen,Build,Pos,B_lives)
        troop3.bool=1
    elif(ch=='X'):
        
        b1.move(Buildings,board,Build,Pos,B_lives)
        b1.bool=1
  
    elif(ch=='Y'):
        
        b2.move(Buildings,board,Build,Pos,B_lives)
        b2.bool=1
     
    elif(ch=='Z'):
        
        b3.move(Buildings,board,Build,Pos,B_lives)
        b3.bool=1
    if(canon1.life==1):
     canon1.attack(board.screen,Persons,Pos)
    if(canon2.life==1):
     canon2.attack(board.screen,Persons,Pos)
    if(troop1.bool==1):
    
        troop1.move(Buildings,board,board.screen,Build,Pos,B_lives)
        
           
    if(troop2.bool==1):
        troop2.move(Buildings,board,board.screen,Build,Pos,B_lives)
    if(troop3.bool==1):
        troop3.move(Buildings,board,board.screen,Build,Pos,B_lives)
    if(b1.bool==1):
    
        b1.move(Buildings,board,Build,Pos,B_lives)
        b1.move(Buildings,board,Build,Pos,B_lives)
           
    if(b2.bool==1):
        b2.move(Buildings,board,Build,Pos,B_lives)
        b2.move(Buildings,board,Build,Pos,B_lives)
    if(b3.bool==1):
        b3.move(Buildings,board,Build,Pos,B_lives)
        b3.move(Buildings,board,Build,Pos,B_lives)
    blives=0
    for i in range(0,canon_end+1):
        if(B_lives[i]==1):
            blives=blives+1
    
    plives=0
    for i in range(0,len(Persons)):
        if(Persons[i].life==1):
            plives=plives+1
    if(plives==0):
        print("Defeat:(")
        end=1
    elif(blives==0):
        os.system('clear')
        board.display_screen(Build,Buildings,queen,1,Pos,Persons,B_lives)
        print("Victory:)")
        end=1
    


ch=input("Select  role king:K queen:Q") 
get=Get()

        
   
Build=[]
for i in range(n_rows):
            Build.append([])
            for j in range(n_cols):
                Build[i].append(-1)


board = Screen(n_rows,n_cols)
background = Background(0,0,n_rows,n_cols)
background.show(board.screen,Build)

Buildings=[]
B_lives=[]

#townhall
t_hall=Townhall(0,thall_hitp,2,2,n_rows-4,n_cols-4,thall_no)
t_hall.pos_townhall(board.screen,Build)
Buildings.append(t_hall)
B_lives.append(1)


#huts
huts=[]
for i in range(hut_start,hut_end+1):
    hut=Hut(hut_damage,hut_hitp,1,1,n_rows-1,n_cols-1,i)
    while(board.screen[hut.row][hut.col]!=' '):
          hut=Hut(1,hut_hitp,1,1,n_rows-1,n_cols-1,i)
    hut.pos_hut(board.screen,Build)
    Buildings.append(hut)
    B_lives.append(1)

#canon
canon1=Canon(2,canon_hitp,1,1,n_rows-1,n_cols-1,canon_start)
while(board.screen[canon1.row][canon1.col]!=' '):
          canon1=Canon(canon_damage,canon_hitp,1,1,n_rows-1,n_cols-1,canon_start) 
canon1.pos_canon(board.screen,Build)
Buildings.append(canon1)
B_lives.append(1)
canon2=Canon(2,canon_hitp,1,1,n_rows-1,n_cols-1,canon_end)
while(board.screen[canon2.row][canon2.col]!=' '):
          canon2=Canon(canon_damage,canon_hitp,1,1,n_rows-1,n_cols-1,canon_end) 
canon2.pos_canon(board.screen,Build)
Buildings.append(canon2)
B_lives.append(1)


#walls
walls=[]
for i in range(wall_start,wall_end+1):
    wall=Wall(hut_damage,hut_hitp,1,1,n_rows-1,n_cols-1,i)
    while(board.screen[wall.row][wall.col]!=' '):
          wall=Wall(hut_damage,wall_hitp,1,1,n_rows-1,n_cols-1,i)
    wall.pos_wall(board.screen,Build)
    Buildings.append(wall)
    B_lives.append(1)





#Persons
Pos=[]
for i in range(n_rows):
            Pos.append([])
            for j in range(n_cols):
                Pos[i].append(-1)

Persons=[]

#king
if(ch=='K'):
 king=King(king_damage,king_health,n_rows,n_cols,0)
 while(board.screen[king.row][king.col]!=' '):
        king=King(king_damage,king_health,n_rows,n_cols,0)
 king.pos_king(board.screen,Pos)
 Persons.append(king)
#queen
elif(ch=='Q'):
 queen=Queen(queen_damage,queen_health,n_rows,n_cols,0)
 while(board.screen[queen.row][queen.col]!=' '):
        queen=queen(queen_damage,queen_health,n_rows,n_cols,0)
 queen.pos_queen(board.screen,Pos)
 Persons.append(queen)

distance=[]
for i in range(0,canon_end+1):
    distance.append(-1)

#barbarians
troop1=Troop(troop_damage,troop_health,n_rows-1,n_cols-1,0,1)
while(board.screen[troop1.row][troop1.col]!=' '):
    troop1=Troop(troop_damage,troop_health,n_rows-1,n_cols-1,0,1)
troop2=Troop(troop_damage,troop_health,n_rows-1,n_cols-1,0,2)
while(board.screen[troop2.row][troop2.col]!=' '):
    troop2=Troop(troop_damage,troop_health,n_rows-1,n_cols-1,0,2)
troop3=Troop(troop_damage,troop_health,n_rows-1,n_cols-1,0,3)
while(board.screen[troop3.row][troop3.col]!=' '):
    troop3=Troop(troop_damage,troop_health,n_rows-1,n_cols-1,0,3)
troop1.pos_troop(board,Pos)
Persons.append(troop1)
troop2.pos_troop(board,Pos)
Persons.append(troop2)
troop3.pos_troop(board,Pos)
Persons.append(troop3)

b1=Balloon(balloon_damage,balloon_health,n_rows-1,n_cols-1,0,4)
while(board.screen[b1.row][b1.col]!=' '):
    b1=Balloon(balloon_damage,balloon_health,n_rows-1,n_cols-1,0,4)
b2=Balloon(troop_damage,troop_health,n_rows-1,n_cols-1,0,5)
while(board.screen[b2.row][b2.col]!=' '):
    b2=Balloon(balloon_damage,balloon_health,n_rows-1,n_cols-1,0,5)
b3=Balloon(troop_damage,troop_health,n_rows-1,n_cols-1,0,6)
while(board.screen[b3.row][b3.col]!=' '):
    b3=Balloon(balloon_damage,balloon_health,n_rows-1,n_cols-1,0,6)
b1.pos_troop(board,Pos)
Persons.append(b1)
b2.pos_troop(board,Pos)
Persons.append(b2)
b3.pos_troop(board,Pos)
Persons.append(b3)

if(ch=='K'):
  board.display_screen(Build,Buildings,king,1,Pos,Persons,B_lives)
  process_input1(Build,Buildings,board,Persons,Pos,king,B_lives)
elif(ch=='Q'):
  board.display_screen(Build,Buildings,queen,0,Pos,Persons,B_lives) 
  process_input2(Build,Buildings,board,Persons,Pos,queen,B_lives)





    
