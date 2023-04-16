class MissionaryBackend:
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
        n = self.n
        self.setup()
        # number of moves which follow normal cases is  stored in total
        # overall the  cases are 2*n with two edge/special cases
        total = 2 * n - 2

        for i in range(total):
            if i == 0:
                # transfer 2 cannibals from island a;
                # keep one at island b
                # keep one as the boat man
                self.first_transfer()
            else:
                if self.x1 > self.y1 and (self.x1 > 0 and self.y1 > 0):
                    self.transfer_human()
                else:
                    self.transfer_cannibal()
        # edge case:
        # transfer last human to island b
        self.transfer_human()
        # now transfer the cannibal boatman to island b
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
        self.y1 -= 2
        self.y2 += 1
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


if __name__ == "__main__":
    MissionaryBackend(5)
