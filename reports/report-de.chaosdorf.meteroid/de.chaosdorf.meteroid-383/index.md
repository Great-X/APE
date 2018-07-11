title: de.chaosdorf.meteroid

# de.chaosdorf.meteroid

[Google Play Store](https://play.google.com/store/apps/details?id=de.chaosdorf.meteroid)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.IllegalArgumentException: Illegal URL: http://metej8q0u01pq6t351ep823tv36htj7bx77x378g06lm10vys8n3a0m060640lw75l317jf638m401/api/v1/
// 	at retrofit2.Retrofit$Builder.baseUrl(Retrofit.java:454)
// 	at de.chaosdorf.meteroid.util.Connection.initializeRetrofit(Connection.java:118)
// 	at de.chaosdorf.meteroid.util.Connection.upgradeAPIversion(Connection.java:91)
// 	at de.chaosdorf.meteroid.util.Connection.reset(Connection.java:66)
// 	at de.chaosdorf.meteroid.SetHostname.saveHostname(SetHostname.java:138)
// 	at de.chaosdorf.meteroid.SetHostname.onOptionsItemSelected(SetHostname.java:97)
// 	at android.app.Activity.onMenuItemSelected(Activity.java:2914)
// 	at com.android.internal.policy.PhoneWindow.onMenuItemSelected(PhoneWindow.java:1151)
// 	at com.android.internal.view.menu.MenuBuilder.dispatchMenuItemSelected(MenuBuilder.java:761)
// 	at com.android.internal.view.menu.MenuItemImpl.invoke(MenuItemImpl.java:152)
// 	at com.android.internal.view.menu.MenuBuilder.performItemAction(MenuBuilder.java:904)
// 	at com.android.internal.view.menu.MenuBuilder.performItemAction(MenuBuilder.java:894)
// 	at android.widget.ActionMenuView.invokeItem(ActionMenuView.java:616)
// 	at com.android.internal.view.menu.ActionMenuItemView.onClick(ActionMenuItemView.java:141)
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



