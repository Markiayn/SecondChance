from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from datetime import datetime


from main.views import home_page
from main.models import Article


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)


    def test_home_page_returns_correct_html(self):
        request = HttpRequest()  
        response = home_page(request)  
        html = response.content.decode('utf8')  
        self.assertTrue(html.startswith('<html>'))  
        self.assertIn('<title>Markiyan</title>', html)  
        self.assertTrue(html.endswith('</html>'))  



class Articlemodeltest(TestCase):

    def test_article_model_save_and_retrieve(self):

        article1 = Article(
            title = 'tilte 1',
            fulltext = 'fulltext 1',
            summary = 'summary 1',
            category = 'category 1',
            pubdate = datetime.now(),
        )
        article1.save()



        article2 = Article(
            title = 'tilte 2',
            fulltext = 'fulltext 2',
            summary = 'summary 2',
            category = 'category 2',
            pubdate = datetime.now(),
        )
        article2.save()

        allArticles = Article.objects.all()


        self.assertEqual(len(allArticles), 2)

        self.assertEqual(
            allArticles[0].title ,
            article1.title
        )


        self.assertEqual(
            allArticles[1].title ,
            article2.title
        )