import os
from csv import reader
import csv 
from pathlib import Path
from csv import writer
 

SOURCE_CSV_PATH = "source.csv"
DEFAULT_CARACTOS=["ねずこ","たんじろう","ぜんいつ","いのすけ","ぎゆう"]

def read_source(csv_path:str):
    if not os.path.exists(csv_path):
        print(f"csv_path.exists:(csv_path):")
        write_source(csv_path,DEFAULT_CARACTOS)
     
    with open(csv_path,'r',encoding="utf-8_sig")as f:
        return f.read().splitlines()

def write_source(csv_path:str,source:list):
        
    with open(csv_path,"w",encoding="utf-8_sig")as f:
        f.write("\n".join(source))
        
def search2():
    source = read_source(SOURCE_CSV_PATH)
    while True:
        word =input("")
    
        if word in source: 
            print(f"{word}がみつかりました")
        else:
            print(f"{word}は存在しない")
        
            is_add=input("追加登録しますか？（n:しない　y:する)")
            if is_add == "y":
                source.append(word)   
        
        write_source(SOURCE_CSV_PATH, source=source)      
    
if __name__=="__main__":
    search2()