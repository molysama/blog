#!/usr/bin/python
# -*- coding: utf-8 -*-

from tornado.web import url
from app.http.controllers.index_controller import IndexController
from app.http.controllers.auth.github_controller import GithubOAuth2LoginController

routes = [
    url(r"/", IndexController),
    url(r"/auth/github", GithubOAuth2LoginController),
]