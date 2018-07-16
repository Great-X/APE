title: org.bienvenidoainternet.app

# org.bienvenidoainternet.app

[Google Play Store](https://play.google.com/store/apps/details?id=org.bienvenidoainternet.app)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.NullPointerException: Attempt to invoke virtual method 'org.bienvenidoainternet.app.structure.Board org.bienvenidoainternet.app.structure.BoardItem.getParentBoard()' on a null object reference
// 	at layout.FragmentBoardItemList.deletePost(FragmentBoardItemList.java:784)
// 	at layout.FragmentBoardItemList.onContextItemSelected(FragmentBoardItemList.java:358)
// 	at android.support.v4.app.Fragment.performContextItemSelected(Fragment.java:2085)
// 	at android.support.v4.app.FragmentManagerImpl.dispatchContextItemSelected(FragmentManager.java:2173)
// 	at android.support.v4.app.FragmentController.dispatchContextItemSelected(FragmentController.java:308)
// 	at android.support.v4.app.FragmentActivity.onMenuItemSelected(FragmentActivity.java:370)
// 	at android.support.v7.app.AppCompatActivity.onMenuItemSelected(AppCompatActivity.java:147)
// 	at android.support.v7.view.WindowCallbackWrapper.onMenuItemSelected(WindowCallbackWrapper.java:100)
// 	at android.support.v7.view.WindowCallbackWrapper.onMenuItemSelected(WindowCallbackWrapper.java:100)
// 	at com.android.internal.policy.PhoneWindow$DialogMenuCallback.onMenuItemSelected(PhoneWindow.java:5013)
// 	at com.android.internal.view.menu.MenuBuilder.dispatchMenuItemSelected(MenuBuilder.java:761)
// 	at com.android.internal.view.menu.MenuItemImpl.invoke(MenuItemImpl.java:152)
// 	at com.android.internal.view.menu.MenuBuilder.performItemAction(MenuBuilder.java:904)
// 	at com.android.internal.view.menu.MenuBuilder.performItemAction(MenuBuilder.java:894)
// 	at com.android.internal.view.menu.MenuDialogHelper.onClick(MenuDialogHelper.java:167)
// 	at com.android.internal.app.AlertController$AlertParams$3.onItemClick(AlertController.java:1108)
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



