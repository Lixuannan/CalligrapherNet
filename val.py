import os
import sys

import torch
import torch.nn
from torchvision import transforms, datasets
from tqdm import tqdm

from model import VGG

batch_size = 5

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print("using {} device".format(device))

net = VGG(num_classes=5).to(device=device)
weights_path = "/Users/meizhenchen/Downloads/CalligrapherNet.pth"
assert os.path.exists(weights_path), "file: '{}' dose not exist.".format(weights_path)
net.load_state_dict(torch.load(weights_path, map_location=device))

data_transform = {
    "train": transforms.Compose([transforms.RandomResizedCrop(224),
                                 transforms.RandomHorizontalFlip(),
                                 transforms.ToTensor(),
                                 transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))]),
    "val": transforms.Compose([transforms.Resize((224, 224)),
                               transforms.ToTensor(),
                               transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])}

validate_dataset = datasets.ImageFolder(root="dataset/val/",
                                        transform=data_transform["val"])
val_num = len(validate_dataset)
validate_loader = torch.utils.data.DataLoader(validate_dataset,
                                              batch_size=batch_size, shuffle=False,
                                              num_workers=0)

net.eval()
acc = 0.0
with torch.no_grad():
    val_bar = tqdm(validate_loader, file=sys.stdout)
    for val_data in val_bar:
        val_images, val_labels = val_data
        outputs = net(val_images.to(device))
        predict_y = torch.max(outputs, dim=1)[1]
        acc += torch.eq(predict_y, val_labels.to(device)).sum().item()

val_accurate = acc / val_num
print('val_accuracy: %.3f' % val_accurate)


