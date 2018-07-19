title: de.kugihan.dictionaryformids.hmi_android

# de.kugihan.dictionaryformids.hmi_android

[Google Play Store](https://play.google.com/store/apps/details?id=de.kugihan.dictionaryformids.hmi_android)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.RuntimeException: Could not read input channel file descriptors from parcel.
// 	at android.view.InputChannel.nativeReadFromParcel(Native Method)
// 	at android.view.InputChannel.readFromParcel(InputChannel.java:148)
// 	at android.view.IWindowSession$Stub$Proxy.addToDisplay(IWindowSession.java:759)
// 	at android.view.ViewRootImpl.setView(ViewRootImpl.java:531)
// 	at android.view.WindowManagerGlobal.addView(WindowManagerGlobal.java:310)
// 	at android.view.WindowManagerImpl.addView(WindowManagerImpl.java:85)
// 	at android.widget.PopupWindow.invokePopup(PopupWindow.java:1258)
// 	at android.widget.PopupWindow.showAsDropDown(PopupWindow.java:1110)
// 	at android.widget.ListPopupWindow.show(ListPopupWindow.java:658)
// 	at com.android.internal.view.menu.MenuPopupHelper.tryShow(MenuPopupHelper.java:170)
// 	at android.widget.ActionMenuPresenter$OpenOverflowRunnable.run(ActionMenuPresenter.java:997)
// 	at android.os.Handler.handleCallback(Handler.java:739)
// 	at android.os.Handler.dispatchMessage(Handler.java:95)
// 	at android.os.Looper.loop(Looper.java:148)
// 	at android.app.ActivityThread.main(ActivityThread.java:5417)
// 	at java.lang.reflect.Method.invoke(Native Method)
// 	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:726)
// 	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:616)

```



