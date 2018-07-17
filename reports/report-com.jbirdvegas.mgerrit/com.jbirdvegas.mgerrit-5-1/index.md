title: com.jbirdvegas.mgerrit

# com.jbirdvegas.mgerrit

[Google Play Store](https://play.google.com/store/apps/details?id=com.jbirdvegas.mgerrit)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.RuntimeException: Unable to start activity ComponentInfo{com.jbirdvegas.mgerrit/com.jbirdvegas.mgerrit.activities.GerritControllerActivity}: java.lang.RuntimeException: Parcel android.os.Parcel@7249f8b: Unmarshalling unknown type code 28 at offset 1820
// 	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2416)
// 	at android.app.ActivityThread.handleLaunchActivity(ActivityThread.java:2476)
// 	at android.app.ActivityThread.-wrap11(ActivityThread.java)
// 	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1344)
// 	at android.os.Handler.dispatchMessage(Handler.java:102)
// 	at android.os.Looper.loop(Looper.java:148)
// 	at android.app.ActivityThread.main(ActivityThread.java:5417)
// 	at java.lang.reflect.Method.invoke(Native Method)
// 	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:726)
// 	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:616)
// Caused by: java.lang.RuntimeException: Parcel android.os.Parcel@7249f8b: Unmarshalling unknown type code 28 at offset 1820
// 	at android.os.Parcel.readValue(Parcel.java:2340)
// 	at android.os.Parcel.readSparseArrayInternal(Parcel.java:2675)
// 	at android.os.Parcel.readSparseArray(Parcel.java:1967)
// 	at android.os.Parcel.readValue(Parcel.java:2321)
// 	at android.os.Parcel.readArrayMapInternal(Parcel.java:2614)
// 	at android.os.BaseBundle.unparcel(BaseBundle.java:221)
// 	at android.os.Bundle.getSparseParcelableArray(Bundle.java:856)
// 	at com.android.internal.policy.PhoneWindow.restoreHierarchyState(PhoneWindow.java:2033)
// 	at android.app.Activity.onRestoreInstanceState(Activity.java:1008)
// 	at android.app.Activity.performRestoreInstanceState(Activity.java:963)
// 	at android.app.Instrumentation.callActivityOnRestoreInstanceState(Instrumentation.java:1163)
// 	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2389)
// 	... 9 more

```



