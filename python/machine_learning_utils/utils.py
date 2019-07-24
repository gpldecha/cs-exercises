import pickle
import numpy as np


def load_data(file):
    try:
        with open(file, 'rb') as fo:
            return pickle.load(fo, encoding='bytes')
    except IOError:
        print('Unable to read file: {}'.format(file))
        return None


def split_test_train(test_percentage, data, labels):
    num_samples = data.shape[0]
    unique_labels = np.unique(labels)
    num_labels = len(unique_labels)
    num_test_samples = int(num_samples*test_percentage)
    num_test_samples_per_label = int(num_test_samples/num_labels)
    train_data = list()
    test_data = list()
    for i, label in enumerate(unique_labels):
        idx_label = np.where(labels == label)[0]
        if len(idx_label) <= num_test_samples_per_label:
            print('Warning there are {} labels and you want {} for your test set'.format(len(idx_label),
                                                                                         num_test_samples_per_label))
            test_data.append(data[idx_label, :])
        else:
            idx_test = idx_label[:num_test_samples_per_label]
            idx_train = idx_label[num_test_samples_per_label:]
            test_data.append(data[idx_test, :, :, :])
            train_data.append(data[idx_train, :, :, :])

    train_data = np.concatenate(train_data)
    test_data = np.concatenate(test_data)

    np.random.shuffle(train_data)
    np.random.shuffle(test_data)

    return train_data, test_data

