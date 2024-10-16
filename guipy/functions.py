from PySide6.QtWidgets import (QFrame, QPushButton, QLabel, QSpacerItem,
                               QHBoxLayout, QVBoxLayout, QSizePolicy, QGraphicsBlurEffect)
from PySide6.QtCore import QSize, QRect, Qt
from PySide6.QtGui import QPixmap, QCursor, QFont
from database import Database

db = Database('database.db')

# OPEN PAGES
def open_menu(self) -> None:
    self.stackedWidget.setCurrentWidget(self.island_page)
    self.stackedWidget_2.setCurrentWidget(self.island_page_2)
    self.activate_btn()
    # Обновляем переменные
    island_area_task_update(self)
    self.island_page_data_update()


def open_shop(self) -> None:
    self.stackedWidget_2.setCurrentWidget(self.shop_page)
    self.activate_btn()
    self.tasks_check()


def open_backpack(self) -> None:
    self.stackedWidget_2.setCurrentWidget(self.backpack_page)
    self.activate_btn()
    self.tasks_check()


def open_island(self) -> None:
    self.stackedWidget_2.setCurrentWidget(self.island_page_2)
    self.activate_btn()
    self.tasks_check()
    island_area_task_update(self)
    self.island_page_data_update()


def island_area_task_update(self) -> None:
    tasks = db.get_tasks()
    user_info = db.get_user_info()
    # Создаем горизонтальный Frame, максимальная вместимость - 4 задания
    island_n = 1
    n = 0
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
    getattr(self, hl_name).setContentsMargins(-1, 0, -1, 0)
    self.verticalLayout_7.addWidget(getattr(self, i_tasks_f_name, 0))
    self.verticalLayout_7.setContentsMargins(-1, 0, -1, 0)
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
        vl_task_frame.setContentsMargins(5, 3, 5, 4)
        # Если задание доступно (Проверка по уровню)
        # Создаем кнопку
        if user_info[2] < task[4]:
            task_close_frame = QFrame(task_frame)
            task_close_frame.setObjectName(u"island_tasks_task_" + t_id + "_close_f")
            task_close_frame.setStyleSheet(u"background: none;\n")
            task_close_frame.setFrameShape(QFrame.Shape.StyledPanel)
            task_close_frame.setFrameShadow(QFrame.Shadow.Raised)
            task_close_frame.setMaximumSize(QSize(150, 50))
            task_close_frame.setContentsMargins(0, 0, 0, 0)

            hl_task_close_frame = QHBoxLayout(task_close_frame)
            hl_task_close_frame.setObjectName(u"hl_island_tasks_task_" + t_id + "_uses")
            hs_task_close_frame = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
            hl_task_close_frame.addItem(hs_task_close_frame)

            task_close_title = QLabel(task_close_frame)
            task_close_title.setObjectName(u"island_tasks_task_" + t_id + "_label")
            task_close_title.setText("Закрыто")
            task_close_title.setFont(self.font_intro_bold)
            task_close_title.setStyleSheet(u"color: white;\n"
                                           u"background: none;")
            hl_task_close_frame.addWidget(task_close_title)
            hs2_task_close_frame = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
            hl_task_close_frame.addItem(hs2_task_close_frame)
            hl_task_close_frame.setContentsMargins(0, 0, 0, 0)
            vl_task_frame.addWidget(task_close_frame)

        else:
            tbtn = f"task_{t_id}_start_btn"
            setattr(self, tbtn, QPushButton(task_frame))
            getattr(self, tbtn, 0).setObjectName(tbtn)
            getattr(self, tbtn, 0).setText("Добывать")
            getattr(self, tbtn, 0).setFont(self.font_plump)
            getattr(self, tbtn, 0).setStyleSheet(u"color: #fff;")
            getattr(self, tbtn, 0).setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            getattr(self, tbtn, 0).setEnabled(True)
            getattr(self, tbtn, 0).clicked.connect(lambda checked, tid=t_id: self.start_task(tid))
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
        hl_task_title.setContentsMargins(-1, 0, -1, 0)

        vl_task_frame.addWidget(task_title)
        # Info задачки
        task_info = QLabel(task_frame)
        task_info.setObjectName(u"island_tasks_task_" + t_id + "_info")
        task_info.setFont(self.font_intro_bold)
        if user_info[2] < task[4]:
            font_vopros = QFont()
            font_vopros.setFamilies([u"a_Concepto"])
            font_vopros.setPointSize(14)
            task_info.setText(f"???")
            task_info.setFont(font_vopros)
        else:
            task_info.setText(f"{task[2]} очк. навыка / {task[3]}сек.")
        task_info.setEnabled(True)
        task_info.setStyleSheet(u"color: white;\nbackground: none;")
        task_info.setScaledContents(False)
        task_info.setAlignment(Qt.AlignmentFlag.AlignCenter)

        vl_task_frame.addWidget(task_info)

        # Создаем frame с картинкой
        t_img_f = u"island_tasks_task_" + t_id + "_img_frame"
        setattr(self, t_img_f, QFrame(task_frame))
        getattr(self, t_img_f, 0).setObjectName(t_img_f)
        getattr(self, t_img_f, 0).setEnabled(True)
        getattr(self, t_img_f, 0).setMinimumSize(QSize(0, 50))
        getattr(self, t_img_f, 0).setFrameShape(QFrame.Shape.NoFrame)
        getattr(self, t_img_f, 0).setFrameShadow(QFrame.Shadow.Raised)
        hl_t_img_f = f"hl_task_{t_id}_img_frame"
        setattr(self, hl_t_img_f, QHBoxLayout(getattr(self, t_img_f, 0)))
        getattr(self, hl_t_img_f, 0).setObjectName(f"hl_task_{t_id}_img_frame")
        getattr(self, hl_t_img_f, 0).setContentsMargins(-1, 2, -1, 2)
        timg_label = f"task_{t_id}_img_label"
        setattr(self, timg_label, QLabel(getattr(self, t_img_f, 0)))
        getattr(self, timg_label, 0).setObjectName(f"task_{t_id}_img_label")
        getattr(self, timg_label, 0).setMinimumSize(QSize(50, 50))
        getattr(self, timg_label, 0).setMaximumSize(QSize(50, 50))
        getattr(self, timg_label, 0).setPixmap(QPixmap(u":/images/gems/" + task[7]))
        getattr(self, timg_label, 0).setScaledContents(True)
        getattr(self, timg_label, 0).setAlignment(Qt.AlignmentFlag.AlignCenter)
        if user_info[2] < task[4]:
            setattr(self, f"task_{t_id}_blur_img", QGraphicsBlurEffect())
            getattr(self, f"task_{t_id}_blur_img", 0).setBlurRadius(15)
            getattr(self, timg_label, 0).setGraphicsEffect(getattr(self, f"task_{t_id}_blur_img", 0))

        getattr(self, hl_t_img_f, 0).addWidget(getattr(self, timg_label, 0))

        vl_task_frame.addWidget(getattr(self, t_img_f, 0), 0, Qt.AlignmentFlag.AlignVCenter)

        task_use_info_frame = QFrame(task_frame)
        task_use_info_frame.setObjectName(u"island_tasks_task_" + t_id + "_uses")
        task_use_info_frame.setStyleSheet(u"background: none;\n")
        task_use_info_frame.setFrameShape(QFrame.Shape.StyledPanel)
        task_use_info_frame.setFrameShadow(QFrame.Shadow.Raised)

        hl_task_use_info = QHBoxLayout(task_use_info_frame)
        hl_task_use_info.setObjectName(u"hl_island_tasks_task_" + t_id + "_uses")
        hs_task_use_info = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        hl_task_use_info.addItem(hs_task_use_info)
        hl_task_use_info.setContentsMargins(-1, 0, -1, 0)

        # --USES--
        i_t_use_label = f"island_tasks_task_{t_id}_uses_label"
        setattr(self, i_t_use_label, QLabel(task_use_info_frame))
        getattr(self, i_t_use_label, 0).setObjectName(u"island_tasks_task_" + t_id + "_uses_label")
        if user_info[2] >= task[4]:
            getattr(self, i_t_use_label, 0).setText(f"{task[6]}/{task[5]}")
        else:
            getattr(self, i_t_use_label, 0).setText(f"Требуется уровень {task[4]}")
            task_use_info_frame.setStyleSheet(u"background-color: "
                                              u"qlineargradient(spread:pad, x1:0, y1:0.131, x2:1, y2:0.864, "
                                              u"stop:0 rgba(255, 47, 47, 200), stop:1 rgba(255, 53, 53, 200));\n")

        getattr(self, i_t_use_label, 0).setFont(self.font_intro_bold)
        getattr(self, i_t_use_label, 0).setStyleSheet("color: #fff;\nbackground: none;\n")

        hl_task_use_info.addWidget(getattr(self, i_t_use_label, 0))

        hs2_task_use_info = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        hl_task_use_info.addItem(hs2_task_use_info)

        vl_task_frame.addWidget(task_use_info_frame)
        getattr(self, hl_name, 0).addWidget(task_frame)

        n += 1

    # Добавляем спейсер в последний фрейм
    hs_tasks_frame_last = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
    getattr(self, hl_name).addItem(hs_tasks_frame_last)
    getattr(self, i_tasks_f_name, 0).show()

