title: com.workingagenda.democracydroid

# com.workingagenda.democracydroid

[Google Play Store](https://play.google.com/store/apps/details?id=com.workingagenda.democracydroid)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.NullPointerException: uriString
// 	at android.net.Uri$StringUri.<init>(Uri.java:475)
// 	at android.net.Uri$StringUri.<init>(Uri.java)
// 	at android.net.Uri.parse(Uri.java:437)
// 	at com.workingagenda.democracydroid.Adapters.ViewHolders.EpisodeViewHolder.startMediaIntent(EpisodeViewHolder.java:180)
// 	at com.workingagenda.democracydroid.Adapters.ViewHolders.EpisodeViewHolder.loadEpisode(EpisodeViewHolder.java:162)
// 	at com.workingagenda.democracydroid.Adapters.ViewHolders.EpisodeViewHolder.access$000(EpisodeViewHolder.java:50)
// 	at com.workingagenda.democracydroid.Adapters.ViewHolders.EpisodeViewHolder$1.onClick(EpisodeViewHolder.java:104)
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



