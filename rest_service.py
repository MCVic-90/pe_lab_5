from flask import Flask, request
import pickle

app = Flask(__name__)

path = 'C:\\Users\\MC_VIC\\Dropbox\\1 семестр\\ПИ\\лр4\\dictionary.pkl'


class AllWords:

    def __init__(self):
        self.words = []

    def pickle_read_file(self, path):
        f = open(path, 'rb')
        file = pickle.load(f)
        self.words = [i for i in file]

        return self.words


@app.route('/get_all', methods=['GET'])
def get_all():
    res = {'all_words': str(AllWords().pickle_read_file(path))}
    return res


if __name__ == '__main__':
    app.run(debug=True, port=5555)