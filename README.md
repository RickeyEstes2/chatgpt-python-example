Modified version of simple Python script [app.py](https://github.com/NextIdeaTechUS/chatgpt-python-example/raw/master/app.py), from the [GitHub repo](https://github.com/NextIdeaTechUS/chatgpt-python-example), which is referred to from [How to use ChatGPT with Python](https://blog.nextideatech.com/how-to-use-chatgpt-with-python/), to explore features of openai [ChatGPT](https://chat.openai.com/chat) on [Android 11 (API level 30)](https://developer.android.com/studio/releases/platforms#11 using the Pydroid 3 IDE for Python 3.9 https://play.google.com/store/apps/details?id=ru.iiec.pydroid3) and save the conversation to çhatlog.txt, in the same directory. 

You must have an openai account. If you don't, then you can [sign up for one](https://auth0.openai.com/u/signup/identifier?state=hKFo2SBPaUMyZmJqYW5IMzNVRXVvSnNYTWYtdFNBN05DSzA5d6Fur3VuaXZlcnNhbC1sb2dpbqN0aWTZIEJNTTVITDc4MU50c1FRLXYzXzNtUExtQTFVRzdURkRLo2NpZNkgRFJpdnNubTJNdTQyVDNLT3BxZHR3QjNOWXZpSFl6d0Q)

After signing up for an openai account, you need to generate an [API key](https://beta.openai.com/account/api-keys)

Then you need to replace OPEN_API_KEY, on line number 5 with the API you were given.


You must have pandas and openai installed, if you don't, then you need to:
pip install pandas
pip install openai