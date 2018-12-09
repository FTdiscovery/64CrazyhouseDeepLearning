import torch
import numpy as np
import torch.nn as nn
import torch.utils.data as data_utils
from ChessConvNet import ChessConvNet
from PolicyDataset import PolicyDataset
import ChessResNet
import h5py

# inputs and outputs are numpy arrays. This method of checking accuracy only works with imported games.
# if it's not imported, accuracy will never be 100%, so it will just output the trained network after 10,000 epochs.
def validateNetwork(loadDirectory):

    with h5py.File('Training Data/18-10PolicyOutputs.h5', 'r') as hf:
        actions = hf["Outputs"][0:50000]
        print(len(actions))
    with h5py.File('Training Data/18-10Inputs.h5', 'r') as hf:
        inputs = hf["Inputs"][0:50000]
        print(len(inputs))
    actions = torch.from_numpy(actions)
    data = PolicyDataset(inputs, actions)

    testLoader = torch.utils.data.DataLoader(dataset=data, batch_size=16, shuffle=False)
    # to create a prediction, create a new dataset with input of the states, and output should just be np.zeros()

    try:
        model = torch.load(loadDirectory)
    except:
        print("Pretrained NN model not found!")

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model.eval()  # eval mode
    with torch.no_grad():
        correct = 0
        total = 0
        for images, labels in testLoader:
            images = images.to(device)
            labels = labels.to(device)
            outputs = model(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            _, labels = torch.max(labels.data, 1)
            correct += (predicted == labels).sum().item()

            print('Test Accuracy of the model on', total, 'test positions: {} %'.format(100 * correct / total))

validate = True
if validate:
    validateNetwork("18051810-POLICY.pt")





