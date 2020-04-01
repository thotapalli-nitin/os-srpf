def WT(processes, n, wt):
    rt = [0] * n
    for i in range(n):
        rt[i] = processes[i][1]

    total= 0
    t = 0
    min = 999
    var = 0
    chk = False

    while (total!= n):
        for j in range(n):
            if ((processes[j][2] <= t) and
                    (rt[j] < min) and rt[j] > 0):
                min = rt[j]
                var = j
                chk = True

            if (chk == False):
                t += 1
                continue


            if (rt[j] >= 2):
                rt[j] -= 2
            elif (rt[j] == 1):
                rt[j] -= 1

        min = rt[var]
        if (min == 0):
            min = 999999999

        if (rt[var] == 0):
            total += 1
            chk = False


        fint = t + 1

        wt[var] = (fint - bt[var][1] -
                     bt[var][2])


        t += 1

def TAT(processes, n, wt, tat):

    for i in range(n):
        tat[i] = processes[i][1] + wt[i]

def AVGT(processes, n):
    wt = [0] * n
    tat = [0] * n

    WT(processes, n, wt)

    TAT(processes, n, wt, tat)

    print("Processes Arrival Time  Burst Time	 Waiting",
          "Time	 Turn-Around Time")
    total_waiting_time = 0
    total_turn_around_time = 0
    for i in range(n):
        total_waiting_time = total_waiting_time + wt[i]
        total_turn_around_time = total_turn_around_time + tat[i]
        print(" ", processes[i][0], "\t\t\t", processes[i][2], "\t\t\t", processes[i][1], "\t\t\t\t", wt[i], "\t\t\t",
              tat[i])

    print("\nAvg WT of the processes is  =  ",(total_waiting_time / n))
    print("Avg TAT of the processes is= ", (total_turn_around_time / n))


if __name__ == "__main__":
    n = int(input('Enter the number of processes: '))
    bt = [0] * (n + 1)
    art = [0] * (n + 1)
    abt = [0] * (n + 1)
    for i in range(n):
        abt[i] = int(input('Enter the burst time for process {} : '.format(1+i)))
        art[i] = int(input('Enter the arrival time for  process {} : '.format(1+i)))
        bt[i] = [i, abt[i], art[i]]

AVGT(bt, n)
