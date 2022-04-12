from src.constant import *
from colorama import init, Fore, Back, Style
init()
# Screen contains whole game area including left of display


class Screen:
    def __init__(this, r, c):
        this.r = r
        this.c = c
        this.screen = []
        # initialize screen with spaces
        for i in range(this.r):
            this.screen.append([])
            for j in range(this.c):
                this.screen[i].append(' ')
  

    def display_screen(this,Build,Building,player,bool,Pos,Persons,B_lives):
        z=int(player.health)
        # print(Persons[0].life)
        # print(player.life)
        if(bool==1):
         print("king health")
        else:
          print("queen health")
        print(player.health)
        if(z>0):
          while(z!=0):
             print(Back.GREEN+Fore.BLACK+ ' ' + Style.RESET_ALL, end='')
             z=z-1
        print("\n")
        # for i in range(this.r):
        #     for j in range(this.c):
        #      print(this.screen[i][j],end='')
        #     print()
        # print(Building[0].row,Building[0].col)
        # for i in range(1,4):
        #   print("index,r,c,life")
        #   print(Persons[i].tar_ind)
        #   print(Persons[i].a_x)
        #   print(Persons[i].a_y)
        #   print("count")
        #   print(Persons[i].count)
        #   print(Building[Persons[i].tar_ind].life)
        # for i in range(wall_start,wall_end+1):
        #  print("lives")
        #  print(B_lives[i])
        #  print(Building[i].life)
        # #   print(Building[i].danger)
        #  print(Building[i].hitpoints)
        # for i in range(0,6):
        #    print(distance[i])
        for i in range(this.r):
            for j in range(this.c):
                tobeprinted = this.screen[i][j]
                if(tobeprinted==0):
                    if(player.health>0):
                      print(Back.MAGENTA + 'Q' + Style.RESET_ALL, end='')
                    else:
                        print(' ',end='')
                elif(tobeprinted == 1):
                    print(Back.MAGENTA + 'K' + Style.RESET_ALL, end='')
                elif(tobeprinted == 2):
                    t=Pos[i][j]
                    tr=Persons[t]
                    if(tr.life==0):
                      print(' ',end='')
                    elif(tr.a_mode==0):
                     print(Back.BLUE +Fore.BLACK+ 'T' + Style.RESET_ALL, end='') 
                    elif(tr.a_mode==1):
                     print(Back.BLUE +Fore.RED+ 'T' + Style.RESET_ALL, end='') 

                elif(tobeprinted == 3):
                    k=Build[i][j]
                    b=Building[k]
                    p=b.hitpoints/thall_hitp
                    if(p>0.5):
                      print(Back.GREEN+Fore.BLACK + 'X' + Style.RESET_ALL, end='')
                    elif(p>0.25):
                      print(Back.YELLOW+Fore.BLACK + 'X' + Style.RESET_ALL, end='')
                    elif(p>0):
                      print(Back.RED+Fore.BLACK + 'X' + Style.RESET_ALL, end='')
                    else:
                      print(' ',end='')
                elif(tobeprinted == 4):
                    k=Build[i][j]
                    b=Building[k]
                    p=b.hitpoints/hut_hitp
                    if(b.danger==1):
                      print(Back.GREEN+Fore.RED + 'H' + Style.RESET_ALL, end='')
                    elif(p>0.5):
                      print(Back.GREEN+Fore.BLACK + 'H' + Style.RESET_ALL, end='')
                    elif(p>0.25):
                      print(Back.YELLOW+Fore.BLACK + 'H' + Style.RESET_ALL, end='')
                    elif(p>0):
                      print(Back.RED+Fore.BLACK + 'H' + Style.RESET_ALL, end='')
                    else:
                      print(' ',end='')
                elif(tobeprinted == 5):
                    k=Build[i][j]
                    b=Building[k]
                    p=b.hitpoints/hut_hitp
                    if(p>0):
                     print(Back.WHITE+Fore.BLACK +'W'+Style.RESET_ALL, end='')
                    else:
                      print(' ',end='')

                elif(tobeprinted == 6):
                    k=Build[i][j]
                    b=Building[k]
                    # print(b.is_attacking)
                    if(b.is_attacking==0):
                     print(Back.YELLOW+Fore.RED +'C'+Style.RESET_ALL, end='')
                    else:
                     print(Back.RED+Fore.YELLOW+'C'+Style.RESET_ALL, end='')
                elif(tobeprinted==7):
                  if(player.health>0):
                     print(Back.RED+' '+Style.RESET_ALL, end='')
                  else:
                     print(' ',end='')
                elif(tobeprinted==8):
                     print(Back.YELLOW+'B'+Style.RESET_ALL, end='')
                elif(tobeprinted==9):
                     print(Back.RED+'8'+Style.RESET_ALL, end='')
                
                else:
                    print(tobeprinted, end='')
            print()




