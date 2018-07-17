title: libretasks.app

# libretasks.app

[Google Play Store](https://play.google.com/store/apps/details?id=libretasks.app)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// android.database.CursorIndexOutOfBoundsException: Index 0 requested, with a size of 0
// 	at android.database.AbstractCursor.checkPosition(AbstractCursor.java:460)
// 	at android.database.AbstractWindowedCursor.checkPosition(AbstractWindowedCursor.java:136)
// 	at android.database.AbstractWindowedCursor.getLong(AbstractWindowedCursor.java:74)
// 	at libretasks.app.model.CursorHelper.getLongFromCursor(CursorHelper.java:85)
// 	at libretasks.app.model.UIDbHelper.loadRuleSparse(UIDbHelper.java:566)
// 	at libretasks.app.model.UIDbHelper.loadRule(UIDbHelper.java:542)
// 	at libretasks.app.view.simple.ActivitySavedRules.editRule(ActivitySavedRules.java:264)
// 	at libretasks.app.view.simple.ActivitySavedRules.access$000(ActivitySavedRules.java:67)
// 	at libretasks.app.view.simple.ActivitySavedRules$1.onItemClick(ActivitySavedRules.java:111)
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



