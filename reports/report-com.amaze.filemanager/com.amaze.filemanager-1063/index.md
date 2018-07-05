title: com.amaze.filemanager

# com.amaze.filemanager

[Timeline](./vis-timeline.html)

```
android.view.ViewRootImpl$CalledFromWrongThreadException
	at android.view.ViewRootImpl.checkThread(ViewRootImpl.java:6556)
	at android.view.ViewRootImpl.requestLayout(ViewRootImpl.java:907)
	at android.view.View.requestLayout(View.java:18728)
	at android.view.View.requestLayout(View.java:18728)
	at android.view.View.requestLayout(View.java:18728)
	at android.view.View.requestLayout(View.java:18728)
	at android.view.View.requestLayout(View.java:18728)
	at android.view.View.requestLayout(View.java:18728)
	at android.support.v4.widget.DrawerLayout.requestLayout(DrawerLayout.java:1265)
	at android.view.View.requestLayout(View.java:18728)
	at android.widget.RelativeLayout.requestLayout(RelativeLayout.java:360)
	at android.view.View.requestLayout(View.java:18728)
	at android.widget.AbsListView.requestLayout(AbsListView.java:1975)
	at android.widget.ListView.setAdapter(ListView.java:519)
	at com.amaze.filemanager.activities.MainActivity.refreshDrawer(MainActivity.java:1519)
	at com.amaze.filemanager.activities.MainActivity.onBookAdded(MainActivity.java:2188)
	at com.amaze.filemanager.utils.DataUtils$1.run(DataUtils.java:210)
	at android.os.Handler.handleCallback(Handler.java:739)
	at android.os.Handler.dispatchMessage(Handler.java:95)
	at android.os.Looper.loop(Looper.java:148)
	at android.os.HandlerThread.run(HandlerThread.java:61)

```

