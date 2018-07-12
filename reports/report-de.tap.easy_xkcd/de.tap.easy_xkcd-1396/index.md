title: de.tap.easy_xkcd

# de.tap.easy_xkcd

[Google Play Store](https://play.google.com/store/apps/details?id=de.tap.easy_xkcd)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.NullPointerException: Attempt to invoke virtual method 'java.lang.Object android.content.Context.getSystemService(java.lang.String)' on a null object reference
// 	at de.tap.easy_xkcd.fragments.comics.ComicFragment$ComicAdapter.<init>(ComicFragment.java:135)
// 	at de.tap.easy_xkcd.fragments.comics.ComicBrowserFragment$ComicBrowserPagerAdapter.<init>(ComicBrowserFragment.java:196)
// 	at de.tap.easy_xkcd.fragments.comics.ComicBrowserFragment$updateNewest.onPostExecute(ComicBrowserFragment.java:170)
// 	at de.tap.easy_xkcd.fragments.comics.ComicBrowserFragment$updateNewest.onPostExecute(ComicBrowserFragment.java:128)
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



