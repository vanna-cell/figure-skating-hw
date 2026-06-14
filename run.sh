#!/bin/bash

case "$1" in
    build_generator)
        echo "Сборка образа генератора..."
        docker build -t generator-image ./generator
        ;;
    run_generator)
        echo "Запуск генератора..."
        docker run --rm -v "%cd%/data:/data" generator-image
        echo "CSV-файл создан в data/data.csv"
        ;;
    create_local_data)
        echo "Локальная генерация..."
        mkdir local_data
        python generator/generate.py local_data
        echo "Файл создан в local_data/data.csv"
        ;;
    build_reporter)
        echo "Сборка образа аналитика..."
        docker build -t reporter-image ./reporter
        ;;
    run_reporter)
        echo "Запуск аналитика..."
        docker run --rm -v "%cd%/data:/data" reporter-image
        echo "HTML-отчёт создан в data/report.html"
        ;;
    structure)
        echo "=== Структура проекта ==="
        dir
        echo ""
        echo "=== generator/ ==="
        dir generator
        echo ""
        echo "=== reporter/ ==="
        dir reporter
        echo ""
        echo "=== data/ ==="
        dir data
        ;;
    clear_data)
        echo "Очистка data/..."
        del /q data\*.csv data\*.html 2>nul
        echo "data/ очищена"
        ;;
    inside_generator)
        echo "Содержимое /data изнутри контейнера генератора:"
        docker run --rm -v "%cd%/data:/data" --entrypoint /bin/sh generator-image -c "ls -la /data"
        ;;
    inside_reporter)
        echo "Содержимое /data изнутри контейнера аналитика:"
        docker run --rm -v "%cd%/data:/data" --entrypoint /bin/sh reporter-image -c "ls -la /data"
        ;;
    report_server)
        echo "Запуск веб-сервера для report.html..."
        docker run --rm -d -p 8080:80 -v "%cd%/data:/usr/share/nginx/html:ro" --name report-server nginx:alpine
        echo "Сервер запущен. Откройте http://localhost:8080/report.html"
        echo "Для остановки сервера выполните: docker stop report-server"
        ;;
    *)
        echo "Использование: run.sh {build_generator|run_generator|create_local_data|build_reporter|run_reporter|structure|clear_data|inside_generator|inside_reporter|report_server}"
        exit 1
        ;;
esac