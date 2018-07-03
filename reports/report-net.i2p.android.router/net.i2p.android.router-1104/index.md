title: net.i2p.android.router

# net.i2p.android.router

[Timeline](./vis-timeline.html)

```
java.lang.RuntimeException
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2416)
	at android.app.ActivityThread.handleLaunchActivity(ActivityThread.java:2476)
	at android.app.ActivityThread.handleRelaunchActivity(ActivityThread.java:4077)
	at android.app.ActivityThread.-wrap15(ActivityThread.java)
	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1350)
	at android.os.Handler.dispatchMessage(Handler.java:102)
	at android.os.Looper.loop(Looper.java:148)
	at android.app.ActivityThread.main(ActivityThread.java:5417)
	at java.lang.reflect.Method.invoke(Native Method)
	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:726)
	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:616)
Caused by: java.lang.NullPointerException
	at net.i2p.android.wizard.model.AbstractWizardModel.load(AbstractWizardModel.java:70)
	at net.i2p.android.wizard.ui.AbstractWizardActivity.onCreate(AbstractWizardActivity.java:52)
	at android.app.Activity.performCreate(Activity.java:6251)
	at android.app.Instrumentation.callActivityOnCreate(Instrumentation.java:1107)
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2369)
	... 10 more

```

