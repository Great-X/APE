title: org.mozilla.mozstumbler

# org.mozilla.mozstumbler

[Google Play Store](https://play.google.com/store/apps/details?id=org.mozilla.mozstumbler)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.InternalError: Thread starting during runtime shutdown
// 	at java.lang.Thread.nativeCreate(Native Method)
// 	at java.lang.Thread.start(Thread.java:1063)
// 	at org.apache.http.impl.conn.tsccm.AbstractConnPool.enableConnectionGC(AbstractConnPool.java:145)
// 	at org.apache.http.impl.conn.tsccm.ThreadSafeClientConnManager.createConnectionPool(ThreadSafeClientConnManager.java:125)
// 	at org.apache.http.impl.conn.tsccm.ThreadSafeClientConnManager.<init>(ThreadSafeClientConnManager.java:103)
// 	at org.acra.util.HttpRequest.getHttpClient(HttpRequest.java:214)
// 	at org.acra.util.HttpRequest.send(HttpRequest.java:141)
// 	at org.acra.sender.HttpSender.send(HttpSender.java:225)
// 	at org.acra.SendWorker.sendCrashReport(SendWorker.java:179)
// 	at org.acra.SendWorker.checkAndSendReports(SendWorker.java:141)
// 	at org.acra.SendWorker.run(SendWorker.java:77)

```



