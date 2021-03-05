from pathlib import Path
import pickle

def get_model(version):
    """ Function to get model """
    p = str(Path(__file__).parents[1])
    f = '/model/model_v' + str(version) + '.pkl'
    with open(p + f, 'rb') as model_path:
        model = pickle.load(model_path)

    return model
