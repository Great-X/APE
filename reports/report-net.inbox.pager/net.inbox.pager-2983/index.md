title: net.inbox.pager

# net.inbox.pager

[Google Play Store](https://play.google.com/store/apps/details?id=net.inbox.pager)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.IllegalStateException: database not open
// 	at net.sqlcipher.database.SQLiteDatabase.queryWithFactory(SQLiteDatabase.java:1677)
// 	at net.sqlcipher.database.SQLiteDatabase.query(SQLiteDatabase.java:1634)
// 	at net.sqlcipher.database.SQLiteDatabase.query(SQLiteDatabase.java:1723)
// 	at net.inbox.db.DBAccess.get_messages_count(DBAccess.java:506)
// 	at net.inbox.InboxPreferences$7.onClick(InboxPreferences.java:256)
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



