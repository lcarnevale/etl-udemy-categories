# Collect Udemy course metadata
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

This project is intended how a first tentative to explore the ETL procedure. As example, I aim to gather Udemy courses metadata.

## QuickStart
Create a Python 3 virtual environment.
```bash
$ virtualenv -p python3 venv
$ source venv/bin/activate
```

Install all the dependencies.
```bash
$ pip install -r requirements.txt
```

Run the scraper with a course URL as input parameter and define a JSON object in output:
```bash
$ scrapy crawl udemy-course -a course_url=<UDEMY-COURSE-URL> -o course.json
```

## ETL Procedure
In the following, I provide an explanation about how the ETL procedure works over the implementation.

### Extract
The Extraction phase gathers the following metadata by the course page:
- URL;
- title;
- subtitle;
- average rating;
- amount of ratings;
- amount of students enrolled;
- last updated date;
- author;
- main language;
- price;
- "What you'll learn";
- "Requirements";
- hours of on-demand video;
- amount of articles;
- amount of downloadable resources.