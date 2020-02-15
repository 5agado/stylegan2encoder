import os


class Config:
    BASE_PATH = 'C:/Users/User/Documents/models/stylegan2'

    @staticmethod
    def get_vgg16_path():
        pkl_name = 'vgg16.pkl'
        #return 'http://d36zk2xti64re0.cloudfront.net/stylegan1/networks/metrics/vgg16.pkl'
        return os.path.join(Config.BASE_PATH, pkl_name)

    @staticmethod
    def get_vgg16_perceptual_path():
        pkl_name = 'vgg16_zhang_perceptual.pkl'
        #return 'http://d36zk2xti64re0.cloudfront.net/stylegan1/networks/metrics/vgg16_zhang_perceptual.pkl'
        return os.path.join(Config.BASE_PATH, pkl_name)

    @staticmethod
    def get_inception_features_path():
        pkl_name = 'inception_v3_features.pkl'
        #return 'http://d36zk2xti64re0.cloudfront.net/stylegan1/networks/metrics/inception_v3_features.pkl'
        return os.path.join(Config.BASE_PATH, pkl_name)

    @staticmethod
    def get_inception_softmax_path():
        pkl_name = 'inception_v3_softmax.pkl'
        #return 'http://d36zk2xti64re0.cloudfront.net/stylegan1/networks/metrics/inception_v3_softmax.pkl'
        return os.path.join(Config.BASE_PATH, pkl_name)
