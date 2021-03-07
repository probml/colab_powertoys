
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
    def show_image(img_path,size=None,ratio=None):
        if not size:
            size=[0,600]
        img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
        img=toys.image_resize(img,height=size[1])
        if ratio:
            img=cv2.resize(img,size,fx=ratio[0],fy=ratio[1])
        cv2_imshow(img)


    @staticmethod
    def show_and_run(script, i=True):
        sar(script, i)
    @staticmethod
    def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
        # From https://stackoverflow.com/questions/44650888/resize-an-image-without-distortion-opencv
        # initialize the dimensions of the image to be resized and
        # grab the image size
        dim = None
        (h, w) = image.shape[:2]

        # if both the width and height are None, then return the
        # original image
        if width is None and height is None:
            return image

        # check to see if the width is None
        if width is None:
            # calculate the ratio of the height and construct the
            # dimensions
            r = height / float(h)
            dim = (int(w * r), height)

        # otherwise, the height is None
        else:
            # calculate the ratio of the width and construct the
            # dimensions
            r = width / float(w)
            dim = (width, int(h * r))

        # resize the image
        resized = cv2.resize(image, dim, interpolation = inter)

        # return the resized image
        return resized


