import json
import sys

def deep_diff():
    try:
        #standart input=stdin
        line1 = sys.stdin.readline()
        line2 = sys.stdin.readline()
        
        if not line1 or not line2:
            return
#When you read JSON from input, it comes in as a string (text)
#Бұл жолдар енгізуден алынған JSON мәтінін Python сөздіктеріне түрлендіреді, сондықтан бағдарлама кілттер 
# мен мәндерді оңай қол жеткізіп, салыстыра алады

        obj_a = json.loads(line1)
        obj_b = json.loads(line2)
    except (ValueError, EOFError):
        return
        #end of file error ,
    

    differences = []

    def serialize(val):
        if val == "<missing>":
            return "<missing>"
        return json.dumps(val, separators=(',', ':'))

    def compare(a, b, path):
        # Both are dictionaries - recurse-салыстру
        if isinstance(a, dict) and isinstance(b, dict):
            all_keys = sorted(set(a.keys()) | set(b.keys()))
            for key in all_keys:
                new_path = f"{path}.{key}" if path else key
                val_a = a.get(key, "<missing>")#bir key bar,ekinshisi jok bolsa
                val_b = b.get(key, "<missing>")
                compare(val_a, val_b, new_path)
        
        #  One is missing or they are different values/types
        elif a != b:
            differences.append(f"{path} : {serialize(a)} -> {serialize(b)}")#serialize(val): Табылған айырмашылықты қайтадан JSON форматына (мәтінге) 
            #айналдырып, әдемілеп көрсетеді

    compare(obj_a, obj_b, "")

    if not differences:#list bos bolsa
        print("No differences")
    else:
        # Problem asks for lexicographical sort by path
        differences.sort()
        for diff in differences:
            print(diff)

if __name__ == "__main__":
    deep_diff() 
    #JSON-ды жай мәтін ретінде салыстыру мүмкін емес,
    #  өйткені ішіндегі элементтердің орны ауысып тұруы 
    # мүмкін. Ал сөздікке айналдыру арқылы біз нақты кілттерді 
    # keys салыстырамыз." recursia=JSON құрылымы иерархиялық .#power switch 
