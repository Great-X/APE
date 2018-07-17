title: com.crazyhitty.chdev.ks.munch

# com.crazyhitty.chdev.ks.munch

[Google Play Store](https://play.google.com/store/apps/details?id=com.crazyhitty.chdev.ks.munch)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.IllegalArgumentException: Comparison method violates its general contract!
// 	at java.util.TimSort.mergeLo(TimSort.java:761)
// 	at java.util.TimSort.mergeAt(TimSort.java:497)
// 	at java.util.TimSort.mergeCollapse(TimSort.java:424)
// 	at java.util.TimSort.sort(TimSort.java:210)
// 	at java.util.Arrays.sort(Arrays.java:1998)
// 	at java.util.Collections.sort(Collections.java:1900)
// 	at com.crazyhitty.chdev.ks.munch.feeds.FeedsPresenter.onSuccess(FeedsPresenter.java:99)
// 	at com.crazyhitty.chdev.ks.munch.feeds.FeedsLoaderInteractor.onSuccess(FeedsLoaderInteractor.java:104)
// 	at com.crazyhitty.chdev.ks.rssmanager.RssReader.parseRss(RssReader.java:82)
// 	at com.crazyhitty.chdev.ks.rssmanager.RssReader.onSuccess(RssReader.java:103)
// 	at com.crazyhitty.chdev.ks.rssmanager.RssParser.onPostExecute(RssParser.java:42)
// 	at com.crazyhitty.chdev.ks.rssmanager.RssParser.onPostExecute(RssParser.java:15)
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



