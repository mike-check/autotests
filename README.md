# UI autotests for nps server

### Test scenarios
| № | Test case |	Status |	Comment |
| ------------- | ------------- | ------------- | ------------- |
1|Открыть страницу с неустановленным cookie пользователем, которому требуется показывать всплывающее окно. Проверить, что cookie NPS_sended установлен корректно после открытия окна, всплывающее окно должно отобразиться| [PASSED]| test_cookies_after_rate |
2|Открыть страницу с неустановленным cookie пользователем, которому не требуется показывать всплывающее окно. Проверить, что cookie NPS_sended установлен корректно после открытия окна, всплывающее окно не должно отобразиться|[PASSED]| 
3|Открыть страницу с установленным cookie, запрещающая отображение всплывающего окна. Проверить , что всплывающее окно не отобразилось| [PASSED]|
4|Открыть страницу с отображенным всплывающим окном. Проверить внешний вид всплывающего окна на соответствие дизайну и текстам надписей|[FAILED]| test_check_welcome_label, test_check_like_label, test_check_dislike_label. Не соответствует заголовок, пропущен артикль “a”
5|Проверить пункт 4 при различных размерах окна|[PASSED]| 
6|Открыть страницу с отображенным всплывающим окном. Проверить что при нажатии на кнопки от 0 до 6 появляется поле для ввода комментария|[FAILED]| test_check_rate_buttons. Не появляется для оценки 6
7|Открыть страницу с отображенным всплывающим окном. Проверить что при нажатии на кнопки от 7 до 10 не появляется поле для ввода комментария|[PASSED]| test_check_rate_buttons|
8|Открыть страницу с отображенным всплывающим окном. Перейти к вводу комментария. В режиме Networking с установленным флагом “Persist Logs” проверить, что комментарий с разрешенной длиной корректно отправлен (в требованиях нет ни слова о длине и содержимом комментария, длина комментария может быть от 0 до 255 символов, в противном случае ошибка)|[PASSED]| test_send_feedback|
9|Открыть страницу с отображенным всплывающим окном. Перейти к вводу комментария. Проверить окно ввода на соответствие дизайну и текстам надписей|[PASSED]| test_check_feedback_label |
10|В режиме Networking с установленным флагом “Persist Logs” проверить корректность HTTP запроса в случае оценки от 0 до 6 (метод и endpoint должны соответствовать указанным в документации, поле user_action должно соответствовать проставленной оценке, в поле feedback должен быть текстовый комментарий, который указал пользователь. В идеале проверить соответствие типов и кодировок для строчного типа)|[PASSED]| 
11|Аналогично предыдущему пункту в режиме Networking с установленным флагом “Persist Logs” проверить корректность HTTP запроса в случае оценки от 7 до 10|[PASSED]| 
12|Проверить response от сервера на post запросы в случае любой оценки [PASSED]| 
13|Закрыть всплывающее окно на этапе выбора оценки, на этапе ввода фидбека. Проверить, что ничего не послалось серверу.|[PASSED]| test_close_window| 
14|Проверить, что всплывающее окно показывается только каждому 10-му пользователю|[PASSED]| 


### Install 
For correct tests exercution you need to have `python` v. 3.6+. For install requirements run

`pip install -r requirements.txt`

### Run
Command to run tests:

`$ py.test -s -v --driver=Chrome --html=report/index.html tests/`

Only Chrome and Firefor browsers are supported.

### Report
Report `index.html` will be in `report` folder. Example is [here](http://htmlpreview.github.io/?https://github.com/mike-check/autotests/blob/master/report/index.html).
