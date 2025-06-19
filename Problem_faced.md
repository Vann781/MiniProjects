Problems Faced While Building My AI Diary App
Using Python + HuggingFace Transformers + Speech Recognition + Firebase

1️⃣ Version Compatibility Issues
🐍 Python version: Initially I was using Python 3.11 and 3.12

HuggingFace Transformers and PyTorch are most stable on Python 3.9 / 3.10

Many errors came when using Python 3.11+, like:

ImportError: cannot import name 'TypeIs' from 'typing_extensions'

module 'tensorflow' has no attribute 'data'

Solution: Downgraded to Python 3.10
(But eventually I wanted to run it on 3.11 so fixed other lib versions)

2️⃣ Transformers + Tensorflow Conflicts
Transformers library tries to load Tensorflow by default

But many models (like distilroberta) work better with PyTorch

Faced error:
ValueError: Your currently installed version of Keras is Keras 3, but this is not yet supported in Transformers.
Fix:
pipeline(..., framework="pt")

Forced to use PyTorch, no TensorFlow needed.

3️⃣ torch + typing_extensions Error
Got error:
ImportError: cannot import name 'TypeIs' from 'typing_extensions'


Cause: PyTorch needed older version of typing_extensions

Fixed by matching compatible versions of:

PyTorch

typing_extensions

transformers

 4️⃣ speech_recognition & PyAudio Issue
For speech to text, I used speech_recognition lib.

But it depends on PyAudio which:

Is difficult to install on Windows

Needs portaudio drivers

Faced error:
AttributeError: Could not find PyAudio; check installation

Solution:

Installed pyaudio wheel manually

Used this:
pip install pipwin
pipwin install pyaudio


5️⃣ HuggingFace Model Download & Caching
Model downloads automatically from HuggingFace Hub

Initially gave this warning:
huggingface_hub cache-system uses symlinks by default...
Fixed by:

Enabling Developer Mode on Windows

OR ignoring the warning (safe to ignore)
6️⃣ Deprecated arguments warning
return_all_scores=True is now deprecated

New method:
pipeline(..., top_k=None)
But my code still works with return_all_scores=True, no big issue

7️⃣ Mixing Multiple Package Versions
After 3-4 installs/uninstalls, got conflict:
sentence-transformers 4.1.0 requires transformers>=4.41.0, but you have transformers 4.36.2

Solution:

Did a clean reinstall:

pip uninstall transformers torch tokenizers
pip install transformers==4.41.1 torch==2.2.2 tokenizers==0.15.2

Summary:
| Problem                   | Solution                   |
| ------------------------- | -------------------------- |
| Python 3.11 not working   | Switched to 3.10           |
| TF vs PT clash            | Forced PT (framework="pt") |
| PyAudio missing           | Manual install via pipwin  |
| typing\_extensions errors | Version fix                |
| Model caching warnings    | Safe to ignore             |
| Deprecation warnings      | Updated method             |



What I Learned:
Real world project = version compatibility matters a lot

Never trust pip install transformers blindly 😅

Read HuggingFace docs properly — models are either PT or TF

Windows users: installing PyAudio is tricky!
