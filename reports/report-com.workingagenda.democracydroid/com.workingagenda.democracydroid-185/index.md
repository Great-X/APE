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
// 	at com.workingagenda.democracydroid.Adapters.ViewHolders.EpisodeViewHolder.onMenuItemClick(EpisodeViewHolder.java:250)
// 	at com.android.internal.view.menu.MenuItemImpl.invoke(MenuItemImpl.java:148)
// 	at com.android.internal.view.menu.MenuBuilder.performItemAction(MenuBuilder.java:904)
// 	at com.android.internal.view.menu.MenuBuilder.performItemAction(MenuBuilder.java:894)
// 	at com.android.internal.view.menu.MenuDialogHelper.onClick(MenuDialogHelper.java:167)
// 	at com.android.internal.app.AlertController$AlertParams$3.onItemClick(AlertController.java:1108)
// 	at android.widget.AdapterView.performItemClick(AdapterView.java:310)
// 	at android.widget.AbsListView.performItemClick(AbsListView.java:1145)
// 	at android.widget.AbsListView$PerformClick.run(AbsListView.java:3066)
// 	at android.widget.AbsListView$3.run(AbsListView.java:3903)
// 	at android.os.Handler.handleCallback(Handler.java:739)
// 	at android.os.Handler.dispatchMessage(Handler.java:95)
// 	at android.os.Looper.loop(Looper.java:148)
// 	at android.app.ActivityThread.main(ActivityThread.java:5417)
// 	at java.lang.reflect.Method.invoke(Native Method)
// 	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:726)
// 	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:616)

```



