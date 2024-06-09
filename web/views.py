from web import app
from flask import render_template, redirect
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume, ISimpleAudioVolume
from comtypes import CLSCTX_ALL
import pythoncom
from ctypes import POINTER, cast


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    メイン画面
    """
    # win32com開始前に呼出
    pythoncom.CoInitialize()
    # スピーカーデバイス取得
    devices = AudioUtilities.GetSpeakers()
    # インターフェース取得
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = interface.QueryInterface(IAudioEndpointVolume)
    # 現在マスターボリューム取得
    master_vol = volume.GetMasterVolumeLevelScalar()
    print({"CurrentMasteVolScale": master_vol})
    # win32com終了後に呼出
    pythoncom.CoUninitialize()

    vol_text = f"{(master_vol * 100):.0f}%"
    return render_template('volume.html', vol_text=vol_text)


@app.route('/api/master-volume/up')
def masterVolUp():
    """
    音量上げる
    """
    print("masterVolUp")
    # win32com開始前に呼出
    pythoncom.CoInitialize()
    # スピーカーデバイス取得
    devices = AudioUtilities.GetSpeakers()
    # インターフェース取得
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = interface.QueryInterface(IAudioEndpointVolume)
    # 現在マスターボリューム取得
    master_vol = volume.GetMasterVolumeLevelScalar()
    print({"CurrentMasteVolScale": master_vol})
    # 音量は5%ずつ増やす
    master_vol += 0.05
    volume.SetMasterVolumeLevelScalar(
        1 if 1 < master_vol else master_vol, None)
    pythoncom.CoUninitialize()

    return redirect('/')


@app.route('/api/master-volume/down')
def masterVolDown():
    """
    音量下げる
    """
    print("masterVolDown")
    # win32com開始前に呼出
    pythoncom.CoInitialize()
    # スピーカーデバイス取得
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = interface.QueryInterface(IAudioEndpointVolume)
    # 現在マスターボリューム取得
    master_vol = volume.GetMasterVolumeLevelScalar()
    print({"CurrentMasteVolScale": master_vol})
    # 音量は10%ずつ減らす
    master_vol += -0.1
    volume.SetMasterVolumeLevelScalar(
        0 if master_vol < 0 else master_vol, None)
    pythoncom.CoUninitialize()

    return redirect('/')


@app.route('/api/master-volume/mute')
def masterVolMute():
    """
    音量0
    """
    print("masterVolDown")
    # win32com開始前に呼出
    pythoncom.CoInitialize()
    # スピーカーデバイス取得
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = interface.QueryInterface(IAudioEndpointVolume)
    # 現在マスターボリューム取得
    master_vol = volume.GetMasterVolumeLevelScalar()
    print({"CurrentMasteVolScale": master_vol})
    volume.SetMasterVolumeLevelScalar(0, None)
    pythoncom.CoUninitialize()

    return redirect('/')
