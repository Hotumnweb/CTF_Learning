import re

def extract_flags_file(input_file, output_file):
    with open(input_file,'r',encoding='utf-8') as f:
        r = f.read()
        res = re.findall("flag{.+?}",r)
        print(f'找到了{len(res)}个flag,如下：\n',res)
        with open(output_file,'w',encoding='utf-8') as fi:
            for ch in res:
                fi.write(ch + '\n')
print(extract_flags_file("response.txt","flags_out.txt"))