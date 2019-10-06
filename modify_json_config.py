import json, sys
import notebook.auth
from os.path import isdir, isfile, expanduser, dirname
from collections import defaultdict

def update_jupyter_password(path, hashed_pw ):
#   config_dir = dirname(path)
#   if not isdir(config_dir): makedirs(config_dir)
    d = defaultdict ( dict )
    try:
        with open(path,'r') as f:
            d.update (json.load(f))
    except: pass
    d["NotebookApp"]["password"] = hashed_pw
    with open(path,'w') as f:
        json.dump(d, f, indent = 2)

#=============================================================================

hashString = notebook.auth.passwd(sys.argv[1])

update_jupyter_password( 
   expanduser("~/.jupyter/jupyter_notebook_config.json"),
   hashString
)
