# Установка

Для установки необходимых библиотек используйте
```bash
pip3 install -r requirements.txt
```

Для генерации __pdf__ файла решения лабораторных работ достаточно иметь установленные [TeXiFy](https://plugins.jetbrains.com/plugin/9473-texify-idea), __pandoc__ и __basictex__.
```bash
brew install pandoc
```
```bash
brew install basictex
```

# Генерация решения

Для того, чтобы сгенерировать решение, используйте команду
```bash
pandoc [название_директории]/solution.tex -o [название_директории]/output.pdf
```