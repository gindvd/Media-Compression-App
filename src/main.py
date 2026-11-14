from sys import platform


if platform.startswith("win"):
    """Set up VLC paths for the python-vlc library to use bundled VLC dlls / plugins in the bin folder"""

    import os
    from utils.resource_paths import resource_path

    vlc_dir = resource_path(os.path.join("bin", "vlc"))

    if not os.path.isdir(vlc_dir):
        raise SystemError("Missing VLC plugins folder!")

    os.environ["PYTHON_VLC_MODULE_PATH"] = str(vlc_dir)
    os.environ["PYTHON_VLC_LIB_PATH"] = str(os.path.join(vlc_dir, "libvlc.dll"))
    os.environ["VLC_PLUGIN_PATH"] = str(os.path.join(vlc_dir, "plugins"))

    # add dlls explicitly
    if hasattr(os, "add_dll_directory"):
        os.add_dll_directory(str(vlc_dir))

    os.environ["PATH"] = str(vlc_dir) + os.pathsep + os.environ.get("PATH", "")


from app import App

from bootstrapper.initialization import initialize_app


def main() -> None:
    app: App = initialize_app()
    app.mainloop()


if __name__ == "__main__":
    main()
