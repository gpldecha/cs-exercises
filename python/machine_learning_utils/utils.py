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
    train_label = list()
    test_data = list()
    test_label = list()
    for i, label in enumerate(unique_labels):
        idx_label = np.where(labels == label)[0]
        if len(idx_label) <= num_test_samples_per_label:
            print('Warning there are {} labels and you want {} for your test set'.format(len(idx_label),
                                                                                         num_test_samples_per_label))
            test_data.append(data[idx_label, :])
            test_label.append(labels[idx_label])
        else:

            idx_test = idx_label[:num_test_samples_per_label]
            idx_train = idx_label[num_test_samples_per_label:]

            test_data.append(data[idx_test, :, :, :])
            train_data.append(data[idx_train, :, :, :])

            test_label.append(labels[idx_test])
            train_label.append(labels[idx_train])

    train_data = np.concatenate(train_data)
    train_label = np.concatenate(train_label)

    test_data = np.concatenate(test_data)
    test_label = np.concatenate(test_label)

    idx = np.arange(0, train_data.shape[0])
    np.random.shuffle(idx)

    train_data = train_data[idx, :, :, :]
    train_label = train_label[idx]

    idx = np.arange(0, test_data.shape[0])
    np.random.shuffle(idx)

    test_data = test_data[idx, :, :, :]
    test_label = test_label[idx]

    return train_data, train_label, test_data, test_label

