"""Run packaged scripts with isolated dependencies without changing Codex's Python."""
from pathlib import Path
import os, subprocess, sys
root = Path(__file__).resolve().parents[1]
if len(sys.argv) < 2:
    raise SystemExit('Usage: codex_run.py script.py [arguments]')
script = (root / 'scripts' / sys.argv[1]).resolve()
if script.parent != (root / 'scripts').resolve() or not script.is_file():
    raise SystemExit('Choose a packaged script filename.')
env = os.environ.copy()
env['PYTHONPATH'] = str(root / '.python-deps') + os.pathsep + env.get('PYTHONPATH', '')
env['PYTHONIOENCODING'] = 'utf-8'
raise SystemExit(subprocess.call([sys.executable, str(script), *sys.argv[2:]], env=env))
