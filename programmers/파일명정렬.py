from collections import OrderedDict
import re
def solution(files):
    hnt = {}
    for file in files:
        hnt[file] = {
            "head":"",
            "number":"",
            "tail":""
        }
        flag = False
        for i in range(len(file)):
            if file[i].isdigit():
                hnt[file]["number"] += file[i]
                flag = True
            elif not file[i].isdigit() and flag == False:
                hnt[file]["head"] += file[i]
            else:
                hnt[file]["tail"] += file[i:]
                break
    
    hnt = OrderedDict(
        sorted(
            hnt.items(),
            key = lambda x: (
                x[1]["head"].lower(),
                int(x[1]["number"])
            )
        )
    )

    return list(hnt.keys())