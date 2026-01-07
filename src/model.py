import torch
import torch.nn as nn
import torch.nn.functional as F


class TabularNet(nn.Module):
    def __init__(self, input_dim):
        super().__init__()
        self.fc1 = nn.Linear(input_dim, 64)
        self.fc2 = nn.Linear(64, 32)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        return x


class ImageNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 16, 3, padding=1)
        self.conv2 = nn.Conv2d(16, 32, 3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)

        self.fc = nn.Linear(32 * 64 * 64, 64)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(x.size(0), -1)
        x = F.relu(self.fc(x))
        return x


class MultimodalNet(nn.Module):
    def __init__(self, tabular_dim):
        super().__init__()
        self.tabular_net = TabularNet(tabular_dim)
        self.image_net = ImageNet()

        self.fc1 = nn.Linear(32 + 64, 64)
        self.fc2 = nn.Linear(64, 1)

    def forward(self, tabular, image):
        t = self.tabular_net(tabular)
        i = self.image_net(image)

        x = torch.cat([t, i], dim=1)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x
