from PySide6.QtWidgets import (QFrame, QPushButton, QLabel, QSpacerItem,
                               QHBoxLayout, QVBoxLayout, QSizePolicy)
from PySide6.QtCore import QSize, QRect, Qt
from PySide6.QtGui import QPixmap, QCursor
from icecream import ic
from database import Database

db = Database('database.db')

def island_area_task_update(self) -> None:
    tasks = db.get_tasks()
    # Создаем горизонтальный Frame, максимальная вместимость - 4 задания
    island_n = 1
    n = 0
    btns = []  # Список кнопок выполнений
    hl_name = "hL_island_tasks_frame_" + str(island_n)
    i_tasks_f_name = "island_tasks_frame_" + str(island_n)
    setattr(self, i_tasks_f_name, QFrame(self.island_tasks_area))
    getattr(self, i_tasks_f_name, 0).setObjectName(u"island_tasks_area")
    getattr(self, i_tasks_f_name, 0).setGeometry(QRect(0, 0, 600, 201))
    getattr(self, i_tasks_f_name, 0).setMinimumSize(QSize(600, 200))
    # getattr(self, i_tasks_f_name, 0).setStyleSheet(u"border: 1px solid #fff;")
    getattr(self, i_tasks_f_name, 0).setEnabled(True)
    setattr(self, hl_name, QHBoxLayout(getattr(self, i_tasks_f_name, 0)))
    getattr(self, hl_name).setObjectName(hl_name)
    self.verticalLayout_7.addWidget(getattr(self, i_tasks_f_name, 0))
    ic(getattr(self, hl_name))
    for task in tasks:
        if n == 4:
            island_n += 1
            hl_name = "hL_island_tasks_frame_" + str(island_n)
            i_tasks_f_name = "island_tasks_frame_" + str(island_n)
            setattr(self, i_tasks_f_name, QFrame(self.island_tasks_area))
            getattr(self, i_tasks_f_name, 0).setObjectName(u"island_tasks_area")
            getattr(self, i_tasks_f_name, 0).setGeometry(QRect(0, 0, 600, 201))
            getattr(self, i_tasks_f_name, 0).setMinimumSize(QSize(600, 200))
            # getattr(self, i_tasks_f_name, 0).setStyleSheet(u"border: 1px solid #fff;")
            getattr(self, i_tasks_f_name, 0).setEnabled(True)
            setattr(self, hl_name, QHBoxLayout(getattr(self, i_tasks_f_name, 0)))
            getattr(self, hl_name).setObjectName(u"hL_island_tasks_frame_" + str(island_n))
            self.verticalLayout_7.addWidget(getattr(self, i_tasks_f_name, 0))
            ic(getattr(self, hl_name))
            n = 0
        t_id = str(task[0])
        # Создаем Frame задания
        task_frame = QFrame(getattr(self, i_tasks_f_name, 0))
        task_frame.setObjectName(u"task_frame_" + t_id)
        task_frame.setEnabled(True)
        task_frame.setMinimumSize(QSize(150, 191))
        task_frame.setMaximumSize(QSize(150, 191))
        task_frame.setStyleSheet(u"background: #403C43;\n"
                                 u"border-radius: 5px;")
        task_frame.setFrameShape(QFrame.Shape.StyledPanel)
        task_frame.setFrameShadow(QFrame.Shadow.Raised)
        # Layout чтобы выровнить фрейм
        vl_task_frame = QVBoxLayout(task_frame)
        vl_task_frame.setObjectName(u"verticalLayout_10")
        # Если задание доступно (Проверка по уровню)
        # TODO: Сделать проверку по уровню
        # Создаем кнопку
        tbtn = f"task_{t_id}_start_btn"
        print(tbtn)
        setattr(self, tbtn, QPushButton(task_frame))
        getattr(self, tbtn, 0).setObjectName(tbtn)
        getattr(self, tbtn, 0).setText("Добывать")
        getattr(self, tbtn, 0).setFont(self.font_plump)
        getattr(self, tbtn, 0).setStyleSheet(u"color: #fff;")
        getattr(self, tbtn, 0).setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        getattr(self, tbtn, 0).setEnabled(True)
        print(getattr(self, tbtn, 0).clicked.connect(lambda checked, tid=t_id: self.start_task(tid)))
        vl_task_frame.addWidget(getattr(self, tbtn, 0))  # Добавляем кнопку в layout
        # Создаем название
        task_title = QFrame(task_frame)
        task_title.setObjectName(u"island_task_" + t_id + "_title")
        task_title.setEnabled(True)
        task_title.setMinimumSize(QSize(0, 30))
        task_title.setMaximumSize(QSize(16777215, 20))
        task_title.setFrameShape(QFrame.Shape.StyledPanel)
        task_title.setFrameShadow(QFrame.Shadow.Raised)
        hl_task_title = QHBoxLayout(task_title)
        hl_task_title.setObjectName(u"hL_island_t_t_" + t_id + "_title")
        # Создаем и добавляем спейсер
        hs_task_title = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        hl_task_title.addItem(hs_task_title)

        task_title_label = QLabel(task_frame)
        task_title_label.setObjectName(u"island_tasks_task_" + t_id + "_label")
        task_title_label.setText(task[1])
        task_title_label.setMinimumSize(QSize(0, 0))
        task_title_label.setMaximumSize(QSize(150, 16777215))
        task_title_label.setFont(self.font_dt)
        task_title_label.setStyleSheet(u"color: white;\n"
                                       u"background: none;")
        hl_task_title.addWidget(task_title_label)
        hs2_task_title = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        hl_task_title.addItem(hs2_task_title)

        vl_task_frame.addWidget(task_title)
        # Info задачки
        task_info = QLabel(task_frame)
        task_info.setObjectName(u"island_tasks_task_" + t_id + "_info")
        task_info.setText(f"{task[2]} очк. навыка / {task[3]}сек.")
        task_info.setEnabled(True)
        task_info.setFont(self.font_intro_bold)
        task_info.setStyleSheet(u"color: white;\nbackground: none;")
        task_info.setScaledContents(False)
        task_info.setAlignment(Qt.AlignmentFlag.AlignCenter)

        vl_task_frame.addWidget(task_info)

        # Создаем frame с картинкой
        task_img_frame = QFrame(task_frame)
        task_img_frame.setObjectName(u"island_tasks_task_" + t_id + "_img_frame")
        task_img_frame.setEnabled(True)
        task_img_frame.setMinimumSize(QSize(0, 63))
        task_img_frame.setFrameShape(QFrame.Shape.StyledPanel)
        task_img_frame.setFrameShadow(QFrame.Shadow.Raised)
        hl_task_img_frame = QHBoxLayout(task_img_frame)
        hl_task_img_frame.setObjectName(u"island_hL_tasks_task_" + t_id + "_img_frame")
        task_img_label = QLabel(task_img_frame)
        task_img_label.setObjectName(u"label_6")
        task_img_label.setMinimumSize(QSize(50, 50))
        task_img_label.setMaximumSize(QSize(50, 50))
        task_img_label.setPixmap(QPixmap(u":/images/gems/" + task[7]))
        task_img_label.setScaledContents(True)
        task_img_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        task_img_label.setWordWrap(False)

        hl_task_img_frame.addWidget(task_img_label)

        vl_task_frame.addWidget(task_img_frame, 0, Qt.AlignmentFlag.AlignVCenter)

        task_use_info_frame = QFrame(task_frame)
        task_use_info_frame.setObjectName(u"island_tasks_task_" + t_id + "_uses")
        task_use_info_frame.setStyleSheet(u"padding: 0;\n"
                                          u"margin: 0;")
        task_use_info_frame.setFrameShape(QFrame.Shape.StyledPanel)
        task_use_info_frame.setFrameShadow(QFrame.Shadow.Raised)
        hl_task_use_info = QHBoxLayout(task_use_info_frame)
        hl_task_use_info.setObjectName(u"hl_island_tasks_task_" + t_id + "_uses")
        hs_task_use_info = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        hl_task_use_info.addItem(hs_task_use_info)

        # --USES--
        self.task_use_info_label = QLabel(task_use_info_frame)
        self.task_use_info_label.setObjectName(u"island_tasks_task_" + t_id + "_uses_label")
        self.task_use_info_label.setText(f"{task[6]}/{task[5]}")
        self.task_use_info_label.setFont(self.font_intro_bold)
        self.task_use_info_label.setStyleSheet(u"color: #fff;")

        hl_task_use_info.addWidget(self.task_use_info_label)

        hs2_task_use_info = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        hl_task_use_info.addItem(hs2_task_use_info)

        vl_task_frame.addWidget(task_use_info_frame)
        getattr(self, hl_name, 0).addWidget(task_frame)

        n += 1

    # Добавляем спейсер в последний фрейм
    hs_tasks_frame_last = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
    getattr(self, hl_name).addItem(hs_tasks_frame_last)
    getattr(self, i_tasks_f_name, 0).show()
    # print(getattr(self, i_tasks_f_name, 0).children())

