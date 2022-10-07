from IPython import get_ipython
ipython = get_ipython()

ipython.run_line_magic("load_ext", "autoreload")
ipython.run_line_magic("autoreload", "2")
