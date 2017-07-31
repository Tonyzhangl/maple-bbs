#!/usr/bin/env python
from flask import request, g, current_app
from flask_wtf.csrf import CsrfProtect
from flask_admin import Admin
from flask_babelex import Babel, Domain
from flask_babelex import lazy_gettext as _
from flask_avatar import Avatar
from flask_maple.middleware import Middleware
from flask_maple.models import db
from flask_maple.app import App
from flask_maple.json import CustomJSONEncoder
from flask_maple.bootstrap import Bootstrap
from flask_maple.error import Error
from flask_maple.captcha import Captcha
from flask_maple.redis import Redis
from flask_maple.mail import Mail
from flask_cache import Cache
from flask_principal import Principal
from flask_login import LoginManager
from flask_msearch import Search
import os


def register_babel():
    base_path = os.path.abspath(os.path.dirname(__file__))
    translations = os.path.join(base_path, os.pardir, 'translations')
    domain = Domain(translations)
    babel = Babel(default_domain=domain)

    @babel.localeselector
    def get_locale():
        user = getattr(g, 'user', None)
        if user is not None:
            if request.path.startswith('/admin'):
                return 'zh_Hans_CN'
            if g.user.is_authenticated:
                return user.setting.locale or 'zh'
        return request.accept_languages.best_match(current_app.config[
            'LANGUAGES'].keys())

    @babel.timezoneselector
    def get_timezone():
        user = getattr(g, 'user', None)
        if user is not None:
            if g.user.is_authenticated:
                return user.setting.timezone or 'UTC'
        return 'UTC'

    return babel


def register_login():
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.session_protection = "strong"
    login_manager.login_message = _("Please login to access this page.")
    # login_manager.anonymous_user = Anonymous

    @login_manager.user_loader
    def user_loader(id):
        from forums.api.user.models import User
        user = User.query.get(int(id))
        return user

    # @login_manager.token_loader
    # def load_token(token):
    #     return None

    return login_manager


babel = register_babel()
db = db
admin = Admin(name='HonMaple', template_mode='bootstrap3')
avatar = Avatar()
csrf = CsrfProtect()
bootstrap = Bootstrap(
    css=('styles/monokai.css', 'styles/mine.css',
         'tags/css/bootstrap-tokenfield.css', 'select2/css/select2.min.css'),
    js=('styles/upload.js', 'styles/forums.js', 'styles/following.js',
        'styles/topic.js', 'tags/bootstrap-tokenfield.min.js',
        'select2/js/select2.min.js'),
    use_auth=True)
captcha = Captcha()
error = Error()
redis_data = Redis()
cache = Cache()
mail = Mail()
principal = Principal()
login_manager = register_login()
maple_app = App(json=CustomJSONEncoder)
middleware = Middleware()
search = Search(db=db)
