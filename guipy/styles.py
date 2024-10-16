rank_progress_bar_styles = """
                            QProgressBar{
                                background-color: rgb(255, 255, 255);
                                border-radius: 10px;
                                color: transparent;
                            }
                            
                            QProgressBar::chunk{
                                border-radius: 10px;
                                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 
                                rgba(2, 97, 123, 255), stop:1 rgba(4, 177, 225, 255))
                            }
                            """
rank_progress_bar_styles_onclick = """
                            QProgressBar{
                                background-color: rgb(255, 255, 255);
                                border-radius: 10px;
                                color: transparent;
                            }
                            
                            QProgressBar::chunk{
                                border-radius: 10px;
                                background-color: rgba(43, 255, 114, 200);
                            }
                            """
