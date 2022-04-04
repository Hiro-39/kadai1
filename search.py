 
source=["ねずこ","たんじろう","ぜんいつ","いのすけ","ぎゆう"]
source.append("せんじゅうろう")

def search(source):
    word =input("鬼滅のメンバーを入力してください>>>")
    
    if word in source: 
            
            print("{}がみつかりました".format(word))
        
        
    elif word not in source:
            print("{}は存在しない".format(word))
    
if __name__=="__main__":
    print(__name__)
   
    search(source)



from csv import reader
import csv 
from pathlib import Path

#課題1　問３　読み込み
with open('search.csv','r')as csv_file:
    csv_readr=reader(csv_file)
    list_of_rows = list(source)
    print(list_of_rows)


def print_lines():
    print(Path('test.csv').read_text())
    
with open("stock.csv","w",encoding="s")as f:
    writer = csv.writer(f,lineterminator="\n")
    writer.writerow(source)
print_lines()
    



    