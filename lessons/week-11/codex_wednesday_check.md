# Have this working by Wednesday night (under 3 minutes)

Thursday we build with an AI coding assistant. Last time a lot of class time went to install and sign-in trouble, so check it **before** class. If every line below says `OK`, you are done. All of this is on your own computer; nothing here needs a password typed into a chat or a Canvas page.

## 1. Paste this into a terminal (about 20 seconds)

Use the Linux terminal (Chromebook), a Mac Terminal, or the Windows WSL terminal.

```bash
chk() { if "$@" >/dev/null 2>&1; then echo "OK   $*"; else echo "FIX  $*"; fi; }
chk python3 -c 'import sys; assert sys.version_info >= (3, 9)'
chk git --version
chk codex --version
chk codex login status
```

You want four `OK` lines. A `FIX` line tells you which step to do below.

## 2. Check the course checker runs (about 10 seconds)

Put `relations_test_first_check.py` and `relations_test_first_concepts.md` (posted with this page) into one folder, then:

```bash
python3 relations_test_first_check.py
```

The last line should say `ALL CHECKS PASSED`. That proves Python works for Thursday.

## 3. If you see a `FIX` line

| Line | What to do |
|---|---|
| `python3 ...` | Install Python 3.9 or newer from python.org (or `sudo apt install python3` in the Linux terminal). Run step 1 again. |
| `git --version` | Install Git (`sudo apt install git` in the Linux terminal, or git-scm.com). Run step 1 again. |
| `codex --version` | Run the official installer from the [Codex CLI guide](https://developers.openai.com/codex/cli): `curl -fsSL https://chatgpt.com/codex/install.sh \| sh`. Close and reopen the terminal (so the new command is found), then run step 1 again. |
| `codex login status` | Type `codex`, choose **Sign in with ChatGPT**, and finish in the browser. If no browser opens, use the link it prints. Use your own account. Then `/quit` and run step 1 again. |

**If your account cannot use Codex, or something still says `FIX` after the table: do not buy anything.** Copy the four lines from step 1 (they contain no passwords or login codes) and send them to Jeremy before class, or bring the laptop to the start of class. A paper-and-Python path works for Thursday even without the assistant: the concept sheet and its checker need only Python.

**Never paste a password, login code, or key into a chat, Canvas, or an email.**
