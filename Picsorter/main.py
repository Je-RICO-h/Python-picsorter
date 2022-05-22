import os
import shutil
import sys
import datetime
import json

dateconvert = {
    1: "Jan",
    2: "Feb",
    3: "Marc",
    4: "Apr",
    5: "Maj",
    6: "Jun",
    7: "Jul",
    8: "Aug",
    9: "Szept",
    10: "Okt",
    11: "Nov",
    12: "Dec"
}


def prepare():
    root = ""

    if len(sys.argv) > 1:
        root = sys.argv[1]
    else:
        while not os.path.exists(root) and not os.path.isdir(root):
            root = input("Adj egy helyes elérési mappát: ")

    with open("settings.txt","r") as f:
        settings = json.load(f)

    sorting(root,settings["subfold"],settings["delpar"])


def sorting(root,subfold,delpar):

    files = os.listdir(root)

    if subfold:

        for file in files:

            if os.path.isdir(f"{root}/{file}"):
                subsorting(root,f"/{file}",delpar)

            else:
                modtime = os.path.getmtime(root + "/" + file)
                moddate = datetime.datetime.fromtimestamp(modtime)
                sortfolder = f"{root}/{moddate.year}/{dateconvert[int(moddate.month)]}"

                if not os.path.exists(f"{root}/{moddate.year}"):
                    os.mkdir(f"{root}/{moddate.year}")

                if not os.path.exists(sortfolder):
                    os.mkdir(sortfolder)
                os.rename(root + "/" + file, sortfolder + "/" + file)
    else:

        for file in files:
            if not os.path.isdir(f"{root}/{file}"):

                modtime = os.path.getmtime(root + "/" + file)
                moddate = datetime.datetime.fromtimestamp(modtime)
                sortfolder = f"{root}/{moddate.year}/{dateconvert[int(moddate.month)]}"

                if not os.path.exists(f"{root}/{moddate.year}"):
                    os.mkdir(f"{root}/{moddate.year}")

                if not os.path.exists(sortfolder):
                    os.mkdir(sortfolder)

                os.rename(root + "/" + file, sortfolder + "/" + file)

    if delpar and subfold:
        check = os.listdir(root)
        for i in check:
            if "20" not in i:
                shutil.rmtree(root+"/"+i)

    return


def subsorting(root,path,delpar):
    files = os.listdir(root+path)

    for file in files:

        if os.path.isdir(f"{root + path}/{file}"):
            subsorting(root,f"{path}/{file}",delpar)
        else:
            modtime = os.path.getmtime(root+path+"/"+file)
            moddate = datetime.datetime.fromtimestamp(modtime)

            if delpar:

                sortfolder = f"{root}/{moddate.year}/{dateconvert[int(moddate.month)]}"

                if not os.path.exists(f"{root}/{moddate.year}"):
                    os.mkdir(f"{root}/{moddate.year}")
            else:

                sortfolder = f"{root+path}/{moddate.year}/{dateconvert[int(moddate.month)]}"

                if not os.path.exists(f"{root + path}/{moddate.year}"):
                    os.mkdir(f"{root+path}/{moddate.year}")

            if not os.path.exists(sortfolder):
                os.mkdir(sortfolder)

            os.rename(root+path+"/"+file,sortfolder+"/"+file)
    return

if __name__ == "__main__":
    prepare()
