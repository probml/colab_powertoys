from .toys import toys
import os
class probml_toys():
    """docstring for probml_toys."""
    def __init__(self):
        os.environ["PYPROBML"] = '/pyprobml/'
    @staticmethod
    def save_fig(fname,verbose=False, *args, **kwargs):
        if "PYPROBML" in os.environ:
            root = os.environ["PYPROBML"]
            figdir = os.path.join(root, 'figures')
        else:
            figdir = '../figures' # default directory one above where code lives
        toys.save_fig(fname, figdir,verbose,*args, **kwargs)
    @staticmethod
    def git_ssh(git_command, email=None, username=None,
        verbose=False):
        toys.git_ssh(git_command, email,username,verbose)
    @staticmethod
    def show_image(img_path,*args, **kwargs):
      toys.show_image(img_path,*args, **kwargs)
    @staticmethod
    def show_and_run(script, i=True):
      toys.show_and_run(script,i)
        
p=probml_toys()
