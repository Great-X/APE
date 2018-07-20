title: de.schildbach.wallet_test

# de.schildbach.wallet_test

[Google Play Store](https://play.google.com/store/apps/details?id=de.schildbach.wallet_test)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.IllegalStateException
// 	at android.support.v4.util.Preconditions.checkState(Preconditions.java:130)
// 	at android.support.v4.util.Preconditions.checkState(Preconditions.java:142)
// 	at de.schildbach.wallet.ui.send.SweepWalletFragment.maybeDecodeKey(SweepWalletFragment.java:376)
// 	at de.schildbach.wallet.ui.send.SweepWalletFragment.access$900(SweepWalletFragment.java:104)
// 	at de.schildbach.wallet.ui.send.SweepWalletFragment$6.run(SweepWalletFragment.java:370)
// 	at android.os.Handler.handleCallback(Handler.java:739)
// 	at android.os.Handler.dispatchMessage(Handler.java:95)
// 	at android.os.Looper.loop(Looper.java:148)
// 	at android.app.ActivityThread.main(ActivityThread.java:5417)
// 	at java.lang.reflect.Method.invoke(Native Method)
// 	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:726)
// 	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:616)

```



