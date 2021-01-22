from flask import Flask, render_template, request, make_response, jsonify
import time

from music_module.handle_music import call_music



app = Flask(__name__)

@app.route('/')
def test():
    return render_template('splash.html')

@app.route('/music')
def music():
    return render_template('back.html')

@app.route('/get_song', methods=['GET', 'POST'])
def song():
    speech = request.get_json()
    speech_value = speech['Message']
    print(speech_value)
    split_song = speech_value.split()
    song_query = '+'.join(split_song)
    
    call_music(song_query)

    return 'done playing'
    
if __name__ == '__main__':
    app.run()