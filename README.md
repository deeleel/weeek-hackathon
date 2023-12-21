# Хакатон МФТИ по Наукам о данных 12-2023
## Задача Weeek

* ./datasets - сохранены датасеты (как заказчика, так и наш)
* ./LSTM_classifier:
    * Код обучения LSTM-классификатора на основе датасета заказчика: *LSTM_Сlassifier_Train.ipynb*
    * Веса модели: *LSTM_classifier.pth*
    * Словарь (*vocab.json*) и целевые значения (*flipped_tasks.json*), на которых обучалась модель.
    * Код для запуска и тестирования обученной модели: *LSTM_Classifier_Usage_Example.ipynb*
* ./LSTM_NER:
    * Код обучения LSTM-модели для выделения именованных сущностей на основе нашего датасета: *LSTM_NER_Train.ipynb*
    * Веса модели: *LSTM_NER.pth*
    * Словарь (*vocab.json*) и целевые значения (*tag_to_ix.json*), на которых обучалась модель.
    * Код для запуска и тестирования обученной модели: *LSTM_NER_Usage_Example.ipynb*
* ./spacy - работа с разметой данных с помощью spacy
   * final_2 - ner модель для выделения объектов [person, time, task_type]
* ./DeepPavlov_NER - дообучение DeepPavlov по нашему NER-датасету
    * Код дообучения модели на нашем датасете: *DeepPavlov_NER.ipynb*
* ./ner_test - пробная модель NER на нескольких примерах от заказчика, сделанная до того, как быд получен датасет от заказчика

## Команда "Авоська и Небоська"
* Кайгородов Глеб Борисович
* Коряковцева Алёна Андреевна @AlyonaKor
* Граур Андрей Константинович @Graur
* Кудрявцева Полина Дмитриевна @pluie-d-automne
* Ли Диана Александровна @deeleel

## Презентация
https://docs.google.com/presentation/d/1GJ2eLmNa1yechN6k-K4Jj2d8aj7AswPm/edit?usp=sharing&ouid=118037884440268728238&rtpof=true&sd=true
