title: com.biglybt.android.client

# com.biglybt.android.client

[Google Play Store](https://play.google.com/store/apps/details?id=com.biglybt.android.client)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.IndexOutOfBoundsException: setSpan (1 ... 1) ends beyond length 0
// 	at android.text.SpannableStringBuilder.checkRange(SpannableStringBuilder.java:1090)
// 	at android.text.SpannableStringBuilder.setSpan(SpannableStringBuilder.java:665)
// 	at android.text.SpannableStringBuilder.setSpan(SpannableStringBuilder.java:658)
// 	at android.text.Selection.setSelection(Selection.java:76)
// 	at android.widget.EditText.setSelection(EditText.java:91)
// 	at android.widget.NumberPicker$SetSelectionCommand.run(NumberPicker.java:2246)
// 	at android.os.Handler.handleCallback(Handler.java:739)
// 	at android.os.Handler.dispatchMessage(Handler.java:95)
// 	at android.os.Looper.loop(Looper.java:148)
// 	at android.app.ActivityThread.main(ActivityThread.java:5417)
// 	at java.lang.reflect.Method.invoke(Native Method)
// 	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:726)
// 	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:616)

```



