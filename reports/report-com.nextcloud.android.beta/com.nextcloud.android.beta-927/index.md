title: com.nextcloud.android.beta

# com.nextcloud.android.beta

[Timeline](./vis-timeline.html)

```
java.lang.RuntimeException
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2416)
	at android.app.ActivityThread.handleLaunchActivity(ActivityThread.java:2476)
	at android.app.ActivityThread.-wrap11(ActivityThread.java)
	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1344)
	at android.os.Handler.dispatchMessage(Handler.java:102)
	at android.os.Looper.loop(Looper.java:148)
	at android.app.ActivityThread.main(ActivityThread.java:5417)
	at java.lang.reflect.Method.invoke(Native Method)
	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:726)
	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:616)
Caused by: java.lang.NullPointerException
	at com.owncloud.android.datamodel.ArbitraryDataProvider.getBooleanValue(ArbitraryDataProvider.java:125)
	at com.owncloud.android.ui.fragment.contactsbackup.ContactsBackupFragment.onCreateView(ContactsBackupFragment.java:141)
	at android.support.v4.app.Fragment.performCreateView(Fragment.java:2346)
	at android.support.v4.app.FragmentManagerImpl.moveToState(FragmentManager.java:1428)
	at android.support.v4.app.FragmentManagerImpl.moveFragmentToExpectedState(FragmentManager.java:1759)
	at android.support.v4.app.FragmentManagerImpl.moveToState(FragmentManager.java:1827)
	at android.support.v4.app.BackStackRecord.executeOps(BackStackRecord.java:797)
	at android.support.v4.app.FragmentManagerImpl.executeOps(FragmentManager.java:2596)
	at android.support.v4.app.FragmentManagerImpl.executeOpsTogether(FragmentManager.java:2383)
	at android.support.v4.app.FragmentManagerImpl.removeRedundantOperationsAndExecute(FragmentManager.java:2338)
	at android.support.v4.app.FragmentManagerImpl.execPendingActions(FragmentManager.java:2245)
	at android.support.v4.app.FragmentManagerImpl.dispatchStateChange(FragmentManager.java:3248)
	at android.support.v4.app.FragmentManagerImpl.dispatchActivityCreated(FragmentManager.java:3200)
	at android.support.v4.app.FragmentController.dispatchActivityCreated(FragmentController.java:195)
	at android.support.v4.app.FragmentActivity.onStart(FragmentActivity.java:597)
	at android.support.v7.app.AppCompatActivity.onStart(AppCompatActivity.java:177)
	at com.owncloud.android.ui.activity.BaseActivity.onStart(BaseActivity.java:189)
	at com.owncloud.android.ui.activity.DrawerActivity.onStart(DrawerActivity.java:1380)
	at com.owncloud.android.ui.activity.FileActivity.onStart(FileActivity.java:186)
	at android.app.Instrumentation.callActivityOnStart(Instrumentation.java:1237)
	at android.app.Activity.performStart(Activity.java:6268)
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2379)
	... 9 more

```

