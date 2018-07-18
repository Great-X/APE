title: io.github.phora.aeondroid

# io.github.phora.aeondroid

[Google Play Store](https://play.google.com/store/apps/details?id=io.github.phora.aeondroid)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.NumberFormatException: Invalid double: ""
// 	at java.lang.StringToReal.invalidReal(StringToReal.java:63)
// 	at java.lang.StringToReal.parseDouble(StringToReal.java:267)
// 	at java.lang.Double.parseDouble(Double.java:301)
// 	at java.lang.Double.valueOf(Double.java:338)
// 	at io.github.phora.aeondroid.workers.AeonDroidService.recheckGps(AeonDroidService.java:251)
// 	at io.github.phora.aeondroid.workers.AeonDroidService$RefreshManualLocationListener.onTimezoneUpdate(AeonDroidService.java:433)
// 	at io.github.phora.aeondroid.workers.UpdateTimezoneListener.onSharedPreferenceChanged(UpdateTimezoneListener.java:67)
// 	at android.app.SharedPreferencesImpl$EditorImpl.notifyListeners(SharedPreferencesImpl.java:479)
// 	at android.app.SharedPreferencesImpl$EditorImpl.commit(SharedPreferencesImpl.java:465)
// 	at io.github.phora.aeondroid.workers.UpdateTimezoneListener.onSharedPreferenceChanged(UpdateTimezoneListener.java:59)
// 	at android.app.SharedPreferencesImpl$EditorImpl.notifyListeners(SharedPreferencesImpl.java:479)
// 	at android.app.SharedPreferencesImpl$EditorImpl.apply(SharedPreferencesImpl.java:387)
// 	at android.preference.Preference.tryCommit(Preference.java:1415)
// 	at android.preference.Preference.persistString(Preference.java:1448)
// 	at android.preference.EditTextPreference.setText(EditTextPreference.java:92)
// 	at android.preference.EditTextPreference.onDialogClosed(EditTextPreference.java:146)
// 	at android.preference.DialogPreference.onDismiss(DialogPreference.java:395)
// 	at android.app.Dialog$ListenersHandler.handleMessage(Dialog.java:1323)
// 	at android.os.Handler.dispatchMessage(Handler.java:102)
// 	at android.os.Looper.loop(Looper.java:148)
// 	at android.app.ActivityThread.main(ActivityThread.java:5417)
// 	at java.lang.reflect.Method.invoke(Native Method)
// 	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:726)
// 	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:616)

```



