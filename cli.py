import click
from cafebabel.auth import user_datastore
from cafebabel.core import app
from cafebabel.core.models import Role, User, UserProfile, UserRoles
from peewee import create_model_tables, drop_model_tables


def _initdb():
    tables = [User, UserProfile, Role, UserRoles]
    drop_model_tables(tables, fail_silently=True)
    create_model_tables(tables, fail_silently=True)
    user_datastore.create_user(
        email='admin@example.com', password='password',
        firstname='Admin', lastname='Admin')
    click.echo('DB intialized.')


def _dropdb():
    tables = [User, UserProfile, Role, UserRoles]
    drop_model_tables(tables, fail_silently=True)
    click.echo('DB dropped.')


@app.cli.command()
def initdb():
    _initdb()
