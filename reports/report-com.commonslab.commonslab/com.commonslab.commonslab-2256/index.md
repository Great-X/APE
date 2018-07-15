title: com.commonslab.commonslab

# com.commonslab.commonslab

[Google Play Store](https://play.google.com/store/apps/details?id=com.commonslab.commonslab)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.NullPointerException: Attempt to invoke virtual method 'void com.commonslab.commonslab.Activities.LoginActivity.toggleLoadingScreen()' on a null object reference
// 	at com.commonslab.commonslab.Fragments.LoginFragment$7.onFailure(LoginFragment.java:186)
// 	at apiwrapper.commons.wikimedia.org.Network.Tasks.UserLoginTask.onPostExecute(UserLoginTask.java:59)
// 	at apiwrapper.commons.wikimedia.org.Network.Tasks.UserLoginTask.onPostExecute(UserLoginTask.java:22)
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



