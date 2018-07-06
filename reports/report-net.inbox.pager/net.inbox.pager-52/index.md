title: net.inbox.pager

# net.inbox.pager

[Google Play Store](https://play.google.com/store/apps/details?id=net.inbox.pager)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.IllegalStateException: database not open
// 	at net.sqlcipher.database.SQLiteDatabase.execSQL(SQLiteDatabase.java:2262)
// 	at net.inbox.db.DBAccess.rekey_db(DBAccess.java:152)
// 	at net.inbox.SettingsFragment$3.onCheckedChanged(SettingsFragment.java:97)
// 	at android.widget.CompoundButton.setChecked(CompoundButton.java:156)
// 	at android.widget.Switch.setChecked(Switch.java:1070)
// 	at android.widget.Switch.toggle(Switch.java:1065)
// 	at android.widget.CompoundButton.performClick(CompoundButton.java:120)
// 	at android.view.View$PerformClick.run(View.java:21153)
// 	at android.os.Handler.handleCallback(Handler.java:739)
// 	at android.os.Handler.dispatchMessage(Handler.java:95)
// 	at android.os.Looper.loop(Looper.java:148)
// 	at android.app.ActivityThread.main(ActivityThread.java:5417)
// 	at java.lang.reflect.Method.invoke(Native Method)
// 	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:726)
// 	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:616)

```



