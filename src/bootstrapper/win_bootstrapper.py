import os

from ctypes import windll

try:
    windll.user32.SetProcessDpiAwarenessContext(-4)
except AttributeError:
    windll.shcore.SetProcessDpiAwareness(2)

from app import App

from models.app_state import AppState
from models.services import Services

from services.ffmpeg_service import FFmpegService
from services.ffprobe_service import FFprobeService
from services.vlc_playback_service import VLCService

from utils.resource_paths import resource_path
from utils.file_utils import check_file, check_path


def initialize_win(app_state: AppState) -> App:
    
    ffmpeg_path: str = resource_path(os.path.join("bin", "ffmpeg.exe"))
    check_file(ffmpeg_path)

    ffprobe_path: str = resource_path(os.path.join("bin", "ffprobe.exe"))
    check_file(ffprobe_path)

    services = Services(
        ffmpeg_service=FFmpegService(ffmpeg_path=ffmpeg_path),
        ffprobe_service=FFprobeService(path=ffprobe_path),
        vlc_service=VLCService()
    )

    app: App = App(app_state=app_state, services=services)

    icon_path: str = resource_path(
        os.path.join("assets", "images", "icons", "thestrawhat.ico")
    )

    app.iconbitmap(icon_path)

    return app
