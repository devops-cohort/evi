import unittest
import pytest

from flask import abort, url_for
from flask_testing import TestCase
from os import getenv
from application import app, db
from application.model import Users

class TestBase(TestCase):

    def create_app(self):

         # pass in test configurations
        config_name = 'testing'
        app.config.update(
     SQLALCHEMY_DATABASE_URI='mysql+pymysql://'+str(getenv('MYSQL_USER'))+':'+str(getenv('MYSQL_PASSWORD'))+'@'+str(getenv('MYSQL_URL'))+'/'+str(getenv('DatabaseB'))        )

        return app
 
    
    '''def setUp(self):
        
        """
        Will be called before every test
        """

        db.session.commit()
        db.drop_all()
        db.create_all()

        # create test admin user
        admin = Users(first_name="admin", last_name="admin", email="admin@admin.com", password="admin2016")

        # create test non-admin user
        employee = Users(first_name="test", last_name="user", email="test@user.com", password="test2016")

        # save users to database
        db.session.add(admin)
        db.session.add(employee)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()
'''
class testing(TestBase):

    def test_home_view(self):
        """
        test that about page is accessible without login
        """
        response = self.client.get(url_for('about'))
        self.assertEqual(response.status_code, 200)
    def test_home_view(self):
        """
        test that about page is accessible without login
        """
        response = self.client.get(url_for('login'))
        self.assertEqual(response.status_code, 200)
    def test_home_view(self):
        """
        test that about page is accessible without login
        """
        response = self.client.get(url_for('signup'))
        self.assertEqual(response.status_code, 200)
'''

    def test_login_view(self):
        """
        test that login page is accessible without login
        """
        response = self.client.get(url_for('login'))
        self.assertEqual(response.status_code, 200)
    def test_user_view(self):
        """
        test tgat user page is inaccessible without login and redirects to login page tgeb to dashboard
        """
        target_url=url_for('user',user_id=2)
        redirect_url=url_for('login',next=target_url)
        response =self.client.get(target_url)
        self.assertEqual(responce.status_code,302)
        self.assertRedirects(response,redirect_url
'''
