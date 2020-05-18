# Collect Udemy course metadata

This project aims to gather Udemy course metadata.

### QuickStart
The scraper requires a course URL as input parameter and creates a JSON object in output:

```bash
scrapy crawl udemy-course -a course=sell-on-amazon-as-small-start-up -o course.json
```

### Extract
The following metadata are extracted by the course page:
- URL of course
- Title
- Subtitle
- Avg. rating
- Amount of ratings
- Amount of students enrolled
- Last updated date
- Name of author
- Language (only the one next to the speech bubble)
- Price
- What you'll learn (in one column, formatted as text)
- Requirements (in one column, formatted as text)
- hours of on-demand video
- amount of articles
- amount of downloadable resources

More specifically, I want all courses from those two categories:
https://www.udemy.com/courses/business/home-business/ (1382 courses)
https://www.udemy.com/courses/business/entrepreneurship/ (3511 courses)

An example detail page would be this one:
https://www.udemy.com/course/sell-on-amazon-as-small-start-up/