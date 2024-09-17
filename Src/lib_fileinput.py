import pandas as pd
import matplotlib.pyplot as mpimg 
import sys 

is_windows = sys.platform.startswith('win')


if is_windows:
    filename_ytrain = "..\\Data\\Y_train_CVw08PX.csv"
    filename_Xtrain = "..\\Data\\X_train_update.csv"
    filename_Xtest = "..\\Data\\X_test_update.csv"
else:
    filename_ytrain = "../Data/Y_train_CVw08PX.csv"
    filename_Xtrain = "../Data/X_train_update.csv"
    filename_Xtest = "../Data/X_test_update.csv"



def get_xtrain():
    X_train = pd.read_csv(filename_Xtrain, index_col=0)
    return X_train

def get_ytrain():
    y_train = pd.read_csv("../Data/Y_train_CVw08PX.csv", index_col=0)
    return y_train

def get_xtest():
    X_test = pd.read_csv(filename_Xtest, index_col=0)
    return X_test

def clean_text(text):
    if pd.isna(text):
        return str('')
    soup = BeautifulSoup(text, 'html.parser')
    tmp = soup.getText()
    tmp = unidecode(tmp)
    return re.sub(r'[^a-zA-Z0-9]+', ' ', tmp)


def get_image(product_id, image_id, type):
    """ 
    Fonction Pour récupérer le tableau correspondant à l'image product_id et image_id
    - product_id : type int 
    - image_id : type int
    - type = 'train' ou 'test'
    """
    filename = 'image' + '_' + str(image_id) + '_' + 'product' + '_' + str(product_id)+'.jpg'
    ### pathname dépend de l'arborescence locale où sont stockées les images (hors repo Github)
    if (type!='train') and (type!='test'):
        return []
    pathname = "../../Images/image_" + type + "/"
    img = mpimg.imread(pathname+filename)
    return img


def get_size_image(product_id, image_id, type):
    """
    return the size (x,y) of the image referred by product_id & image_id 
    input type must be 'train' or 'test'
    """
    img = get_image(product_id, image_id, type)
    if len(img) == 0:
        return [0,0]
    return [img.shape[0], img.shape[1]]