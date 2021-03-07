
import os
import matplotlib.pyplot as plt
import nbimporter
from magic import show_and_run as sar
from google.colab import files
from google.colab.patches import cv2_imshow
import cv2


DISCLAIMER = 'WARNING : Editing in VM - changes lost after reboot!!'

class toys():
    """docstring for toys."""
    def __init__(self):
        pass
    @staticmethod
    def save_fig(fname, figdir,verbose=False,*args, **kwargs):
        '''Save current plot window to the figures directory.
        Authors: Mahmoud Soliman <mjs@aucegypt.edu> and Kevin Murphy <murphyk@gmail.com>
        '''
        if not os.path.exists(figdir):
            os.mkdir(figdir)
        fname_full = os.path.join(figdir, fname)
        if verbose:
            print('saving image to {}'.format(fname_full))
        plt.tight_layout()
        plt.savefig(fname_full, *args, **kwargs)
    @staticmethod
    def git_ssh(git_command, email, username,
            verbose=False):
        '''Execute a git command via ssh from colab.
        Authors: Mahmoud Soliman <mjs@aucegypt.edu> and Kevin Murphy <murphyk@gmail.com>
        '''
        git_command=git_command.replace(r"https://github.com/","git@github.com:")
        print('executing command via ssh:', git_command)
        # copy keys from drive to local .ssh folder
        if verbose:
            print('Copying keys from gdrive to local VM')
        os.system('rm -rf ~/.ssh')
        os.system('mkdir ~/.ssh')
        os.system('cp  -r /content/drive/MyDrive/ssh/* ~/.ssh/')
        os.system('ssh-keyscan -t rsa github.com >> ~/.ssh/known_hosts')
        os.system('ssh -T git@github.com') # test
        # git commands
        if verbose:
            print('Executing git commands')
        os.system('git config --global user.email {}'.format(email))
        os.system('git config --global user.name {}'.format(username))
        os.system(git_command)
        # cleanup
        if verbose:
            print('Cleanup local VM')
        os.system('rm -r ~/.ssh/')
        os.system('git config --global user.email ""')
        os.system('git config --global user.name ""')
    @staticmethod
    def show_image(img_path,size=None,ratio=(0.5,0.5)):

        img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
        img=cv2.resize(img,size,fx=ratio[0],fy=ratio[1])
        cv2_imshow(img)


    @staticmethod
    def show_and_run(script, i=True):
        sar(script, i)


