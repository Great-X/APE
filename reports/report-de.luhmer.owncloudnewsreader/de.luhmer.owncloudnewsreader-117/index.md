title: de.luhmer.owncloudnewsreader

# de.luhmer.owncloudnewsreader

[Google Play Store](https://play.google.com/store/apps/details?id=de.luhmer.owncloudnewsreader)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.RuntimeException: Failure delivering result ResultInfo{who=null, request=15642, result=-1, data=Intent { cmp=de.luhmer.owncloudnewsreader/.SettingsActivity (has extras) }} to activity {de.luhmer.owncloudnewsreader/de.luhmer.owncloudnewsreader.NewsReaderListActivity}: java.lang.IllegalStateException: Can not perform this action after onSaveInstanceState
// 	at android.app.ActivityThread.deliverResults(ActivityThread.java:3699)
// 	at android.app.ActivityThread.handleSendResult(ActivityThread.java:3742)
// 	at android.app.ActivityThread.-wrap16(ActivityThread.java)
// 	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1393)
// 	at android.os.Handler.dispatchMessage(Handler.java:102)
// 	at android.os.Looper.loop(Looper.java:148)
// 	at android.app.ActivityThread.main(ActivityThread.java:5417)
// 	at java.lang.reflect.Method.invoke(Native Method)
// 	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:726)
// 	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:616)
// Caused by: java.lang.IllegalStateException: Can not perform this action after onSaveInstanceState
// 	at android.support.v4.app.FragmentManagerImpl.checkStateLoss(Unknown Source)
// 	at android.support.v4.app.FragmentManagerImpl.enqueueAction(Unknown Source)
// 	at android.support.v4.app.BackStackRecord.commitInternal(Unknown Source)
// 	at android.support.v4.app.BackStackRecord.commit(Unknown Source)
// 	at android.support.v4.app.DialogFragment.show(Unknown Source)
// 	at de.luhmer.owncloudnewsreader.NewsReaderListActivity.StartLoginFragment(Unknown Source)
// 	at de.luhmer.owncloudnewsreader.NewsReaderListActivity.startSync(Unknown Source)
// 	at de.luhmer.owncloudnewsreader.NewsReaderListActivity.resetUiAndStartSync(Unknown Source)
// 	at de.luhmer.owncloudnewsreader.NewsReaderListActivity.onActivityResult(Unknown Source)
// 	at android.app.Activity.dispatchActivityResult(Activity.java:6456)
// 	at android.app.ActivityThread.deliverResults(ActivityThread.java:3695)
// 	... 9 more

```



