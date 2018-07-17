title: com.hectorone.multismssender

# com.hectorone.multismssender

[Google Play Store](https://play.google.com/store/apps/details?id=com.hectorone.multismssender)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.NullPointerException: Attempt to invoke interface method 'java.util.Iterator java.lang.Iterable.iterator()' on a null object reference
// 	at android.os.Parcel.readException(Parcel.java:1626)
// 	at android.os.Parcel.readException(Parcel.java:1573)
// 	at com.android.internal.telephony.ISms$Stub$Proxy.sendMultipartTextForSubscriber(ISms.java:910)
// 	at android.telephony.SmsManager.sendMultipartTextMessageInternal(SmsManager.java:475)
// 	at android.telephony.SmsManager.sendMultipartTextMessage(SmsManager.java:457)
// 	at com.hectorone.multismssender.MultiSmsSender.sendMessage(MultiSmsSender.java:431)
// 	at com.hectorone.multismssender.MultiSmsSender$MessageSenderThread.run(MultiSmsSender.java:270)

```



