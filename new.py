from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

video_put_arg = reqparse.RequestParser()
video_put_arg.add_argument("likes", type=int, help="Likes on video")
video_put_arg.add_argument("name", type=str, help="Name should be a string")
video_put_arg.add_argument("views", type=int, help="Views of video")

video = {}

class Video(Resource):
    def get(self, video_id):
        return videos[video_id], 201

    def post(self, video_id):
        args = video_put_arg.parse_args()
        return args

api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)