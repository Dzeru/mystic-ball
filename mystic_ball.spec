# -*- mode: python -*-
a = Analysis(['mystic_ball.py'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)

a.datas += [('mystic_ball.png','C:\\bagpack\\auni\\subjects\\TechProgPython\\mystic_ball\\mystic_ball.png','DATA'),
            ('mystic_ball_logo.ico','C:\\bagpack\\auni\\subjects\\TechProgPython\\mystic_ball\\mystic_ball_logo.ico','DATA')]
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='mystic_ball.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False ,
          icon='C:\\bagpack\\auni\\subjects\\TechProgPython\\mystic_ball\\mystic_ball_logo.ico')