title: com.bijoysingh.quicknote

# com.bijoysingh.quicknote

[Google Play Store](https://play.google.com/store/apps/details?id=com.bijoysingh.quicknote)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// android.util.AndroidRuntimeException: Calling startActivity() from outside of an Activity  context requires the FLAG_ACTIVITY_NEW_TASK flag. Is this really what you want?
// 	at android.app.ContextImpl.startActivity(ContextImpl.java:672)
// 	at android.app.ContextImpl.startActivity(ContextImpl.java:659)
// 	at android.content.ContextWrapper.startActivity(ContextWrapper.java:331)
// 	at com.github.bijoysingh.starter.util.IntentUtils$ShareBuilder.share(IntentUtils.java:115)
// 	at com.bijoysingh.quicknote.database.Note.share(Note.java:195)
// 	at com.bijoysingh.quicknote.service.FloatingNoteService$loadView$2.onClick(FloatingNoteService.kt:96)
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



