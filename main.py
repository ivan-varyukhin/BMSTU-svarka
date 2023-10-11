import sys
import pickle
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton


class PredictorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Загрузка модели из файла
        with open('model.pkl', 'rb') as file:
            self.model = pickle.load(file)

        self.setWindowTitle("Прогнозирование размеров сварного шва при электронно-лучевой сварке тонкостенных конструкций аэрокосмического назначения")

        self.iw_label = QLabel("Величина сварочного тока (IW):")
        self.iw_edit = QLineEdit()
        self.if_label = QLabel("Ток фокусировки электронного пучка (IF):")
        self.if_edit = QLineEdit()
        self.vw_label = QLabel("Скорость сварки (VW):")
        self.vw_edit = QLineEdit()
        self.fp_label = QLabel("Расстояние от поверхности образцов до электронно-оптической системы (FP):")
        self.fp_edit = QLineEdit()

        self.predict_button = QPushButton("Предсказать")
        self.predict_button.clicked.connect(self.predict)

        self.depth_label = QLabel("Глубина шва (Depth):")
        self.width_label = QLabel("Ширина шва (Width):")

        layout = QVBoxLayout()
        layout.addWidget(self.iw_label)
        layout.addWidget(self.iw_edit)
        layout.addWidget(self.if_label)
        layout.addWidget(self.if_edit)
        layout.addWidget(self.vw_label)
        layout.addWidget(self.vw_edit)
        layout.addWidget(self.fp_label)
        layout.addWidget(self.fp_edit)
        layout.addWidget(self.predict_button)
        layout.addWidget(self.depth_label)
        layout.addWidget(self.width_label)

        self.setLayout(layout)

    def predict(self):
        # Получение переменных от пользователя
        iw = float(self.iw_edit.text())
        if_ = float(self.if_edit.text())
        vw = float(self.vw_edit.text())
        fp = float(self.fp_edit.text())

        # Передача переменных в модель и получение результата
        depth, width = self.model.predict([[iw, if_, vw, fp]])[0]

        # Вывод результата
        self.depth_label.setText(f"Глубина шва (Depth): {depth}")
        self.width_label.setText(f"Ширина шва (Width): {width}")

        # Очистка полей ввода
        self.iw_edit.clear()
        self.if_edit.clear()
        self.vw_edit.clear()
        self.fp_edit.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PredictorApp()
    window.show()
    sys.exit(app.exec_())