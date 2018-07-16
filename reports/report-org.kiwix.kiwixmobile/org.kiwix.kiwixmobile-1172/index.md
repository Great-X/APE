title: org.kiwix.kiwixmobile

# org.kiwix.kiwixmobile

[Google Play Store](https://play.google.com/store/apps/details?id=org.kiwix.kiwixmobile)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.NullPointerException: Attempt to invoke virtual method 'void android.widget.ListView.invalidateViews()' on a null object reference
// 	at org.kiwix.kiwixmobile.downloader.DownloadService.playDownload(DownloadService.java:212)
// 	at org.kiwix.kiwixmobile.downloader.DownloadFragment$DownloadAdapter.lambda$getView$0(DownloadFragment.java:180)
// 	at org.kiwix.kiwixmobile.downloader.DownloadFragment$DownloadAdapter.access$lambda$0(DownloadFragment.java)
// 	at org.kiwix.kiwixmobile.downloader.DownloadFragment$DownloadAdapter$$Lambda$1.onClick(Unknown Source)
// 	at android.view.View.performClick(View.java:5204)
// 	at android.view.View$PerformClick.run(View.java:21153)
// 	at android.os.Handler.handleCallback(Handler.java:739)
// 	at android.os.Handler.dispatchMessage(Handler.java:95)
// 	at android.os.Looper.loop(Looper.java:148)
// 	at android.app.ActivityThread.main(ActivityThread.java:5417)
// 	at java.lang.reflect.Method.invoke(Native Method)
// 	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:726)
// 	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:616)

```



