:: Note: nuitka chosen over pyinstaller because it generates smaller exe files

nuitka ^
  --output-dir=build ^
  --onefile ^
  --standalone ^
  --windows-uac-admin ^
  --windows-icon-from-ico=BPS.ico ^
  --lto=yes ^
  --mingw64 ^
  --assume-yes-for-downloads ^
  RegionChanger.py
