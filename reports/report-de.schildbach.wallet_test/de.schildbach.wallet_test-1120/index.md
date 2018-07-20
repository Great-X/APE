title: de.schildbach.wallet_test

# de.schildbach.wallet_test

[Google Play Store](https://play.google.com/store/apps/details?id=de.schildbach.wallet_test)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.IllegalStateException: attempt to re-open an already-closed object: SQLiteQuery: SELECT * FROM address_book WHERE (address LIKE ? OR label LIKE ?)
// 	at android.database.sqlite.SQLiteClosable.acquireReference(SQLiteClosable.java:55)
// 	at android.database.sqlite.SQLiteQuery.fillWindow(SQLiteQuery.java:58)
// 	at android.database.sqlite.SQLiteCursor.fillWindow(SQLiteCursor.java:151)
// 	at android.database.sqlite.SQLiteCursor.onMove(SQLiteCursor.java:123)
// 	at android.database.AbstractCursor.moveToPosition(AbstractCursor.java:236)
// 	at android.database.CursorWrapper.moveToPosition(CursorWrapper.java:197)
// 	at android.widget.CursorAdapter.getItem(CursorAdapter.java:246)
// 	at android.widget.AutoCompleteTextView.buildImeCompletions(AutoCompleteTextView.java:1132)
// 	at android.widget.AutoCompleteTextView.showDropDown(AutoCompleteTextView.java:1092)
// 	at android.widget.AutoCompleteTextView.updateDropDownForFilter(AutoCompleteTextView.java:975)
// 	at android.widget.AutoCompleteTextView.onFilterComplete(AutoCompleteTextView.java:957)
// 	at android.widget.Filter$ResultsHandler.handleMessage(Filter.java:285)
// 	at android.os.Handler.dispatchMessage(Handler.java:102)
// 	at android.os.Looper.loop(Looper.java:148)
// 	at android.app.ActivityThread.main(ActivityThread.java:5417)
// 	at java.lang.reflect.Method.invoke(Native Method)
// 	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:726)
// 	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:616)

```



