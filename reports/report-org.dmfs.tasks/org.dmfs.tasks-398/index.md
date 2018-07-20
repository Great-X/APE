title: org.dmfs.tasks

# org.dmfs.tasks

[Google Play Store](https://play.google.com/store/apps/details?id=org.dmfs.tasks)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.IllegalArgumentException: LIST_ID must refer to an existing TaskList
// 	at org.dmfs.provider.tasks.processors.tasks.Validating.insert(Validating.java:67)
// 	at org.dmfs.provider.tasks.processors.tasks.Validating.insert(Validating.java:34)
// 	at org.dmfs.provider.tasks.TaskProvider.insertInTransaction(TaskProvider.java:888)
// 	at org.dmfs.provider.tasks.SQLiteContentProvider.insert(SQLiteContentProvider.java:154)
// 	at org.dmfs.provider.tasks.TaskProvider.insert(TaskProvider.java:92)
// 	at android.content.ContentProvider$Transport.insert(ContentProvider.java:263)
// 	at android.content.ContentResolver.insert(ContentResolver.java:1231)
// 	at org.dmfs.tasks.model.ContentSet.persist(ContentSet.java:240)
// 	at org.dmfs.tasks.QuickAddDialogFragment.createTask(QuickAddDialogFragment.java:370)
// 	at org.dmfs.tasks.QuickAddDialogFragment.onClick(QuickAddDialogFragment.java:402)
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



