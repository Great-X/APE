title: com.commonslab.commonslab

# com.commonslab.commonslab

[Google Play Store](https://play.google.com/store/apps/details?id=com.commonslab.commonslab)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.NullPointerException: Attempt to invoke virtual method 'boolean android.app.Activity.isDestroyed()' on a null object reference
// 	at com.bumptech.glide.manager.RequestManagerRetriever.assertNotDestroyed(RequestManagerRetriever.java:133)
// 	at com.bumptech.glide.manager.RequestManagerRetriever.get(RequestManagerRetriever.java:102)
// 	at com.bumptech.glide.Glide.with(Glide.java:653)
// 	at com.commonslab.commonslab.Fragments.RegisterFragment$1.onCaptchaReceived(RegisterFragment.java:73)
// 	at apiwrapper.commons.wikimedia.org.Network.Tasks.GetCaptchaTask.onPostExecute(GetCaptchaTask.java:50)
// 	at apiwrapper.commons.wikimedia.org.Network.Tasks.GetCaptchaTask.onPostExecute(GetCaptchaTask.java:20)
// 	at android.os.AsyncTask.finish(AsyncTask.java:651)
// 	at android.os.AsyncTask.-wrap1(AsyncTask.java)
// 	at android.os.AsyncTask$InternalHandler.handleMessage(AsyncTask.java:668)
// 	at android.os.Handler.dispatchMessage(Handler.java:102)
// 	at android.os.Looper.loop(Looper.java:148)
// 	at android.app.ActivityThread.main(ActivityThread.java:5417)
// 	at java.lang.reflect.Method.invoke(Native Method)
// 	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:726)
// 	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:616)

```



