title: de.saschahlusiak.freebloks

# de.saschahlusiak.freebloks

[Google Play Store](https://play.google.com/store/apps/details?id=de.saschahlusiak.freebloks)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.IllegalStateException: The content of the adapter has changed but ListView did not receive a notification. Make sure the content of your adapter is not modified from a background thread, but only from the UI thread. Make sure your adapter calls notifyDataSetChanged() when its content changes. [in ListView(2131558477, class android.widget.ListView) with Adapter(class de.saschahlusiak.freebloks.lobby.ChatListAdapter)]
// 	at android.widget.ListView.layoutChildren(ListView.java:1573)
// 	at android.widget.AbsListView.onWindowFocusChanged(AbsListView.java:2983)
// 	at android.view.View.dispatchWindowFocusChanged(View.java:9534)
// 	at android.view.ViewGroup.dispatchWindowFocusChanged(ViewGroup.java:1200)
// 	at android.view.ViewGroup.dispatchWindowFocusChanged(ViewGroup.java:1204)
// 	at android.view.ViewGroup.dispatchWindowFocusChanged(ViewGroup.java:1204)
// 	at android.view.ViewGroup.dispatchWindowFocusChanged(ViewGroup.java:1204)
// 	at android.view.ViewGroup.dispatchWindowFocusChanged(ViewGroup.java:1204)
// 	at android.view.ViewGroup.dispatchWindowFocusChanged(ViewGroup.java:1204)
// 	at android.view.ViewRootImpl$ViewRootHandler.handleMessage(ViewRootImpl.java:3378)
// 	at android.os.Handler.dispatchMessage(Handler.java:102)
// 	at android.os.Looper.loop(Looper.java:148)
// 	at android.app.ActivityThread.main(ActivityThread.java:5417)
// 	at java.lang.reflect.Method.invoke(Native Method)
// 	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:726)
// 	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:616)

```



