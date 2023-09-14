from typing import List
import argparse

class TreeNode:
    def __init__(self, val: str):
        self.val = val
        self.dirs = []
        self.files = []

    def addDir(self, val: str):
        self.dirs.append(TreeNode(val))

    def addFile(self, file: str):
        sz, fname = file.split()
        self.files.append((fname, int(sz)))

def p11(fstree: 'TreeNode') -> int:
    result = []
    total = fs_sizes(fstree, result, 100000)
    print(result, total)
    return sum(sz for dir,sz in result)

def p21(fstree: 'TreeNode') -> int:
    result = []
    total = fs_sizes(fstree, result, 30000000)
    used_sz = 70000000 - total
    needed_sz = 30000000 - used_sz

    out = []
    for d, sz in result:
        if sz > needed_sz:
            out.append((d, sz))

    out = sorted(out, key=lambda x: x[1])
    print(out[0])
    
def fs_sizes(fstree: 'TreeNode', result: List[str], ds: int):
    print(fstree.val, fstree.dirs, fstree.files)
    total = 0
    for d in fstree.dirs:
        sz = fs_sizes(d, result, ds)
        total += sz
    for fname, sz in fstree.files:
        total += sz

    if total < ds:
        result.append((fstree.val, total))

    return total

def build_fs_tree(commands: List[str], stack: List[TreeNode]):
    if not commands:
        return root
    i = 0
    c = commands[i]
    print(c, i)

    if c[0] == '$':
        cmd = c.split()
        if len(cmd) == 2 and cmd[1] == 'ls':
            i += 1
            c = commands[i]
            print('-', c)
            while c[0] != '$' and i < len(commands):
                arg1, arg2 = c.split()
                tn = stack[-1]

                if arg1 == 'dir':
                    tn.addDir(arg2)
                else:
                    tn.addFile(c)
                i += 1
                if i < len(commands):
                    c = commands[i]
            i -= 1
        else:
            dirname = cmd[2]
            if dirname == '..':
                stack.pop()
                if len(commands[1:]) > 0:
                    build_fs_tree(commands[i+1:], stack)
                    return
            else:
                if len(stack) == 0:
                    tn = TreeNode(dirname)
                    stack.append(tn)
                tn = stack[-1]
                for d in tn.dirs:
                    if d.val == dirname:
                        stack.append(d)
                        break
        if commands[i+1:]:
            build_fs_tree(commands[i+1:], stack)
    else:
        print('fuck')     
                
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input file")
    args = parser.parse_args()

    f = open(args.input, 'r')
    commands = f.readlines()
    f.close()
    stack = []
    build_fs_tree(commands, stack)
    print(p11(stack[0]))
    print(p21(stack[0]))


