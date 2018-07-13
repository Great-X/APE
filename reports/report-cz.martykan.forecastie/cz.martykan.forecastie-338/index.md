title: cz.martykan.forecastie

# cz.martykan.forecastie

[Google Play Store](https://play.google.com/store/apps/details?id=cz.martykan.forecastie)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.NullPointerException: Attempt to invoke virtual method 'void android.support.v7.app.ActionBar.setTitle(java.lang.CharSequence)' on a null object reference
// 	at cz.martykan.forecastie.activities.MainActivity.updateTodayWeatherUI(MainActivity.java:421)
// 	at cz.martykan.forecastie.activities.MainActivity.access$200(MainActivity.java:67)
// 	at cz.martykan.forecastie.activities.MainActivity$TodayWeatherTask.updateMainUI(MainActivity.java:827)
// 	at cz.martykan.forecastie.tasks.GenericRequestTask.onPostExecute(GenericRequestTask.java:132)
// 	at cz.martykan.forecastie.activities.MainActivity$TodayWeatherTask.onPostExecute(MainActivity.java:809)
// 	at cz.martykan.forecastie.activities.MainActivity$TodayWeatherTask.onPostExecute(MainActivity.java:796)
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



