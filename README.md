# python_tree
Displays the file tree and file stats from specified path.


## Install:
```shell
python setup.py install
```

## Run:

### Examples
```shell
python_tree --show-stats --show-tree
```
Show file tree and stats from current directory

```shell
python_tree
```
Show files in current directory

```shell
python_tree /path
```
Show files in /path

```shell
python_tree /path --show-stats
```
Show files and stats in /path


## Help
positional arguments:
  path

optional arguments:
  -h, --help    show this help message and exit
  --show-tree
  --show-stats
