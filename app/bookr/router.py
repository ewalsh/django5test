from reviews import models as review_models
import random

# define a function to take in module and return list of relevant classes
def classes_in_module(mod_list):
    return(
        list(
            filter(
                lambda x: x[0].isupper(),filter(
                    lambda x: '_' not in x, dir(review_models)
                )
            )
        )
    )


class SessionRouter:
    """
    routing session
    """
    route_app_labels = {"session"}

    def db_for_read(self, model, **hints):
        return 'default'

    def db_for_write(self, model, **hints):
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        # return None
        return 'default'

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return 'default'


class AuthRouter:
    """
    A router to control all database operations on models in the
    auth and contenttypes applications.
    """

    route_app_labels = {"auth", "contenttypes"}

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and contenttypes models go to auth_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return "default"
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth and contenttypes models go to auth_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return "default"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or contenttypes apps is
        involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels
            or obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        'auth_db' database.
        """
        if app_label in self.route_app_labels:
            return db == "default"
        return None



class DbRouter:
    """
    A router to control all database operations on models in the
    auth and contenttypes applications.
    """

    # route_app_labels = {"auth", "contenttypes"}

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and contenttypes models go to auth_db.
        """
        if model._name in classes_in_module(review_models):
            return random.choice(["reviews",    "reviews-repl"])
        return "default"

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth and contenttypes models go to auth_db.
        """
        if model._name in classes_in_module(review_models):
            return "reviews"
        return "default"

    def allow_relation(self, obj1, obj2, **hints):
        # """
        # Allow relations if a model in the auth or contenttypes apps is
        # involved.
        # """
        # if (
        #     obj1._meta.app_label in self.route_app_labels
        #     or obj2._meta.app_label in self.route_app_labels
        # ):
        #     return True
        # return None
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # """
        # Make sure the auth and contenttypes apps only appear in the
        # 'auth_db' database.
        # """
        # if app_label in self.route_app_labels:
        #     return db == "auth_db"
        # return None
        return True