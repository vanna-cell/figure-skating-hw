\# Элементы фигурного катания



Проект генерирует данные об элементах фигурного катания и создаёт HTML-отчёт.



\## Команды



| Команда | Описание |

| `run.sh build\_generator` | Собрать образ генератора |

| `run.sh run\_generator` | Сгенерировать data.csv |

| `run.sh create\_local\_data` | Локальная генерация (без Docker) |

| `run.sh build\_reporter` | Собрать образ аналитика |

| `run.sh run\_reporter` | Создать HTML-отчёт |

| `run.sh structure` | Показать структуру проекта |

| `run.sh clear\_data` | Очистить папку data |

| `run.sh inside\_generator` | Проверить данные изнутри генератора |

| `run.sh inside\_reporter` | Проверить данные изнутри аналитика |

| `run.sh report\_server` | Запустить веб-сервер с отчётом |



\## Запуск веб-сервера



1\. Выполните `run.sh report\_server`

2\. Откройте в браузере `http://localhost:8080/report.html`

3\. Для остановки: `docker stop report-server`



\## Запуск в GitHub Codespaces



1\. Откройте репозиторий в Codespaces

2\. Выполните `./run.sh report\_server`

3\. Нажмите на вкладку \*\*Ports\*\* 

4\. Найдите порт 8080, нажмите на значок глобуса



\## Автор

Волкова Анна, ББИ2504

