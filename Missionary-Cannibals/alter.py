class CanniHuman:
    # class fields to reduce parameters in the methods

    # number of missionaries at island B
    x2 = 0

    # number of cannibals at island B
    y2 = 0

    # temporary boatman (cannibal) == 0 OR 1
    temp = 0
    a_list = []
    b_list = []
    temp_list = []

    def __init__(self, n):
        # number of missionaries at island A
        self.x1 = n

        # number of cannibals at island A
        self.y1 = n

        # n number of cannibals in the world == n number of humans in the world
        self.n = n
        self.temp = 0
        self.show_splash_screen()
        self.solver()

    def setup(self):

        # initially n cannibals and n humans at island A
        init_set = (self.n, self.n)
        self.a_list.append(init_set)

        # initially 0 cannibals and 0 humans at island B
        init_set = (0, 0)
        self.b_list.append(init_set)

        #
        self.temp_list.append(self.temp)

    def solver(self):
        self.setup()
        total = 2*self.n - 2
        self.first_transfer()
        for i in range(total):
            if self.x1 > self.y1:
                self.transfer_human()
            else:
                self.transfer_cannibal()
        self.last_move()

        self.display_output()




    def transfer_cannibal(self):
        self.y1 -= 1
        self.y2 += 1
        self.a_list.append((self.x1, self.y1))
        self.b_list.append((self.x2, self.y2))
        self.temp_list.append(self.temp)

    def transfer_human(self):
        self.x1 -= 1
        self.x2 += 1
        self.a_list.append((self.x1, self.y1))
        self.temp_list.append(self.temp)
        self.b_list.append((self.x2, self.y2))

    def first_transfer(self):
        # initially transfer 1 cannibals from Island 1 and keep 1 as the boater
        self.y1 -= 1
        self.x1 -= 1
        self.x2 += 1
        # self.y2 += 1
        self.temp += 1
        self.a_list.append((self.x1, self.y1))
        self.b_list.append((self.x2, self.y2))
        self.temp_list.append(self.temp)

    def last_move(self):
        self.temp -= 1
        self.y2 += 1
        self.a_list.append((self.x1, self.y1))
        self.b_list.append((self.x2, self.y2))
        self.temp_list.append(self.temp)

    def display_output(self):
        print("  IslandA                \t\t\t\t\t\tIslandB   ")
        print()
        print(" Human   Cannibal   cann boater             Human   Cannibals")
        # print(f"  temp list =  {len(self.temp_list)}  a list = {len(self.a_list)}  ")
        for i in range(len(self.a_list)):
            print(
                f" {self.a_list[i][0]}    |    {self.a_list[i][1]}   \t\t  {self.temp_list[i]} "
                f"             \t\t\t{self.b_list[i][0]}   |    {self.b_list[i][1]}")
            print(
                f"--------------------------------------------------------------------------------------------------"
                f"----"
                f"----")
    def show_splash_screen(self):
        h_art = '''
                88  88 88   88 8b    d8    db    88b 88 .dP"Y8 
                88  88 88   88 88b  d88   dPYb   88Yb88 `Ybo." 
                888888 Y8   8P 88YbdP88  dP__Yb  88 Y88 o.`Y8b 
                88  88 `YbodP' 88 YY 88 dP""""Yb 88  Y8 8bodP' 
        '''
        c_art = '''
                     dP""b8    db    88b 88 88b 88 88 88""Yb    db    88     
                    dP   `"   dPYb   88Yb88 88Yb88 88 88__dP   dPYb   88     
                    Yb       dP__Yb  88 Y88 88 Y88 88 88""Yb  dP__Yb  88  .o 
                     YboodP dP""""Yb 88  Y8 88  Y8 88 88oodP dP""""Yb 88ood8 

                 '''
        print(h_art)
        print(c_art)


if __name__ == "__main__":
    number_c = int(input("Enter the number of humans or cannibals \n"))

    CanniHuman(number_c)
