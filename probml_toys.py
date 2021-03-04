from toys import toys
import os
class probml_toys(object):
    """docstring for probml_toys."""
    def __init__(self, arg):
        pass
    @staticmethod
    def save_fig(fname,verbose=False, *args, **kwargs):
        if "PYPROBML" in os.environ:
            root = os.environ["PYPROBML"]
            figdir = os.path.join(root, 'figures')
        else:
            figdir = '../figures' # default directory one above where code lives
        toys.save_fig(fname, figdir,verbose,*args, **kwargs)
    @staticmethod
    def git_ssh(git_command, email="murphyk@gmail.com", username="probml",
        verbose=False):
        toys.git_ssh(git_command, email,username,verbose)
    @staticmethod
    def show_image(img_path,size=600):
      toys.show_image(img_path,size)
    @staticmethod
    def show_and_run(script, i=True):
      import inspect
      #print(toys)
      #print(inspect.getmembers(toys))
      toys.show_and_run(script,i)