title: org.lumicall.android

# org.lumicall.android

[Google Play Store](https://play.google.com/store/apps/details?id=org.lumicall.android)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.NullPointerException: Attempt to read from field 'long org.sipdroid.sipua.UserAgentProfile.sipIdentityId' on a null object reference
// 	at org.sipdroid.sipua.SipdroidEngine.call(SipdroidEngine.java:740)
// 	at org.lumicall.android.sip.DialCandidateHelper.call(DialCandidateHelper.java:54)
// 	at org.sipdroid.sipua.ui.Sipdroid.call_menu(Sipdroid.java:763)
// 	at org.sipdroid.sipua.ui.Sipdroid$4.onClick(Sipdroid.java:296)
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



