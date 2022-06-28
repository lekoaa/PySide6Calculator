import sys;
from typing import Union, Optional;
from operator import add, sub, mul, truediv;

from PySide6.QtWidgets import QApplication, QMainWindow;
from PySide6.QtGui import QFontDatabase;

from window_design import Ui_MainWindow;

operations = {
    "+": add,
    "-": sub,
    "\u00d7": mul,
    "/": truediv
}

error_zero_div = 'Division by zero';
error_undefined = 'Result is undefined';

default_font_size = 20;
default_entry_font_size = 45;

class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self);

        self.entry = self.ui.le_entry;
        self.temp = self.ui.label_ans;
        self.entry_max_len = self.entry.maxLength();
        
        QFontDatabase.addApplicationFont("fonts/AnekLatin-Regular.ttf");

        # digits
        self.ui.button_0.clicked.connect(self.add_digit);
        self.ui.button_1.clicked.connect(self.add_digit);
        self.ui.button_2.clicked.connect(self.add_digit);
        self.ui.button_3.clicked.connect(self.add_digit);
        self.ui.button_4.clicked.connect(self.add_digit);
        self.ui.button_5.clicked.connect(self.add_digit);
        self.ui.button_6.clicked.connect(self.add_digit);
        self.ui.button_7.clicked.connect(self.add_digit);
        self.ui.button_8.clicked.connect(self.add_digit);
        self.ui.button_9.clicked.connect(self.add_digit);

        # actions
        self.ui.button_clear.clicked.connect(self.clear_all);
        self.ui.button_ce.clicked.connect(self.clear_entry);
        self.ui.button_dot.clicked.connect(self.add_dot);
        self.ui.button_negative.clicked.connect(self.negate);
        self.ui.button_backspace.clicked.connect(self.backspace);

        # math
        self.ui.button_equals.clicked.connect(self.calculate);
        self.ui.button_plus.clicked.connect(self.math_operation);
        self.ui.button_minus.clicked.connect(self.math_operation);
        self.ui.button_multiply.clicked.connect(self.math_operation);
        self.ui.button_divide.clicked.connect(self.math_operation);

    def add_digit(self) -> None:
        self.remove_error()
        self.clear_temp_if_equality()
        button = self.sender();
        
        digit_buttons = ('button_0', 'button_1', 'button_2', 'button_3', 'button_4',
                         'button_5', 'button_6', 'button_7', 'button_8', 'button_9');
        
        if button.objectName() in digit_buttons:
            if self.entry.text() == '0':
                self.entry.setText(button.text());
            else:
                self.entry.setText(self.entry.text() + button.text());
        
        self.adjust_entry_font_size();

    def add_dot(self) -> None:
        self.clear_temp_if_equality()
        if '.' not in self.entry.text():
            self.entry.setText(self.entry.text()+'.')
            self.adjust_entry_font_size();

    def negate(self) -> None:
        self.clear_temp_if_equality()
        entry = self.entry.text();

        if '-' not in entry:
            if entry != '0':
                entry = '-' + entry;
        else:
            entry = entry[1:];

        if len(entry) == self.entry_max_len + 1 and '-' in entry:
            self.entry.setMaxLength(self.entry_max_len + 1);
        else:
            self.entry.setMaxLength(self.entry_max_len);

        self.entry.setText(entry)
        self.adjust_entry_font_size();

    def backspace(self) -> None:
        self.remove_error()
        self.clear_temp_if_equality()
        entry = self.entry.text();

        if len(entry) != 1:
            if len(entry) == 2 and '-' in entry:
                self.entry.setText('0');
            else:
                self.entry.setText(entry[:-1]);
	    
        else:
            self.entry.setText('0');

        self.adjust_entry_font_size();
    
    def clear_all(self) -> None:
        self.remove_error()
        self.ui.le_entry.setText('0')
        self.adjust_entry_font_size()
        self.ui.label_ans.clear()
        self.adjust_temp_font_size();

    def clear_entry(self) -> None:
        self.remove_error()
        self.clear_temp_if_equality()
        self.ui.le_entry.setText('0')
        self.adjust_entry_font_size();

    def clear_temp_if_equality(self) -> None:
        if self.get_math_sign() == '=':
            self.ui.label_ans.clear()
            self.adjust_temp_font_size();
    
    @staticmethod
    def remove_trailing_zeros(num: str) -> str:
        n = str(float(num))
        return n.replace('.0', '') if n.endswith('.0') else n;

    def add_temp(self) -> None:
        button = self.sender()
        entry = self.remove_trailing_zeros(self.entry.text());

        if not self.ui.label_ans.text() or self.get_math_sign() == '=':
            self.ui.label_ans.setText(entry + f' {button.text()} ')
            self.adjust_temp_font_size()
            self.ui.le_entry.setText('0')
            self.adjust_entry_font_size();

    def get_entry_num(self) -> Union[int, float]:
        entry = self.entry.text().strip('.')
        return float(entry) if '.' in entry else int(entry);

    def get_temp_num(self) -> Union[int, float, None]:
        if self.ui.label_ans.text():
            temp = self.ui.label_ans.text().strip('.').split()[0]
            return float(temp) if '.' in temp else int(temp);

    def get_math_sign(self) -> Optional[str]:
        if self.ui.label_ans.text():
            return self.ui.label_ans.text().strip('.').split()[-1];

    def get_entry_text_width(self) -> int:
        return self.entry.fontMetrics().boundingRect(self.entry.text()).width();

    def get_temp_text_width(self) -> int:
        return self.ui.label_ans.fontMetrics().boundingRect(self.ui.label_ans.text()).width();

    def calculate(self) -> Optional[str]:
        entry = self.entry.text()
        temp = self.ui.label_ans.text();

        if temp:
            try:
                result = self.remove_trailing_zeros(str(operations[self.get_math_sign()](self.get_temp_num(), self.get_entry_num())))
                self.ui.label_ans.setText(temp + self.remove_trailing_zeros(entry) + ' =')
                self.adjust_temp_font_size()
                self.entry.setText(result)
                self.adjust_entry_font_size()
                return result;
            except KeyError:
                pass;
            except ZeroDivisionError:
                if self.get_temp_num() == 0:
                    self.show_error(error_undefined)
                else:
                    self.show_error(error_zero_div);

    def math_operation(self) -> None:
        temp = self.ui.label_ans.text();
        button = self.sender();

        if not temp:
            self.add_temp();

        else:
            if self.get_math_sign() != button.text():
                if self.get_math_sign() == '=':
                    self.add_temp();
                    
                else:
                    self.ui.label_ans.setText(temp[:-2] + f'{button.text()} ');
            else:
                try:
                    self.ui.label_ans.setText(self.calculate() + f' {button.text()} ');

                except TypeError:
                    pass;

            self.adjust_temp_font_size();

    def show_error(self, text: str) -> None:
        self.ui.le_entry.setMaxLength(self.entry_max_len)
        self.ui.le_entry.setText(text)
        self.adjust_entry_font_size()
        self.disable_buttons(True);

    def remove_error(self) -> None:
        if self.ui.le_entry.text() in (error_undefined, error_zero_div):
            self.ui.le_entry.setMaxLength(self.entry_max_len)
            self.ui.le_entry.setText('0')
            self.adjust_entry_font_size()
            self.disable_buttons(False);

    def disable_buttons(self, disable: bool) -> None:
        self.ui.button_equals.setDisabled(disable)
        self.ui.button_plus.setDisabled(disable)
        self.ui.button_minus.setDisabled(disable)
        self.ui.button_multiply.setDisabled(disable)
        self.ui.button_divide.setDisabled(disable)
        self.ui.button_negative.setDisabled(disable)
        self.ui.button_dot.setDisabled(disable);

        color = 'color: #888;' if disable else 'color: white;'
        self.change_buttons_color(color);

    def change_buttons_color(self, css_color: str) -> None:
        self.ui.button_equals.setStyleSheet(css_color)
        self.ui.button_plus.setStyleSheet(css_color)
        self.ui.button_minus.setStyleSheet(css_color)
        self.ui.button_multiply.setStyleSheet(css_color)
        self.ui.button_divide.setStyleSheet(css_color)
        self.ui.button_negative.setStyleSheet(css_color)
        self.ui.button_dot.setStyleSheet(css_color);

    def adjust_entry_font_size(self) -> None:
        font_size = default_entry_font_size

        while self.get_entry_text_width() > self.entry.width() - 15:
            font_size -= 1
            self.entry.setStyleSheet('font-size: ' + str(font_size) + 'pt; border: none;');

        font_size = 1

        while self.get_entry_text_width() < self.entry.width() - 60:
            font_size += 1

            if font_size > default_entry_font_size:
                break;

            self.entry.setStyleSheet('font-size: ' + str(font_size) + 'pt; border: none;');

    def adjust_temp_font_size(self) -> None:
        font_size = default_font_size

        while self.get_temp_text_width() > self.ui.label_ans.width() - 10:
            font_size -= 1
            self.ui.label_ans.setStyleSheet('font-size: ' + str(font_size) + 'pt; color: #888;');

        font_size = 1

        while self.get_temp_text_width() < self.ui.label_ans.width() - 60:
            font_size += 1

            if font_size > default_font_size:
                break;

            self.ui.label_ans.setStyleSheet('font-size: ' + str(font_size) + 'pt; color: #888;');

    def resizeEvent(self, event) -> None:
        self.adjust_entry_font_size()
        self.adjust_temp_font_size();


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Calculator()
    window.show()

    sys.exit(app.exec());