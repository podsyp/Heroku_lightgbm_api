def show_metrics(metrics):
    tmp = []
    for m in ['train', 'val', 'test']:
        tmp_ = []
        tmp_.append('Model: ' + str(metrics[m][0]))
        tmp_.append('Set: ' + str(metrics[m][1]))
        tmp_.append('R^2: ' + str(metrics[m][2]))
        tmp_.append('Mean Absolute Error: ' + str(metrics[m][3]))
        tmp_.append('Mean Squared Error: ' + str(metrics[m][4]))
        tmp_.append('Median Absolute Error: ' + str(metrics[m][5]))
        tmp_.append('Mean Squared Log Error: ' + str(metrics[m][6]))

        tmp.append(tmp_)
    return tmp
