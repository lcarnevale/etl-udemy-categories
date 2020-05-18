#!/usr/bin/env python
"""ETL process for gathering Udemy courses metadata by category.
"""

__author__ = "Lorenzo Carnevale"
__license__ = "MIT"
__email__ = "lorenzocarnevale@gmail.com"

# standard libraries
import re
# third parties libraries
import scrapy


class UdemyCourseSpider(scrapy.Spider):
    name = 'udemy-course'

    def __init__(self, course, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = [
            f'https://www.udemy.com/course/{course}/',
        ]

    def parse(self, response):
        yield {
            'url': self.__get_url(response),
            'title': self.__get_title(response),
            'subtitle': self.__get_subtitle(response),
            'avg_rating': self.__get_avg_rating(response),
            'rating': self.__get_rating(response),
            'students_enrolled': self.__get_enrollment(response),
            'last_update': self.__get_last_update(response),
            'author': self.__get_author(response),
            'language': self.__get_language(response),
            'price': self.__get_price(response),
            'learning_goals': self.__get_learning_goals(response),
            'requirements': self.__get_requirements(response),
            'duration': self.__get_duration(response),
            'articles_amount': self.__get_aticles_amount(response),
            'downloadable': self.__get_downloadable(response)
        }

    def __get_url(self, response):
        return "Not implemented yet"

    def __get_title(self, response):
        pattern = "div.clp-lead__title::text"
        return response.css(pattern).get(). \
            strip()

    def __get_subtitle(self, response):
        pattern = "div.clp-lead__headline::text"
        return response.css(pattern).get(). \
            strip()

    def __get_avg_rating(self, response):
        id_pattern = 'span.tooltip-container span::attr(id)'
        id = response.css(id_pattern).get()
        avg_rating_pattern = '[id="%s"]::text' % id
        avg_rating = response.css(avg_rating_pattern).get(). \
            strip()
        return float(avg_rating)

    def __get_rating(self, response):
        return "Not implemented yet"

    def __get_enrollment(self, response):
        data_purpose = 'enrollment'
        pattern = '[data-purpose="%s"]::text' % data_purpose
        enrollment = response.css(pattern).get(). \
            strip()
        enrollment = re.findall(r'[0-9]+', enrollment)
        return int(''.join(enrollment))

    def __get_last_update(self, response):
        return response.css('div.last-update-date span::text').get(). \
            strip(). \
            split(' ')[-1]

    def __get_author(self, response):
        data_purpose = 'instructor-name-top'
        pattern = 'span[data-purpose="%s"] a::text' % data_purpose
        return response.css(pattern).get(). \
            strip()

    def __get_language(self, response):
        return "Not implemented yet"

    def __get_price(self, response):
        return "Not implemented yet"

    def __get_learning_goals(self, response):
        pattern = 'ul.what-you-get__items span.what-you-get__text::text'
        learning_goals = response.css(pattern).getall()
        return '. '.join(learning_goals)

    def __get_requirements(self, response):
        pattern = 'ul.requirements__list li.requirements__item::text'
        requirements = response.css(pattern).getall()
        return '. '.join(requirements)

    def __get_duration(self, response):
        data_purpose = 'video-content-length'
        pattern = 'span[data-purpose="%s"]::text' % data_purpose
        duration_string = response.css(pattern).get(). \
            strip()
        return duration_string.split(" ")[0]

    def __get_aticles_amount(self, response):
        return "Not implemented yet"

    def __get_downloadable(self, response):
        return "Not implemented yet"