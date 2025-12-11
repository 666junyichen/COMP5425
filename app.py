from flask import Flask, render_template, request, redirect, url_for, session, redirect
import json
import random

app = Flask(__name__)
app.secret_key = "zen-secret-key"

# 加载音乐库
with open("music.json", 'r') as f:
    music_library = json.load(f)

with open("predictions.json", "r") as f:
    predicted_emotions = json.load(f)

# BPM → 情绪映射
def map_bpm_to_emotion(bpm):
    if bpm < 65:
        return "Sad"
    elif bpm > 100:
        return "Happy"
    else:
        return "Calm"

# 情绪文案
emotion_messages = {
    "Happy": (
        "A lively heartbeat detected!\n"
        "You seem to be glowing with joy and vitality.\n"
        "Let’s celebrate your energy with uplifting music."
    ),
    "Sad": (
        "Your heart rhythm suggests a quiet, low emotional state.\n"
        "You're not alone — even cloudy skies pass.\n"
        "Let these gentle tunes carry you through."
    ),
    "Calm": (
        "Your heart beats with steady rhythm and clarity.\n"
        "You seem to be in a peaceful, centered state.\n"
        "Let the music flow gently with your breath."
    )
}


# 封面图路径
emotion_covers = {
    "Happy": "images/Mask group-1.png",
    "Sad": "images/Mask group-2.png",
    "Calm": "images/Mask group.png"
}

@app.route("/")
def index():
    # 初始页面（无音乐）
    return render_template("index.html", track_title=None)

@app.route("/simulate", methods=["POST"])
def simulate():
    try:
        bpm = int(request.form['bpm'])
    except:
        bpm = 76

    # 获取预测情绪或回退使用规则
    emotion = predicted_emotions.get(str(bpm), map_bpm_to_emotion(bpm))

    # 检索音乐
    matches = [track for track in music_library if track['emotion'].lower() == emotion.lower()]
    track = random.choice(matches) if matches else {"title": "", "filepath": "", "artist": ""}

    # 存入 session，供播放页使用
    session['track'] = {
        'bpm': bpm,
        'emotion': emotion,
        'emotion_text': emotion_messages[emotion],
        'track_title': track['title'],
        'track_artist': track['artist'],
        'cover_image': emotion_covers[emotion],
        'cover': track['cover'],
        'track_path': track['filepath']
    }

    # ✅ 重定向到播放页（避免刷新提示）
    return redirect(url_for('result'))

@app.route("/result")
def result():
    track = session.get('track')

    if not track:
        return redirect(url_for('index'))

    return render_template("index.html", **track)


@app.route("/stop", methods=["POST"])
def stop():
    session.clear()  # ✅ 清空所有 session 数据

    return render_template("index.html",
                           bpm=None,
                           emotion="Calm",
                           emotion_text="Music stopped. You can try again.",
                           track_title=None,
                           track_artist=None,
                           cover_image=emotion_covers["Calm"],
                           track_path=None)


if __name__ == '__main__':
    app.run(debug=True)
