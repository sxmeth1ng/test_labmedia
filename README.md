Одностраничное веб-приложение на Django, которое отображает:

- **Точечный график** зависимости суммы платежа от даты (точки соединены линией)
- **Гистограмму** сумм платежей с именами плательщиков
- Кнопку переключения между графиками

Данные хранятся в СУБД.

---

## 🛠️ Стек технологий

- Python 3.9+
- Django 3.2+
- Chart.js 4.4.0 (CDN)
- PostgreSQL 10+ 
- psycopg2-binary (для PostgreSQL)

---

## 📦 Установка и запуск

### 1. Клонирование и виртуальное окружение

```bash
git clone https://github.com/sxmeth1ng/test_labmedia
cd payment_visualization
python -m venv venv
source venv\Scripts\activate
pip install -r requirements.txt
