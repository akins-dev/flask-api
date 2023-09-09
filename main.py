from flask import Flask, request
from flask_restful import Resource, Api, abort, reqparse

app = Flask(__name__)
api = Api(app)

channels = {}
videos = {}

def abort_if_channel_does_not_exist(channel_id: int) -> None:
    """
        int -> None
        aborts and sends a 404 status code if channel id
            not found
    """
    if channel_id not in channels:
        abort(404, message="Channel does not exist")

def abort_if_video_does_not_exist(video_id: int) -> None:
    if video_id not in videos:
        abort(404, message="Video does not exist")

def abort_if_channel_eixsts(channel_id: int) -> None:
    if channel_id in channels:
        abort(409, message="A channel with this ID already exists")

def abort_if_video_exists(video_id: int) -> None:
    if video_id in videos:
        abort(409, message="A video with that ID already exists")

# class Bobs:
#     NUM = 2
#     def __init__(self): pass

#     def __add__(self, num) -> int:
#         return Bobs().NUM + num

# neew = Bobs()
# print(neew + 4)

# args parser
video_create_args = reqparse.RequestParser()
video_create_args.add_argument("name", type=str, help="Name of video")
video_create_args.add_argument("views", type=int, help="Number of views on video")
video_create_args.add_argument("likes", type=int, help="Number of likes on video")

class Channel(Resource):
    def get(self, channel_id):
        abort_if_channel_does_not_exist(int(channel_id))
        return channels[channel_id]


class Video(Resource):
    def get(self, video_id):
        abort_if_video_does_not_exist(int(video_id))
        return videos[video_id]

    def put(self, video_id):
        abort_if_video_exists(int(video_id))
        args = video_create_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201

    def delete(self, video_id):
        abort_if_video_does_not_exist(int(video_id))
        del videos[video_id]
        return "", 204


api.add_resource(Channel, "/channel/<int:channel_id>")
api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)
         