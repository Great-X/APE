title: org.kore.kolabnotes.android

# org.kore.kolabnotes.android

[Google Play Store](https://play.google.com/store/apps/details?id=org.kore.kolabnotes.android)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.NullPointerException: Attempt to invoke virtual method 'android.print.PrintDocumentAdapter org.kore.kolabnotes.android.fragment.KolabNotesRichEditor.createPrintDocumentAdapter()' on a null object reference
// 	at org.kore.kolabnotes.android.fragment.DetailFragment.printNote(DetailFragment.java:1563)
// 	at org.kore.kolabnotes.android.fragment.DetailFragment.onOptionsItemSelected(DetailFragment.java:924)
// 	at android.app.Fragment.performOptionsItemSelected(Fragment.java:2326)
// 	at android.app.FragmentManagerImpl.dispatchOptionsItemSelected(FragmentManager.java:2072)
// 	at android.app.FragmentController.dispatchOptionsItemSelected(FragmentController.java:290)
// 	at android.app.Activity.onMenuItemSelected(Activity.java:2917)
// 	at android.support.v4.app.FragmentActivity.onMenuItemSelected(FragmentActivity.java:368)
// 	at android.support.v7.app.AppCompatActivity.onMenuItemSelected(AppCompatActivity.java:195)
// 	at android.support.v7.view.WindowCallbackWrapper.onMenuItemSelected(WindowCallbackWrapper.java:108)
// 	at android.support.v7.view.WindowCallbackWrapper.onMenuItemSelected(WindowCallbackWrapper.java:108)
// 	at android.support.v7.app.ToolbarActionBar$2.onMenuItemClick(ToolbarActionBar.java:65)
// 	at android.support.v7.widget.Toolbar$1.onMenuItemClick(Toolbar.java:202)
// 	at android.support.v7.widget.ActionMenuView$MenuBuilderCallback.onMenuItemSelected(ActionMenuView.java:780)
// 	at android.support.v7.view.menu.MenuBuilder.dispatchMenuItemSelected(MenuBuilder.java:822)
// 	at android.support.v7.view.menu.MenuItemImpl.invoke(MenuItemImpl.java:171)
// 	at android.support.v7.view.menu.MenuBuilder.performItemAction(MenuBuilder.java:973)
// 	at android.support.v7.view.menu.MenuPopup.onItemClick(MenuPopup.java:127)
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



