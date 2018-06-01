from flask import Flask
from flask_graphql import GraphQLView
from .schema import schema

app = Flask(__name__)
app.logger.propagate = True

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))
