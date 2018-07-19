import json
import sys
class Notebook:
    def __init__(self, path):
        self.path = path
        with open(self.path) as notebook:
            notebook_str = notebook.read()
            self.json = json.loads(notebook_str)
    def __getitem__(self, index):
        cells = self.json['cells']
        return cells[index]
    def __add__(self,another):
        if not isinstance(another, Notebook):
            another = Notebook(another)
        else:
            target_nb = {}
            cells_lst = self.json['cells'] + another.json['cells']
            target_nb['cells'] = cells_lst
            del another.json['cells']
            target_nb.update(another.json)
            target_str = json.dumps(target_nb)
            target = open('target_notebook_class.ipynb', 'w')
            target.write(target_str)
if len(sys.argv) < 3:
    raise Exception('参数数量必须大于 2！')
for item in sys.argv[1:]:
    if "ipynb" not in item:
       raise Exception("参数必须为ipynb文件！")
notebook_path_lst = sys.argv[1:]
nb1 = Notebook(notebook_path_lst[0])
nb2 = Notebook(notebook_path_lst[1])
nb1 + nb2