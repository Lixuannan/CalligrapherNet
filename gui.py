import sys

import torch
from PIL import Image
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QFileDialog, QWidget, QApplication
from torchvision import transforms

from model import VGG
from ui import Ui_Window


class Main(Ui_Window):
    def __init__(self):
        self.file = ""
        self.class_indict = {
            "0": "草书",
            "1": "楷书",
            "2": "隶书",
            "3": "行书",
            "4": "篆书"
        }
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        self.data_transform = transforms.Compose(
            [transforms.Resize((224, 224)),
             transforms.ToTensor(),
             transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
        self.model = VGG(num_classes=5).to(self.device)
        self.weights_path = "./CalligrapherNet.pth"
        self.model.load_state_dict(torch.load(self.weights_path, map_location=self.device))

    def setupAll(self, form):
        self.setupUi(form)
        self.choose_photo_button.clicked.connect(self.get_file)
        self.run_button.clicked.connect(self.run)

    def get_file(self):
        self.file, _ = QFileDialog.getOpenFileName(self.widget)
        pixmap = QPixmap(self.file).scaled(self.photo_view.size())
        self.photo_view.setPixmap(pixmap)

    def run(self):
        img = Image.open(self.file)
        img = self.data_transform(img)
        img = torch.unsqueeze(img, dim=0)

        self.model.eval()
        with torch.no_grad():
            output = torch.squeeze(self.model(img.to(self.device))).cpu()
            predict = torch.softmax(output, dim=0)

        ans = "计算结果："
        for i in range(len(predict)):
            ans += "{} {} % ".format(self.class_indict[str(i)], int(predict[i].numpy() * 100))

        self.result_lable.setText(ans)


if __name__ == "__main__":
    main = Main()
    app = QApplication()
    weight = QWidget()
    main.setupAll(weight)
    weight.show()
    sys.exit(app.exec())
