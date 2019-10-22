import os, re, time
import sys
from colorama import init
from termcolor import colored

init()

drs = re.findall(r"[A-Z]+:.*$",os.popen("mountvol /").read(),re.MULTILINE)

global res, times
res, ex, masks = [], [], []
inp = []
out_time = False
anal = []
times = {}
stat = False

for k in sys.argv[1:]:

    if k.lower() == "-f":
        ex = [ "Windows", "FileHistory", "Program Files",\
        "Program Files (x86)", "AppData", ".gradle", ".atom", "sdk"]
    elif k.lower() == "-t": out_time = True
    elif k.lower() == "-s": stat = True
    elif "." in k:
        masks.append(k)
        inp.append(k)

for i in range(len(masks)):
    masks[i] = masks[i].replace(".", "\\.")
    masks[i] = masks[i].replace("?", ".")
    masks[i] = masks[i].replace("*", ".*")


if masks:

    def walk(dir_to):
        global times
        # num += 1

        try: 
            os.chdir(dir_to)

            # if num % 200 == 0:
            print("<<<\t" + str(os.getcwd() ) + "\t>>>", flush = True)

            if stat: times[str(os.getcwd())] = time.perf_counter()

            for k in os.listdir():
                # print("\t |" + k, "\t", os.path.isdir(os.getcwd() + "\\" + k))
                # print(">> " + dir_to + "\\" + k)
                if os.path.isdir(dir_to + "\\" + k) and k not in ex:
                    # print(k + " \t +++")
                    try:
                        walk(dir_to + "\\" + k)
                    except: pass
                else:
                    for mask in masks:
                        res_m = re.match(mask, k)
                        if res_m: res_m = res_m[0]
                        if res_m == k: 
                            res.append([dir_to + "\\", k])
                            break

            # print(os.getcwd())
            if stat: 
                anal.append( [ ( time.perf_counter()\
                    - times[str(os.getcwd())] ) *100//1/100, os.getcwd()] )

            os.chdir("..")
            
        except PermissionError: os.chdir("..")

    for disk in drs:
        walk(disk)

    # os.system("cls")
    print("\n\n")
    print("=" * 30)
    print("=" * 30)
    print("\n\n")
    if res != []:
        for i, mask in enumerate(masks):
            print("\n" + colored('>>>', "red") + "\t" + colored(inp[i], 'cyan'))
            for out in res:
                if re.match(mask, out[1]):
                    print(out[0] + colored(out[1], 'green'))

    else: print("Files {} not found".format(masks))

    if stat:
        anal.sort()
        print("\n".join([ str(anal[k][0]) + "s ::: "\
            + str(anal[k][1]) for k in range(len(anal))]))

    if out_time: print("\nWorking time: \t" +\
        colored(str(time.perf_counter()*10//1/10), "yellow") + "s")

    x = input()

else: print("Error argument")

