


class Background:
    def __init__(this,i_row,i_col,f_row,f_col):
        this.r_i = i_row
        this.c_i = i_col
        this.r_f = f_row
        this.c_f = f_col

    def show(this, screen,Build):
        for i in range(0, this.r_f-this.r_i):
            for j in range(0, this.c_f-this.c_i):
                
                if(i == 0 or i == this.r_f-this.r_i-1):
                    screen[i][j] = '_'
                    Build[i][j]=-1
                if(j == 0 or j == this.c_f-this.c_i-1):
                    screen[i][j] = '|'
                    Build[i][j]=-1
                    if(i==0):
                        screen[i][j]=' '

                    
