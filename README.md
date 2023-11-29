# Детекция дорожных знаков на видеорегистраторе

![Alt Text](assets/demonstration_gif.gif)


<div align="center">
    
  <a href="https://github.com/Svyatocheck/DeepLearningPractice/issues">![GitHub issues](https://img.shields.io/github/issues/Svyatocheck/DeepLearningPractice/issues)</a>
  <a href="https://github.com/Svyatocheck/DeepLearningPractice/blob/master/LICENSE">![GitHub license](https://img.shields.io/github/license/Svyatocheck/DeepLearningPractice?color=purple)</a>
  <a href="https://github.com/psf/black">![Code style](https://img.shields.io/badge/code%20style-black-black)</a>
    
</div>

### Stack: 

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://github.com/Vladimir-Dimitrov-Ngu)
[![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)](https://github.com/Vladimir-Dimitrov-Ngu)
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Vladimir-Dimitrov-Ngu)
[![Streamlit](https://img.shields.io/badge/streamlit-%23white.svg?style=for-the-badge&logo=streamlit&logoColor=white)](https://github.com/Vladimir-Dimitrov-Ngu)
[![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)](https://github.com/Vladimir-Dimitrov-Ngu)
[![Yolo](https://img.shields.io/badge/Yolo-%23EE4C2C.svg?style=for-the-badge&logo=Yolo&logoColor=white)](https://github.com/Vladimir-Dimitrov-Ngu)

### Репозиторий:

- assets - графические материалы для Readme файлика
- data_experiments - ноутбуки с обработкой датасетов
- model_experiments - ноутбуки с обучением моделек
- model_weights - лучшие веса обученных моделек

## Контент
- [Детекция дорожных знаков](#)
  - [Контент](#контент)
  - [Проблема](#проблема)
  - [Описание](#описание)
  - [Детекция знаков](#детекция-знаков)
    - [Данные](#данные)
    - [Статьи](#статьи)
    - [Видео](#видео)
    - [Архитектура](#архитектура)
    - [Демо](#демонстрация)
      - [Особенности и ограничения](#особенности-и-ограничения-системы)
  - [Future Roadmap](#future-roadmap)
  - [Contibution](#contributing)
  - [Вывод](#conclusion)
  - [Авторы](#authors)

## Проблема
Данный продукт решает следующие проблемы:
* Автоматическая детекция знаков
* Удобный юзер интерфейс
* Быстрый инференс

## Описание
Предлагаемая система видеонаблюдения предназначена для обеспечения комплексного мониторинга и обнаружения дорожных знаков. 

Все собранные данные хранятся в централизованной базе данных для последующего анализа и обучения модели.

## Детекция знаков
### Данные
[Данные 1](https://www.kaggle.com/datasets/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign )

[Данные 2](pytorch.org/vision/stable/generated/torchvision.datasets.GTSRB.html) 

[Данные 3](https://cg.cs.tsinghua.edu.cn/traffic-sign/)

[Данные 4](https://www.kaggle.com/datasets/valentynsichkar/traffic-signs-dataset-in-yolo-format/data) 

[Данные 5](https://universe.roboflow.com/cchegeu/russian-signs/model/14)

### Статьи
[Статья 1](https://www.researchgate.net/publication/346250677_Automatic_Traffic_Sign_Recognition_Artificial_Inteligence_-_Deep_Learning_Algorithm)

[Статья 2](https://link.springer.com/article/10.1007/s10639-022-11391-z)

### Видео
[Про разметку](https://www.youtube.com/watch?v=wjgnYyU6Ymc)

### Архитектура

<p align="center" width="100%">
    <img width="80%" src="assets/architecture.png">
</p>

### Frontend
![Alt text](assets/mvp_preview.png)

#### Особенности и ограничения 
- В текущей версии приложения ограничение по размеру видео составляет 200 МБ. Это важно учитывать при загрузке видеоматериалов.
- **Загрузка файлов**: пользователи могут загружать видеофайлы в форматах, таких как mp4, mov, avi, asf, m4v и mpeg-4. Загрузка происходит способом drag and drop. Во время загрузки пользователь видит сообщение «Upload a video». После успешной загрузки пользователь видит сообщение «Upload successful!».
- **Обработка видео**: приложение обрабатывает видео с использованием CV-модели. После завершения обработки пользователь видит соответствующий индикатор: «Extracting complete!».
- **Video**: после обработки отображается загруженное видео с ограничивающей рамкой (bounding box) в месте, где модель детектировала дорожный знак.

## Future  Roadmap
- Проверить дополнительные архитектуры (Fast CNN, Faster CNN)
- Улучшить инференс
- Добавить трекинг знаков
- Улучшить взаимодействие с пользователем


## Contributing
Скопируйте файл [`contributing.md`](https://github.com/Svyatocheck/DeepLearningPractice/blob/master/contributing.md).

## Вывод
Предлагаемая система видеонаблюдения создает комплексное решение для мониторинга и детекция дорожных знаков.

Благодаря алгоритмам нейронных сетей, эффективному управлению данными и возможностям немедленного оповещения, он обеспечивает надежный 
инструмент для детекции знаков и может использоваться на реальных кейсах.

## Авторы
- [Vladimir Dimitrov](https://github.com/Vladimir-Dimitrov-Ngu)

