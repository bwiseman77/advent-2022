#! /usr/bin/env python3
import sys

def build_fs():
    path = []
    count = 0
    fs = {}
    # (name, "type", size)
    while (line:=sys.stdin.readline().strip()):
        # get command
        if line.startswith("$"):
            l = line.split(" ")
            file = ""
            command = l[1]
            if(len(l) > 2):
                d       = line.split(" ")[2]
            else:
                d       = ""
            
        elif line.startswith("d"):
            command = ""
            file = ""
            d       = line.split(" ")[1]
            size    = 0

        else:
            command = ""
            d = ""
            size    = int(line.split(" ")[0])
            file    = line.split(" ")[1]

        # do command
        if command == "cd":
            if d == "..":
                path.pop()
            elif d == "/":
                path = []
                path.append(d)
            else:
                path.append(d)

        elif command == "ls":
          pass  
        else:
            # add d to current dir
            curr_path = "+".join(path)
            if file:
                curr_path_file = "+".join(path) + "+" + file
            else:
                curr_path_file = "+".join(path) + "+" + d 
            print(curr_path, curr_path_file)
            if d:
                #path[-1]
                if curr_path in fs:
                    fs[curr_path].append((curr_path_file,"dir",0))
                else:
                     fs[curr_path] = [(curr_path_file, "dir", 0)]
            # add file
            else:
                if curr_path in fs:
                    fs[curr_path].append((curr_path_file, "file", size))
                else:
                    fs[curr_path] = [(curr_path_file, "file", size)]

    return fs

def get_size(fs, d, count):

    size = 0
    for file in fs[d]:
        
        name, ftype, fsize = file
        if ftype == "dir":
            s = get_size(fs, name, count)
            #print(f'size of {name}: {s}')
            if s <= 100000:
                count.append((name, s))
            size += s

        else:
            size += fsize

    return size 

def main():
    fs = build_fs()   
    count = []
    c = 0
    print(fs)

    fs_size = get_size(fs, "/", count)
    print(fs)
    print(fs_size)
    print(count)
    for t in count:
        c += t[1]
    print(c)

            

if __name__ == "__main__":
    main()
