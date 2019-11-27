import os
import re
import sys
import shutil

#pathDir为对应文件夹下所有的文件名,sys.argv[1]为终端中输入的文件夹的路径名
pathDir = os.listdir(sys.argv[1])#在终端中执行python3 convertscript.py ../main_test/时，python3不代表任何，converscript.py代表0,后面的文件夹代表1,文件夹可以写绝对路径，也可以写相对路径。
cwpath = os.path.abspath(sys.argv[1])#提取sys.argv[1]的绝对路径
parent_cwpath = os.path.dirname(cwpath)#提取cwpath的上一级目录的绝对路径
#new_folder = parent_cwpath + os.path.sep + sys.argv[1] + "_copy"#新建原始目录对应的文件夹，用来存放修改后的pyx文件
#os.path.sep为目录分隔符
new_folder = cwpath + "_copy"
isExists=os.path.exists(new_folder)#确认文件夹路径是否存在，存在为真，否则为假
#print(isExists)#存在为True,否则为False
if not isExists:
    os.makedirs(new_folder)#如果不存在，新建一个文件夹
else:#如果存在，删除目录，再新建这个目录
    shutil.rmtree(new_folder)
    os.makedirs(new_folder)    
#pathDir = os.listdir("./main_test/")#显示main_test文件夹下所有的文件，这种相对路径不适合在终端中运行
for allDir in pathDir:
    if os.path.splitext(allDir)[1] == '.pxd':#如果文件是以ｐｘｄ结尾的，提取文件名
        filename = os.path.splitext(allDir)[0]#提取文件名
        open_file = cwpath + os.path.sep + filename + '.pxd'#此文件名为绝对路径
        open_file_move = cwpath + os.path.sep + filename + '.pyx'
        #复制原文件夹中的指定文件到另外一个文件夹中  
        shutil.copy(open_file_move, new_folder)
        open_file_add = new_folder + os.path.sep + filename + '.pyx'#复制到新文件夹中的文件,重新定义绝对路径
        with open(open_file, 'r') as f1, open(open_file_add, 'a') as f2:
            head = 'cdef ' + 'class ' +  'Py' + filename + ':' + '\n'
            f2.write(head)
            contents = f1.readlines()
            for content in contents:
                content = content.strip()
                if content.startswith('cdef') and content.endswith(')'):
                    line = re.findall(r'[(](.*?)[)]', content)#提取括号之间的内容为一个字符串
                    line1 = str(line)
                    line2 = line1[2:-2]
                    #print("打印line2:")
                    #print(line2)
                    #print(type(line2))
                    line3 = line2.split(',')
                    num = len(line3)
                    for s in range(num):
                        if line3[s].find('='):
                            a = line3[s]
                            line4 = line3[s].split('=')
                            line5 = line4[0]#提取参数中等号前面的参数名称
                            line3[s] = line5
                    line4 = ','.join(line3)
                    #print("打印line4:")
                    #print(line4)
                    #print(type(line4))
                    content_1 = content.replace(line2, line4)
                    #print("打印content1:")
                    #print(content_1)
                    
                    content_2 = '  ' + '@staticmethod' +'\n' + '  ' + 'def ' + content_1[5:] + ':' + '\n' + '    ' + 'return ' + content_1[5:] + '\n' + '\n' +'\n'
                    f2.write(content_2)
                elif content.endswith(','):#如果此行是以逗号结尾的，打印此行，方便后续手动修改
                    print("The file is: " + open_file + "\n" + "Codes is: " + content)

print("*"*50)

#pathDir_new = os.listdir(new_folder)
#print(pathDir_new)
#for fileName in pathDir_new:
    #print(fileName)
    #pathFile = new_folder + os.path.sep + fileName
    #print(pathFile)
    #with open(pathFile, 'r') as f3:
        #lines = f3.readlines()
        #for line in lines:
            #line = line.strip()
            #if line.startswith('def') and line.endswith(')'):
                #line = re.findall(r'[(](.*?)[)]', line) 
                    
                    
                    
                
                
    