title: com.knirirr.beecount

# com.knirirr.beecount

[Google Play Store](https://play.google.com/store/apps/details?id=com.knirirr.beecount)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.OutOfMemoryError: Failed to allocate a 7672332 byte allocation with 2279216 free bytes and 2MB until OOM
// 	at dalvik.system.VMRuntime.newNonMovableArray(Native Method)
// 	at android.graphics.Bitmap.nativeCreate(Native Method)
// 	at android.graphics.Bitmap.createBitmap(Bitmap.java:831)
// 	at android.graphics.Bitmap.createBitmap(Bitmap.java:808)
// 	at android.graphics.Bitmap.createBitmap(Bitmap.java:775)
// 	at com.knirirr.beecount.BeeCountApplication.setBackground(BeeCountApplication.java:84)
// 	at com.knirirr.beecount.NewProjectActivity.onSharedPreferenceChanged(NewProjectActivity.java:282)
// 	at android.app.SharedPreferencesImpl$EditorImpl.notifyListeners(SharedPreferencesImpl.java:479)
// 	at android.app.SharedPreferencesImpl$EditorImpl.apply(SharedPreferencesImpl.java:387)
// 	at android.preference.Preference.tryCommit(Preference.java:1415)
// 	at android.preference.Preference.persistBoolean(Preference.java:1681)
// 	at android.preference.TwoStatePreference.setChecked(TwoStatePreference.java:81)
// 	at android.preference.TwoStatePreference.onClick(TwoStatePreference.java:66)
// 	at android.preference.Preference.performClick(Preference.java:994)
// 	at android.preference.PreferenceScreen.onItemClick(PreferenceScreen.java:214)
// 	at android.widget.AdapterView.performItemClick(AdapterView.java:310)
// 	at android.widget.AbsListView.performItemClick(AbsListView.java:1145)
// 	at android.widget.AbsListView$PerformClick.run(AbsListView.java:3066)
// 	at android.widget.AbsListView$3.run(AbsListView.java:3903)
// 	at android.os.Handler.handleCallback(Handler.java:739)
// 	at android.os.Handler.dispatchMessage(Handler.java:95)
// 	at android.os.Looper.loop(Looper.java:148)
// 	at android.app.ActivityThread.main(ActivityThread.java:5417)
// 	at java.lang.reflect.Method.invoke(Native Method)
// 	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:726)
// 	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:616)

```



