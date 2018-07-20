title: de.k3b.android.androFotoFinder

# de.k3b.android.androFotoFinder

[Google Play Store](https://play.google.com/store/apps/details?id=de.k3b.android.androFotoFinder)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.NullPointerException: Attempt to invoke virtual method 'boolean java.io.File.mkdirs()' on a null object reference
// 	at de.k3b.android.util.AndroidFileCommands.execRename(AndroidFileCommands.java:217)
// 	at de.k3b.android.androFotoFinder.directory.DirectoryPickerFragment.onRenameDirAnswer(DirectoryPickerFragment.java:471)
// 	at de.k3b.android.androFotoFinder.directory.DirectoryPickerFragment.access$1200(DirectoryPickerFragment.java:90)
// 	at de.k3b.android.androFotoFinder.directory.DirectoryPickerFragment$11.onDialogResult(DirectoryPickerFragment.java:451)
// 	at de.k3b.android.widget.Dialogs$5.onClick(Dialogs.java:138)
// 	at com.android.internal.app.AlertController$ButtonHandler.handleMessage(AlertController.java:163)
// 	at android.os.Handler.dispatchMessage(Handler.java:102)
// 	at android.os.Looper.loop(Looper.java:148)
// 	at android.app.ActivityThread.main(ActivityThread.java:5417)
// 	at java.lang.reflect.Method.invoke(Native Method)
// 	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:726)
// 	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:616)

```



