title: com.catchingnow.tinyclipboardmanager

# com.catchingnow.tinyclipboardmanager

[Google Play Store](https://play.google.com/store/apps/details?id=com.catchingnow.tinyclipboardmanager)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// android.view.WindowManager$BadTokenException: Unable to add window -- token android.os.BinderProxy@92b837 is not valid; is your activity running?
// 	at android.view.ViewRootImpl.setView(ViewRootImpl.java:567)
// 	at android.view.WindowManagerGlobal.addView(WindowManagerGlobal.java:310)
// 	at android.view.WindowManagerImpl.addView(WindowManagerImpl.java:85)
// 	at android.app.Dialog.show(Dialog.java:319)
// 	at com.catchingnow.tinyclipboardmanager.ActivitySetting.checkAccessibilityPermission(ActivitySetting.java:115)
// 	at com.catchingnow.tinyclipboardmanager.ActivitySetting.access$100(ActivitySetting.java:21)
// 	at com.catchingnow.tinyclipboardmanager.ActivitySetting$1.onSharedPreferenceChanged(ActivitySetting.java:59)
// 	at android.app.SharedPreferencesImpl$EditorImpl.notifyListeners(SharedPreferencesImpl.java:479)
// 	at android.app.SharedPreferencesImpl$EditorImpl.apply(SharedPreferencesImpl.java:387)
// 	at android.preference.Preference.tryCommit(Preference.java:1415)
// 	at android.preference.Preference.persistString(Preference.java:1448)
// 	at android.preference.ListPreference.setValue(ListPreference.java:148)
// 	at android.preference.ListPreference.onDialogClosed(ListPreference.java:283)
// 	at android.preference.DialogPreference.onDismiss(DialogPreference.java:395)
// 	at android.app.Dialog$ListenersHandler.handleMessage(Dialog.java:1323)
// 	at android.os.Handler.dispatchMessage(Handler.java:102)
// 	at android.os.Looper.loop(Looper.java:148)
// 	at android.app.ActivityThread.main(ActivityThread.java:5417)
// 	at java.lang.reflect.Method.invoke(Native Method)
// 	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:726)
// 	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:616)

```



